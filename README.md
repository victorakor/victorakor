<h1 align="center">Victor Akor Ukpahiu-ojo</h1>

<p align="center">
  <strong>Software developer — Go · Python · Computer Vision</strong>
</p>

<p align="center">
  I build systems people actually run on: a school's entire administration,<br>
  a competitive coding arena, real-time video pipelines.
</p>

<p align="center">
  <a href="mailto:victorakor04@gmail.com"><img alt="Email" src="https://img.shields.io/badge/Email-victorakor04%40gmail.com-D14836?style=flat-square&logo=gmail&logoColor=white"></a>
  <a href="https://text-analyzer-ecru.vercel.app"><img alt="Live demo" src="https://img.shields.io/badge/Live_demo-TextFlow-000000?style=flat-square&logo=vercel&logoColor=white"></a>
  <a href="https://github.com/victorakor?tab=repositories"><img alt="Repositories" src="https://img.shields.io/badge/All_projects-181717?style=flat-square&logo=github&logoColor=white"></a>
</p>

---

## About

I write backends in **Go** and **Python**, and I like problems where correctness
matters more than novelty — exam integrity, financial totals, role-based access,
frame-by-frame detection latency.

Most of what I build is full-stack out of necessity rather than preference: if a
school needs report cards, someone has to write both the grading engine and the
page it prints from. I tend to reach for the standard library first and add
dependencies only when they earn their place.

**Currently open to backend and ML engineering roles.**

---

## Featured work

### 🏆 [Hackerthon](https://github.com/victorakor/hackerthon) — competitive coding platform
A full online judge and contest arena. Users solve problems in an in-browser
CodeMirror editor across **9 languages**, run code against test cases before
submitting, and compete three different ways: **1v1 challenges**, **timed
tournaments**, and **team-based clan raids** with a live scoreboard.

Engineering worth calling out:
- **Anti-cheat** — tab-switch and copy/paste detection during active contests
- **Sandboxed code runner** with per-test-case pass/fail reporting
- **AI hints** via Groq, rate-limited per user per question
- Go standard library + SQLite; **zero frontend framework**

`Go` · `SQLite` · `Vanilla JS` · `CodeMirror` · `Docker` · `Render`

---

### 🎓 [LEAPS](https://github.com/victorakor/leaps-management-system) — school operating system
A digital operating system replacing the manual processes of a real secondary
school. Nine modules: admissions, academics, CBT examinations, finance,
reporting, staff, timetabling, media, and audit.

Engineering worth calling out:
- **JWT auth with role-based access control** across every route
- **Full audit logging** — every state change is attributable, for compliance
- **Timetable conflict detection** for classes and exams
- **PDF report card generation** with school branding

`Go` · `PostgreSQL` · `JWT` · `RBAC`

---

### 👁️ [Mall Surveillance System](https://github.com/victorakor/mall-surveillance-system) — real-time computer vision
Flask application streaming live detection to a single-page admin console.
**YOLOv8** handles person detection, **dlib**'s ResNet model handles face
recognition against a known-faces encoding set.

Engineering worth calling out:
- Four simultaneous canvas streams in the operator dashboard
- **Firebase Auth + Realtime Database** for roles, cameras, alerts and settings
- Separate **admin** and **personnel** permission tiers
- Alert verify/dismiss workflow with an activity log

`Python` · `Flask` · `YOLOv8` · `dlib` · `OpenCV` · `Firebase`

---

### More projects

| Project | What it is | Stack |
| --- | --- | --- |
| [**Eye Disease Detection**](https://github.com/victorakor/Eye-disease-detection) | Keras CNN classifying eye disease from retinal images, served via Flask | `Python` `Keras` `Flask` |
| [**Expense Tracker**](https://github.com/victorakor/expense-tracker) | CLI tracker with exact `Decimal` arithmetic and atomic writes. **234 tests, 98% coverage, `mypy --strict`**, CI across 4 Python versions × 3 OSes | `Python` `pytest` `mypy` |
| [**SHIFT**](https://github.com/victorakor/Shift-website) | Multiplayer "steal and guess" game — **stdlib-only** Go server, no external modules | `Go` `Vanilla JS` |
| [**TextFlow**](https://github.com/victorakor/textAnalyzer) · [*live*](https://text-analyzer-ecru.vercel.app) | Markup-driven text formatter: split-pane editor with live syntax highlighting over a Go rule engine | `JS` `CSS` `Go` |

---

## Tech

**Languages**  
![Go](https://img.shields.io/badge/Go-00ADD8?style=flat-square&logo=go&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=css3&logoColor=white)

**Backend & data**  
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=flat-square&logo=postgresql&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=flat-square&logo=sqlite&logoColor=white)
![Firebase](https://img.shields.io/badge/Firebase-FFCA28?style=flat-square&logo=firebase&logoColor=black)
![Flask](https://img.shields.io/badge/Flask-000000?style=flat-square&logo=flask&logoColor=white)

**ML & vision**  
![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?style=flat-square&logo=tensorflow&logoColor=white)
![Keras](https://img.shields.io/badge/Keras-D00000?style=flat-square&logo=keras&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=flat-square&logo=opencv&logoColor=white)
![YOLOv8](https://img.shields.io/badge/YOLOv8-111F68?style=flat-square&logo=yolo&logoColor=white)

**Tooling**  
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=flat-square&logo=githubactions&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git&logoColor=white)
![Vercel](https://img.shields.io/badge/Vercel-000000?style=flat-square&logo=vercel&logoColor=white)
![pytest](https://img.shields.io/badge/pytest-0A9EDC?style=flat-square&logo=pytest&logoColor=white)

---

<div align="center">

<img alt="Most used languages" src="https://github-readme-stats.vercel.app/api/top-langs/?username=victorakor&layout=compact&langs_count=8&hide_border=true&title_color=00ADD8&text_color=808080&bg_color=00000000" />

</div>

---

<p align="center">
  <sub>Reach me at <a href="mailto:victorakor04@gmail.com">victorakor04@gmail.com</a></sub>
</p>
