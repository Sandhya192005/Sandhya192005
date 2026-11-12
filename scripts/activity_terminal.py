"""Generate an animated "terminal" SVG of recent public GitHub activity.

Reads the user's public events (and, when GITHUB_TOKEN is set, last-year
contribution total via GraphQL), then writes assets/activity-terminal.svg:
a terminal window that types a command, prints recent activity line by line,
shows a summary, and loops.

Usage:
    python scripts/activity_terminal.py [--user NAME] [--out PATH]
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import urllib.request
from html import escape

API = "https://api.github.com"
MAX_LINES = 7

# palette (matches profile banner)
BG = "#0b1426"
BAR = "#111d36"
BORDER = "#26375c"
TEXT = "#e2e8f0"
MUTED = "#64748b"
YELLOW = "#facc15"
GREEN = "#22c55e"
BLUE = "#60a5fa"
PURPLE = "#c084fc"
ORANGE = "#f97316"


def _get(url: str, token: str | None, body: dict | None = None):
    req = urllib.request.Request(url, data=json.dumps(body).encode() if body else None)
    req.add_header("Accept", "application/vnd.github+json")
    req.add_header("User-Agent", "profile-activity-terminal")
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    if body:
        req.add_header("Content-Type", "application/json")
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def contributions_last_year(user: str, token: str | None) -> int | None:
    if not token:
        return None
    q = {"query": "query($u:String!){user(login:$u){contributionsCollection{contributionCalendar{totalContributions}}}}",
         "variables": {"u": user}}
    try:
        d = _get(f"{API}/graphql", token, q)
        return d["data"]["user"]["contributionsCollection"]["contributionCalendar"]["totalContributions"]
    except Exception:
        return None


def ago(ts: str, now: dt.datetime) -> str:
    """Card refreshes daily, so show a date rather than a relative time."""
    t = dt.datetime.fromisoformat(ts.replace("Z", "+00:00"))
    return f"{t:%d %b}".lstrip("0")


def short_repo(full: str, user: str) -> str:
    owner, name = full.split("/", 1)
    return name if owner.lower() == user.lower() else full


def build_lines(events: list[dict], user: str, now: dt.datetime) -> list[tuple[str, str, str, str]]:
    """Return (symbol, colour, text, when) tuples, newest first."""
    events = sorted(events, key=lambda e: e["created_at"], reverse=True)
    merged_prs = {
        (e["repo"]["name"], e["payload"].get("number"))
        for e in events
        if e["type"] == "PullRequestEvent" and e["payload"].get("action") in ("merged", "closed")
    }
    out: list[tuple[str, str, str, str]] = []
    push_group: dict | None = None

    def flush():
        nonlocal push_group
        if push_group:
            n = push_group["n"]
            branch = push_group["branch"]
            where = push_group["repo"] + ("" if branch in ("main", "master") else f" ({branch})")
            out.append(("↑", BLUE, f"pushed {n} update{'s' if n > 1 else ''} to {where}", push_group["when"]))
            push_group = None

    for e in events:
        repo_full = e["repo"]["name"]
        if repo_full.lower() == f"{user}/{user}".lower():
            continue  # profile README edits are noise here
        repo = short_repo(repo_full, user)
        p = e.get("payload", {})
        when = ago(e["created_at"], now)
        typ = e["type"]

        if typ == "PushEvent":
            branch = (p.get("ref") or "").removeprefix("refs/heads/")
            if push_group and push_group["repo"] == repo and push_group["branch"] == branch:
                push_group["n"] += 1
                continue
            flush()
            push_group = {"repo": repo, "branch": branch, "n": 1, "when": when}
            continue

        flush()
        line = None
        if typ == "PullRequestEvent":
            action = p.get("action")
            num = p.get("number") or p.get("pull_request", {}).get("number")
            merged = action == "merged" or (action == "closed" and p.get("pull_request", {}).get("merged"))
            if merged:
                line = ("✔", GREEN, f"merged PR #{num} into {repo}", when)
            elif action == "opened" and (repo_full, num) not in merged_prs:
                line = ("⇄", PURPLE, f"opened PR #{num} in {repo}", when)
        elif typ == "CreateEvent":
            if p.get("ref_type") == "repository":
                line = ("+", YELLOW, f"created repository {repo}", when)
            elif p.get("ref_type") == "branch" and p.get("ref") not in ("main", "master"):
                line = ("↳", ORANGE, f"started branch {p.get('ref')} in {repo}", when)
        elif typ == "ReleaseEvent":
            line = ("◆", YELLOW, f"released {p.get('release', {}).get('tag_name', '')} of {repo}", when)
        elif typ == "IssuesEvent" and p.get("action") == "opened":
            line = ("●", ORANGE, f"opened issue #{p.get('issue', {}).get('number')} in {repo}", when)
        elif typ == "WatchEvent":
            line = ("★", YELLOW, f"starred {repo}", when)
        elif typ == "ForkEvent":
            line = ("⑂", BLUE, f"forked {repo}", when)
        if line:
            out.append(line)
        if len(out) >= MAX_LINES:
            break
    flush()
    return out[:MAX_LINES]


def render(lines, summary: str) -> str:
    W, PAD, LH = 1200, 36, 34
    top = 96
    H = top + LH * (len(lines) + 3) + 30
    char_w = 9.6  # approx width of 16px monospace
    cmd = 'git log --author="sandhya" --activity --recent'

    # timeline (seconds)
    t_cmd_start, t_cmd_end = 0.6, 2.6
    t = t_cmd_end + 0.4
    steps = []
    for sym, col, text, when in lines:
        steps.append((t, t + 0.7))
        t += 0.9
    t_sum = (t + 0.2, t + 1.2)
    total = t_sum[1] + 5.0  # hold, then loop

    def kt(x):
        return f"{x / total:.4f}"

    def reveal(cid, x, y, width, start, end):
        return (
            f'<clipPath id="{cid}"><rect x="{x}" y="{y - 22}" height="32" width="0">'
            f'<animate attributeName="width" values="0;0;{width:.0f};{width:.0f};0" '
            f'keyTimes="0;{kt(start)};{kt(end)};{kt(total - 0.4)};1" dur="{total:.1f}s" '
            f'repeatCount="indefinite"/></rect></clipPath>'
        )

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" '
        f'role="img" aria-label="Recent GitHub activity">',
        "<defs>",
    ]
    body = []

    # command line
    y = top
    cmd_w = (len(cmd) + 2) * char_w
    parts.append(reveal("c0", PAD + 4 * char_w, y, cmd_w, t_cmd_start, t_cmd_end))
    body.append(
        f'<text x="{PAD}" y="{y}" class="m"><tspan fill="{GREEN}">➜</tspan>'
        f'<tspan fill="{BLUE}"> ~ </tspan></text>'
        f'<text x="{PAD + 4 * char_w}" y="{y}" class="m" fill="{TEXT}" clip-path="url(#c0)">{escape(cmd)}</text>'
    )

    # activity lines
    for i, ((sym, col, text, when), (s, e)) in enumerate(zip(lines, steps), start=1):
        y = top + LH * (i + 0.4)
        width = W - 2 * PAD
        parts.append(reveal(f"c{i}", PAD, y, width, s, e))
        body.append(
            f'<g clip-path="url(#c{i})">'
            f'<text x="{PAD + 8}" y="{y}" class="m" fill="{col}">{escape(sym)}</text>'
            f'<text x="{PAD + 40}" y="{y}" class="m" fill="{TEXT}">{escape(text)}</text>'
            f'<text x="{W - PAD}" y="{y}" class="m" fill="{MUTED}" text-anchor="end">{escape(when)}</text>'
            f"</g>"
        )

    # summary
    y = top + LH * (len(lines) + 1.6)
    parts.append(reveal("cs", PAD, y, W - 2 * PAD, *t_sum))
    body.append(
        f'<g clip-path="url(#cs)">'
        f'<line x1="{PAD}" y1="{y - 30}" x2="{W - PAD}" y2="{y - 30}" stroke="{BORDER}" stroke-dasharray="4 6"/>'
        f'<text x="{PAD + 8}" y="{y}" class="m" fill="{YELLOW}">★ {escape(summary)}</text></g>'
    )

    # blinking cursor
    yc = top + LH * (len(lines) + 2.6)
    body.append(
        f'<text x="{PAD}" y="{yc}" class="m"><tspan fill="{GREEN}">➜</tspan><tspan fill="{BLUE}"> ~ </tspan></text>'
        f'<rect x="{PAD + 4 * char_w}" y="{yc - 16}" width="10" height="20" fill="{YELLOW}">'
        f'<animate attributeName="opacity" values="1;1;0;0" keyTimes="0;0.5;0.5;1" dur="1s" repeatCount="indefinite"/>'
        f"</rect>"
    )

    parts.append("</defs>")
    parts.append(
        "<style>.m{font-family:Consolas,'SF Mono','Cascadia Mono','Courier New',monospace;font-size:16px}"
        ".t{font-family:-apple-system,'Segoe UI',Helvetica,Arial,sans-serif;font-size:13px}</style>"
    )
    parts.append(f'<rect x="0.5" y="0.5" width="{W - 1}" height="{H - 1}" rx="14" fill="{BG}" stroke="{BORDER}"/>')
    parts.append(f'<path d="M0.5 14.5a14 14 0 0 1 14-14h{W - 29}a14 14 0 0 1 14 14v30h-{W - 1}z" fill="{BAR}"/>')
    parts.append(f'<line x1="0.5" y1="44.5" x2="{W - 0.5}" y2="44.5" stroke="{BORDER}"/>')
    for i, c in enumerate(("#ff5f57", "#febc2e", "#28c840")):
        parts.append(f'<circle cx="{26 + i * 22}" cy="22.5" r="6" fill="{c}"/>')
    parts.append(
        f'<text x="{W / 2}" y="27" class="t" fill="{MUTED}" text-anchor="middle">sandhya@github: ~/activity</text>'
    )
    parts.extend(body)
    parts.append("</svg>")
    return "\n".join(parts)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--user", default=os.environ.get("GITHUB_USER", "Sandhya192005"))
    ap.add_argument("--out", default="assets/activity-terminal.svg")
    args = ap.parse_args()
    token = os.environ.get("GITHUB_TOKEN")
    now = dt.datetime.now(dt.timezone.utc)

    events = _get(f"{API}/users/{args.user}/events/public?per_page=100", token)
    lines = build_lines(events, args.user, now)
    if not lines:
        lines = [("●", MUTED, "no recent public activity", "")]

    user = _get(f"{API}/users/{args.user}", token)
    total = contributions_last_year(args.user, token)
    bits = []
    if total is not None:
        bits.append(f"{total} contributions in the last year")
    bits.append(f"{user.get('public_repos', 0)} public repositories")
    bits.append(f"updated {now:%d %b %Y}")
    summary = "  ·  ".join(bits)

    svg = render(lines, summary)
    os.makedirs(os.path.dirname(args.out) or ".", exist_ok=True)
    with open(args.out, "w", encoding="utf-8", newline="\n") as f:
        f.write(svg)
    print(f"wrote {args.out} ({len(lines)} lines)")


if __name__ == "__main__":
    main()
