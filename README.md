<p align="center">
  <img src="./assets/banner.svg" alt="Sandhya R. — Better Code, Bigger Dreams" width="100%" />
</p>

<h1 align="center">Hi, I'm Sandhya R. 👋</h1>

<p align="center">
  <b>Aspiring Software Developer | Backend &amp; Full-Stack Development</b>
</p>

<p align="center">
  I'm a software developer interested in building practical applications, developing reliable backend APIs,
  and creating user-friendly full-stack solutions. I enjoy problem-solving, exploring technologies,
  and improving my development skills through real-world projects.
</p>

<p align="center">
  <a href="https://github.com/Sandhya192005"><img src="https://img.shields.io/badge/GitHub-Sandhya192005-181717?style=flat&logo=github&logoColor=white" alt="GitHub" /></a>
  <a href="#-connect-with-me"><img src="https://img.shields.io/badge/Open_to-Internships_%26_Entry--Level_Roles-1f6feb?style=flat" alt="Open to internships and entry-level roles" /></a>
</p>

---

## 🧑‍💻 About Me

I'm a **backend-focused full-stack developer** who builds complete, production-style applications — from database
design and REST APIs to the frontend and deployment. Lately my focus has been on **applying AI and LLMs to real
problems**: AI assistants with tool calling, vision-based analysis, and retrieval-augmented generation (RAG).

- 🏗️ **Backend & APIs** — Design REST APIs with **FastAPI** and **Django REST Framework**, with JWT authentication,
  role-based access, rate limiting and versioned schema migrations (Alembic, Django migrations)
- 🤖 **AI & LLM applications** — Built an OpenAI assistant that calls the app's own tools, a food-photo nutrition
  analyzer using vision models, a RAG pipeline with embeddings and **pgvector**, and local LLMs running on CPU
- 🗄️ **Data & infrastructure** — Work with **PostgreSQL / PostGIS**, **Redis**, **Elasticsearch** and **Celery**
  background jobs; containerize full stacks with **Docker Compose**; store data on **AWS** (S3, RDS)
- ⚛️ **Frontend** — Build responsive interfaces with **React, Next.js, TypeScript** and Tailwind CSS, including
  maps, live WebSocket notifications and 3D views with Three.js
- ✅ **Quality & reliability** — Write tests with **pytest** and **Playwright** end-to-end, set up CI with GitHub
  Actions, and design offline-first, idempotent data sync
- ⚙️ **Automation** — Automate business workflows with **n8n**, combining email, Excel and AI classification

---

## 🛠️ Tech Stack

<table>
  <tr>
    <td width="170"><b>Languages</b></td>
    <td><img src="https://skillicons.dev/icons?i=python,java,js,ts&theme=dark" height="40" alt="Python, Java, JavaScript, TypeScript" /> <img src="./assets/sql.svg" height="40" alt="SQL" /></td>
  </tr>
  <tr>
    <td><b>Backend</b></td>
    <td><img src="https://skillicons.dev/icons?i=fastapi,django,nodejs,express&theme=dark" height="40" alt="FastAPI, Django, Node.js, Express.js" /></td>
  </tr>
  <tr>
    <td><b>Frontend</b></td>
    <td><img src="https://skillicons.dev/icons?i=html,css,react,nextjs,tailwind&theme=dark" height="40" alt="HTML5, CSS3, React, Next.js, Tailwind CSS" /></td>
  </tr>
  <tr>
    <td><b>Databases</b></td>
    <td><img src="https://skillicons.dev/icons?i=postgres,mongodb,sqlite,redis,elasticsearch&theme=dark" height="40" alt="PostgreSQL, MongoDB, SQLite, Redis, Elasticsearch" /></td>
  </tr>
  <tr>
    <td><b>AI &amp; LLMs</b></td>
    <td>
      <img src="https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white" height="28" alt="LangChain" />
      <img src="https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=openai&logoColor=white" height="28" alt="OpenAI" />
      <img src="https://img.shields.io/badge/Hugging_Face-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black" height="28" alt="Hugging Face" />
      <img src="https://img.shields.io/badge/pgvector-336791?style=for-the-badge&logo=postgresql&logoColor=white" height="28" alt="pgvector" />
      <img src="https://img.shields.io/badge/Ollama-000000?style=for-the-badge&logo=ollama&logoColor=white" height="28" alt="Ollama" />
      <img src="https://img.shields.io/badge/Embeddings-0A7E8C?style=for-the-badge" height="28" alt="Embeddings" />
    </td>
  </tr>
  <tr>
    <td><b>Tools</b></td>
    <td><img src="https://skillicons.dev/icons?i=aws,docker,postman,git,github,vscode&theme=dark" height="40" alt="AWS, Docker, Postman, Git, GitHub, VS Code" /> <img src="https://img.shields.io/badge/Swagger_UI-85EA2D?style=for-the-badge&logo=swagger&logoColor=black" height="28" alt="Swagger UI" /> <img src="https://img.shields.io/badge/Canva-00C4CC?style=for-the-badge&logo=canva&logoColor=white" height="28" alt="Canva" /></td>
  </tr>
