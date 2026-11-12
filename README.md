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

- 🔧 Interested in **backend and full-stack development**
- 🌐 Building **REST APIs** and practical software applications
- 🗄️ Working with **databases** and application logic: schemas, migrations, authentication
- 🧩 Continuously improving my **programming and problem-solving** skills
- 🎨 Exploring **frontend technologies** to build complete, end-to-end applications

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
    <td><img src="https://skillicons.dev/icons?i=aws,docker,postman,git,github,vscode&theme=dark" height="40" alt="AWS, Docker, Postman, Git, GitHub, VS Code" /></td>
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

## 🎯 What I'm Focusing On

| | |
|---|---|
| 🔌 | Backend engineering and REST APIs |
| 🏗️ | Database integration and application architecture |
| ⚛️ | React and TypeScript for frontend development |
| ✨ | Writing clean, maintainable code |
| 🧠 | Improving problem-solving and software development skills |

---

## 📊 GitHub Activity

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=Sandhya192005&show_icons=true&hide_border=true&bg_color=0d1117&title_color=58a6ff&icon_color=58a6ff&text_color=c9d1d9" height="165" alt="GitHub stats" />
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=Sandhya192005&layout=compact&hide_border=true&bg_color=0d1117&title_color=58a6ff&text_color=c9d1d9" height="165" alt="Most used languages" />
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