</table>

---

## 🚀 Featured Projects

<table>
  <tr>
    <td>
      <h3>🏥 MediConnect</h3>
      <p>
        A hospital appointment booking platform. Patients find doctors and nearby hospitals, book slots and get reminders,
        with an AI assistant that helps search and suggests bookings — but never books on its own.
      </p>
      <ul>
        <li>Django REST API + Next.js frontend, fully Dockerized with PostgreSQL/PostGIS, Redis and Elasticsearch</li>
        <li>Fuzzy doctor search with synonyms and autocomplete; nearby-hospital map using PostGIS and OpenStreetMap</li>
        <li>Celery jobs for email reminders, live notifications over WebSockets (Django Channels)</li>
        <li>OpenAI assistant with tool calling and safety rules; Playwright scraper for hospital websites</li>
        <li>Tested with pytest and Playwright end-to-end tests</li>
      </ul>
      <p>
        <img src="https://skillicons.dev/icons?i=python,django,nextjs,postgres,redis,elasticsearch,docker&theme=dark" height="32" alt="Python, Django, Next.js, PostgreSQL, Redis, Elasticsearch, Docker" />
      </p>
      <p>
        <a href="https://github.com/Sandhya192005/MediConnect"><b>📂 Repository</b></a> &nbsp;·&nbsp; <i>Demo: not deployed yet</i>
      </p>
    </td>
  </tr>
  <tr>
    <td>
      <h3>🥗 AI Food Agent</h3>
      <p>
        A personal nutrition assistant. Upload a photo of a meal and AI vision estimates its calories, protein and fat.
        Recommendations are personalized to your profile, diet preference, health conditions and budget.
      </p>
      <ul>
        <li>JWT authentication with automatic BMI / BMR / daily-calorie and water-goal calculation</li>
        <li>REST API for meal, water-intake and office-menu logging</li>
        <li>PostgreSQL / SQLite via SQLAlchemy + Alembic, tested with pytest, Dockerized</li>
      </ul>
      <p>
        <img src="https://skillicons.dev/icons?i=python,fastapi,postgres,react,ts,docker&theme=dark" height="32" alt="Python, FastAPI, PostgreSQL, React, TypeScript, Docker" />
      </p>
      <p>
        <a href="https://github.com/Sandhya192005/Food-Agent"><b>📂 Repository</b></a> &nbsp;·&nbsp; <i>Demo: not deployed yet</i>
      </p>
    </td>
  </tr>
  <tr>
    <td>
      <h3>💚 AI Health Agent <sub><i>(team project)</i></sub></h3>
      <p>
        An employee wellbeing system with three parts: a background desktop agent, a FastAPI server, and a React dashboard
        that shows AI-written wellbeing reminders.
      </p>
      <ul>
        <li>Offline-first desktop agent that buffers activity locally and syncs without losing or duplicating events</li>
        <li>LLM-generated break / idle / distraction reminders, spoken aloud by an on-screen assistant</li>
        <li>Role-based dashboard: admins see the organization, employees see only their own day</li>
      </ul>
      <p>
        <img src="https://skillicons.dev/icons?i=python,fastapi,postgres,sqlite,react,ts&theme=dark" height="32" alt="Python, FastAPI, PostgreSQL, SQLite, React, TypeScript" />
      </p>
      <p>
        <a href="https://github.com/Suba-kumar09/health-agent"><b>📂 Repository</b></a> &nbsp;·&nbsp; <i>Demo: not deployed yet</i>
      </p>
    </td>
  </tr>
</table>

---

## 🗂️ Other Projects

| Project | Description | Tech |
|---|---|---|
| [🏠 Home Layout](https://github.com/Sandhya192005/home-layout) | Generates dimensioned 2D/3D floor plans from plot size, rooms, budget and Vastu, with cost estimates | FastAPI · PostgreSQL · React · Three.js |
| [📄 RAG-LangChain](https://github.com/Sandhya192005/RAG-LangChain) | "Chat with my resume" — a RAG pipeline built step by step: load, chunk, embed, retrieve, generate | Python · LangChain · OpenAI · pgvector |
| [📦 Cargo Email Automation](https://github.com/Sandhya192005/Cargo-Email-Automation) | Reads shipment emails from Outlook, uses AI to classify them and extract details, logs them to Excel and sends customer reports after human approval | n8n · Claude AI · Outlook · Excel |
| [📚 Book Swapper](https://github.com/Sandhya192005/book-swapper) | List, discover and exchange books (sell, swap, borrow or donate) with requests, ratings and location info | React · TypeScript · Tailwind |
| [💰 Budget Tracker](https://github.com/Sandhya192005/budget-tracker) | Personal finance dashboard with transactions, budgets and spending charts | React · TypeScript · Tailwind |
| [🤖 Local LLM Chat](https://github.com/Sandhya192005/HuggingFace) | Terminal chatbot running Qwen2.5-3B fully on CPU — no GPU or API key | Python · llama.cpp · Hugging Face |
| [⭐ Product Review System](https://github.com/Sandhya192005/product-review-system) | Login-gated app to add products with star ratings and reviews, with live search | HTML · CSS · JavaScript |
| [🩸 Donor List Management](https://github.com/Sandhya192005/donor-list-management) | Searchable donor list with sign-up/login and add, edit and delete records | HTML · CSS · JavaScript |
| [🎓 CGPA Calculator](https://github.com/Sandhya192005/CGPA-calculator) | Calculates semester GPA and overall credit-weighted CGPA for an 8-semester curriculum | HTML · CSS · JavaScript |

---

## 💼 Experience &amp; Practical Work

### Full Stack Developer Intern | Finstein Advizory
- Worked on health and food-related application projects.
- Gained hands-on experience with **Python, FastAPI, and PostgreSQL**.
- Explored REST API development and database integration.
- Gained exposure to **Databricks** and data-related workflows.

### MERN Stack Developer Intern | Altruisty
- Gained practical experience in web application development.
- Worked with the **MERN stack**.
- Explored frontend and backend integration in web applications.

---

## 🎯 Current Focus

| Area | What I'm working on |
|---|---|
| 🤖 **Applied AI & LLM systems** | Building reliable LLM features — RAG with embeddings and vector search, tool-calling assistants, and guardrails for safe, grounded answers |
| 🏗️ **Scalable backend architecture** | Designing clean, well-tested REST APIs with background jobs, caching, search and real-time updates |
| ☁️ **Cloud & DevOps** | Containerized deployments with Docker, AWS services, and CI/CD pipelines with GitHub Actions |
| ✅ **Testing & code quality** | Unit, integration and end-to-end testing, with maintainable, well-documented code |
| 🚀 **Shipping complete products** | Taking projects from idea to deployed demo, with clear documentation and a polished user experience |

---|---|
| 🔌 | Backend engineering and REST APIs |
| 🏗️ | Database integration and application architecture |
| ⚛️ | React and TypeScript for frontend development |
| ✨ | Writing clean, maintainable code |
| 🧠 | Improving problem-solving and software development skills |

---

## 📊 GitHub Activity

<p align="center">
  <img src="https://streak-stats.demolab.com/?user=Sandhya192005&hide_border=false&border_radius=8&background=0B1F3A&border=FACC15&stroke=334155&ring=F97316&fire=F97316&currStreakNum=F97316&sideNums=FACC15&currStreakLabel=3B82F6&sideLabels=3B82F6&dates=E2E8F0" alt="GitHub contribution streak" />
</p>

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Sandhya192005/Sandhya192005/main/profile-3d-contrib/profile-night-rainbow.svg" />
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/Sandhya192005/Sandhya192005/main/profile-3d-contrib/profile-green-animate.svg" />
    <img src="https://raw.githubusercontent.com/Sandhya192005/Sandhya192005/main/profile-3d-contrib/profile-night-rainbow.svg" alt="3D contribution graph" width="100%" />
  </picture>
</p>

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Sandhya192005/Sandhya192005/output/pacman-contribution-graph-dark.svg" />
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/Sandhya192005/Sandhya192005/output/pacman-contribution-graph.svg" />
    <img src="https://raw.githubusercontent.com/Sandhya192005/Sandhya192005/output/pacman-contribution-graph-dark.svg" alt="Pac-Man contribution graph" width="100%" />
  </picture>
</p>

<p align="center">
  <img src="https://komarev.com/ghpvc/?username=Sandhya192005&label=Profile%20views&color=555555&style=flat" alt="Profile views" />
</p>

---

## 📫 Connect With Me

<p>
  <a href="https://github.com/Sandhya192005"><img src="https://img.shields.io/badge/GitHub-Sandhya192005-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub" /></a>
  <a href="https://www.linkedin.com/in/sandhya192005"><img src="https://img.shields.io/badge/LinkedIn-sandhya192005-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn" /></a>
  <a href="mailto:sandhyasubha192005@gmail.com"><img src="https://img.shields.io/badge/Email-sandhyasubha192005%40gmail.com-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="Email" /></a>
</p>

---

<p align="center">
  <img src="./assets/footer.svg" alt="Keep building, keep growing." width="100%" />
</p>
