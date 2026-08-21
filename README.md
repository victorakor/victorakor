<!-- ════════════════════════ ANIMATED HEADER ════════════════════════ -->
<div align="center">

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=0:00ADD8,50:2E8BC0,100:3776AB&height=200&section=header&text=Victor%20Akor&fontSize=66&fontColor=ffffff&fontAlignY=33&animation=fadeIn&desc=Backend%20%C2%B7%20Machine%20Learning%20%C2%B7%20Computer%20Vision&descAlignY=55&descSize=17" alt="Victor Akor" />

<!-- Cycling typing animation -->
<a href="https://github.com/victorakor?tab=repositories">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=21&duration=3200&pause=800&color=00ADD8&center=true&vCenter=true&width=760&height=44&lines=Go+%26+Python+backends+that+hold+up+under+load;Real-time+computer+vision+%E2%80%94+YOLOv8+%2B+dlib;An+entire+school's+operations%2C+digitised;234+tests%2C+98%25+coverage%2C+mypy+--strict;Correctness+over+novelty" alt="Go and Python backends; real-time computer vision; correctness over novelty" />
</a>

<br>

<a href="mailto:victorakor04@gmail.com"><img src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white" alt="Email" /></a>
<a href="https://text-analyzer-ecru.vercel.app"><img src="https://img.shields.io/badge/Live_Demo-000000?style=for-the-badge&logo=vercel&logoColor=white" alt="Live demo" /></a>
<a href="https://github.com/victorakor?tab=repositories"><img src="https://img.shields.io/badge/Projects-181717?style=for-the-badge&logo=github&logoColor=white" alt="Projects" /></a>
<img src="https://komarev.com/ghpvc/?username=victorakor&style=for-the-badge&color=00ADD8&label=VISITORS" alt="Profile views" />

<br><br>

<img src="https://img.shields.io/badge/Open_to_backend_%26_ML_engineering_roles-00ADD8?style=flat-square&labelColor=0d1117" alt="Open to backend and ML engineering roles" />

</div>

<img width="100%" src="https://capsule-render.vercel.app/api?type=rect&color=0:00ADD8,100:3776AB&height=3&section=header" alt="" />

<!-- ════════════════════════ ABOUT ════════════════════════ -->
## 🧭 &nbsp;About

<img align="right" width="410" src="https://raw.githubusercontent.com/victorakor/victorakor/main/assets/langs.svg" alt="Language distribution across public repositories" />

I write backends in **Go** and **Python**, and I gravitate to problems where
**correctness matters more than novelty** — exam integrity, financial totals,
role-based access, frame-by-frame detection latency.

Most of what I build ends up full-stack out of necessity rather than preference:
if a school needs report cards, someone has to write both the grading engine
*and* the page it prints from.

I reach for the standard library first and add dependencies only when they earn
their place. One of my Go servers ships with **zero external modules**, and my
Python CLI has **no runtime dependencies at all**.

```go
type Engineer struct {
    Focus     []string // backend systems, computer vision
    Languages []string // Go, Python, JavaScript
    Believes  string   // "if it isn't tested, it isn't done"
}
```

<br clear="both">

<div align="center">
  <img width="410" src="https://raw.githubusercontent.com/victorakor/victorakor/main/assets/stats.svg" alt="10 public repositories, 2.0 MB of public code, 9 languages, Go primary" />
</div>

<img width="100%" src="https://capsule-render.vercel.app/api?type=rect&color=0:00ADD8,100:3776AB&height=3&section=header" alt="" />

<!-- ════════════════════════ FEATURED WORK ════════════════════════ -->
## 🚀 &nbsp;Featured Work

> <sub><b>Click any project to expand the engineering detail.</b></sub>

<details open>
<summary><b>🏆 &nbsp;Hackerthon</b> — <i>competitive coding platform</i> &nbsp; <code>Go</code> <code>SQLite</code> <code>Vanilla JS</code></summary>

<br>

A full **online judge and contest arena**. Users solve problems in an in-browser
CodeMirror editor across **9 languages**, run code against test cases before
submitting, and compete three different ways.

|  | Engineering worth calling out |
|:--:|:--|
| ⚡ | **Anti-cheat** — tab-switch and copy/paste detection during live contests |
| ⚡ | **Sandboxed runner** with per-test-case pass/fail reporting |
| ⚡ | **AI hints** via Groq, rate-limited per user per question |
| ⚡ | **Three contest modes** — 1v1, timed tournaments, team clan raids |
| ⚡ | Live scoreboard polling on a 5-second cadence |
| ⚡ | Go standard library + SQLite, **zero frontend framework** |

<a href="https://github.com/victorakor/hackerthon"><img src="https://img.shields.io/badge/View_repository-00ADD8?style=for-the-badge&logo=github&logoColor=white" alt="View repository" /></a>

</details>

<details>
<summary><b>🎓 &nbsp;LEAPS</b> — <i>school operating system</i> &nbsp; <code>Go</code> <code>PostgreSQL</code> <code>JWT</code></summary>

<br>

A digital operating system replacing the manual processes of a **real secondary
school**. Nine modules: admissions, academics, CBT examinations, finance,
reporting, staff, timetabling, media, and audit.

|  | Engineering worth calling out |
|:--:|:--|
| 🔐 | **JWT auth with role-based access control** on every route |
| 🔐 | **Full audit logging** — every state change attributable, for compliance |
| 🔐 | **Timetable conflict detection** across classes and exams |
| 🔐 | **PDF report cards** generated with school branding |
| 🔐 | Anti-cheat enforcement in the CBT engine |

<a href="https://github.com/victorakor/leaps-management-system"><img src="https://img.shields.io/badge/View_repository-00ADD8?style=for-the-badge&logo=github&logoColor=white" alt="View repository" /></a>

</details>

<details>
<summary><b>👁️ &nbsp;Mall Surveillance System</b> — <i>real-time computer vision</i> &nbsp; <code>Python</code> <code>YOLOv8</code> <code>dlib</code></summary>

<br>

Flask application streaming **live detection** to a single-page operator console.
**YOLOv8** handles person detection; **dlib**'s ResNet model handles face
recognition against a known-faces encoding set.

|  | Engineering worth calling out |
|:--:|:--|
| 🎥 | **Four simultaneous canvas streams** in the operator dashboard |
| 🎥 | **Firebase Auth + Realtime DB** for roles, cameras, alerts, settings |
| 🎥 | Separate **admin** and **personnel** permission tiers |
| 🎥 | Alert verify/dismiss workflow backed by an activity log |
| 🎥 | Containerised, deployed via `render.yaml` |

<a href="https://github.com/victorakor/mall-surveillance-system"><img src="https://img.shields.io/badge/View_repository-00ADD8?style=for-the-badge&logo=github&logoColor=white" alt="View repository" /></a>

</details>

<details>
<summary><b>🩺 &nbsp;Eye Disease Detection</b> — <i>medical image classification</i> &nbsp; <code>Keras</code> <code>EfficientNetV2</code></summary>

<br>

A fine-tuned **EfficientNetV2** classifying retinal fundus images into
**Cataract**, **Diabetic Retinopathy**, **Glaucoma** or **Normal**, served
through Flask with plain-language findings and follow-up recommendations per
diagnosis.

|  | Engineering worth calling out |
|:--:|:--|
| 🧠 | 256×256 RGB input through `efficientnet_v2.preprocess_input` |
| 🧠 | Softmax over 4 classes, arg-max label returned with a confidence score |
| 🧠 | JSON `/predict` endpoint, CORS-enabled for a separately hosted frontend |
| 🧠 | Model path resolved relative to the module, so it runs from any directory |

<a href="https://github.com/victorakor/Eye-disease-detection"><img src="https://img.shields.io/badge/View_repository-00ADD8?style=for-the-badge&logo=github&logoColor=white" alt="View repository" /></a>

</details>

<details>
<summary><b>💰 &nbsp;Expense Tracker</b> — <i>how I actually work</i> &nbsp; <code>Python</code> <code>pytest</code> <code>mypy</code></summary>

<br>

A dependency-free CLI expense tracker, and the repository I would point at to
show engineering practice rather than feature count.

|  | Engineering worth calling out |
|:--:|:--|
| ✅ | **234 tests · 98% branch coverage · `mypy --strict`** |
| ✅ | CI across **Python 3.10–3.13 × Linux/macOS/Windows** — 14 jobs, all green |
| ✅ | Exact `Decimal` arithmetic — no float drift in money |
| ✅ | **Atomic writes** (temp → `fsync` → `os.replace`), with a test that kills the write mid-flight and proves the ledger survives |
| ✅ | Corrupt CSV rows fail loudly with a line number instead of being silently skipped |

<a href="https://github.com/victorakor/expense-tracker"><img src="https://img.shields.io/badge/View_repository-00ADD8?style=for-the-badge&logo=github&logoColor=white" alt="View repository" /></a>
<a href="https://github.com/victorakor/expense-tracker/actions/workflows/ci.yml"><img src="https://github.com/victorakor/expense-tracker/actions/workflows/ci.yml/badge.svg" alt="CI status" /></a>

</details>

<details>
<summary><b>🎮 &nbsp;SHIFT</b> + <b>TextFlow</b> — <i>a game server and a text engine</i> &nbsp; <code>Go</code> <code>JS</code></summary>

<br>

**SHIFT** — a multiplayer "steal and guess" game on a **standard-library-only**
Go server. No external modules at all: the session layer, persistence and
templating are hand-rolled on `net/http`. Ships with a custom "Vault Card"
design system.

**TextFlow** — a markup-driven text formatter. Split-pane editor with live
tag-syntax highlighting over a Go rule engine, plus an offline demo mode that
reimplements the core rules in JS so the UI previews without a backend.

<a href="https://github.com/victorakor/Shift-website"><img src="https://img.shields.io/badge/SHIFT-00ADD8?style=for-the-badge&logo=go&logoColor=white" alt="SHIFT" /></a>
<a href="https://github.com/victorakor/textAnalyzer"><img src="https://img.shields.io/badge/TextFlow-00ADD8?style=for-the-badge&logo=javascript&logoColor=white" alt="TextFlow" /></a>
<a href="https://text-analyzer-ecru.vercel.app"><img src="https://img.shields.io/badge/Try_it_live-000000?style=for-the-badge&logo=vercel&logoColor=white" alt="Try it live" /></a>

</details>

<img width="100%" src="https://capsule-render.vercel.app/api?type=rect&color=0:00ADD8,100:3776AB&height=3&section=header" alt="" />

<!-- ════════════════════════ TECH STACK ════════════════════════ -->
## 🛠️ &nbsp;Tech Stack

<div align="center">

**Languages**

<img src="https://skillicons.dev/icons?i=go,python,js,html,css,bash&theme=dark" alt="Go, Python, JavaScript, HTML, CSS, Bash" />

**Data &amp; infrastructure**

<img src="https://skillicons.dev/icons?i=postgres,sqlite,firebase,flask,docker,vercel&theme=dark" alt="PostgreSQL, SQLite, Firebase, Flask, Docker, Vercel" />

**ML, vision &amp; tooling**

<img src="https://skillicons.dev/icons?i=tensorflow,opencv,sklearn,git,github,githubactions,linux,vscode&theme=dark" alt="TensorFlow, OpenCV, scikit-learn, Git, GitHub, GitHub Actions, Linux, VS Code" />

</div>

<!--
  The contribution heatmap below is generated by .github/workflows/cards.yml and
  is ready to embed. It is commented out because the calendar currently counts
  contributions on only 19 days of the year -- most of this work lives in private
  repositories. Turn on Settings -> Public profile -> "Include private
  contributions on my profile", wait for the next weekly card refresh, then
  uncomment this block.

<img width="100%" src="https://capsule-render.vercel.app/api?type=rect&color=0:00ADD8,100:3776AB&height=3&section=header" alt="" />

## 📊 &nbsp;Activity

<div align="center">
  <img width="98%" src="https://raw.githubusercontent.com/victorakor/victorakor/main/assets/activity.svg" alt="Contribution heatmap" />
</div>
-->

<img width="100%" src="https://capsule-render.vercel.app/api?type=rect&color=0:00ADD8,100:3776AB&height=3&section=header" alt="" />

<!-- ════════════════════════ FOOTER ════════════════════════ -->
<div align="center">

### Let's build something

<a href="mailto:victorakor04@gmail.com"><img src="https://img.shields.io/badge/victorakor04@gmail.com-D14836?style=for-the-badge&logo=gmail&logoColor=white" alt="victorakor04@gmail.com" /></a>

<br><br>

<i>"If it isn't tested, it isn't done."</i>

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=0:3776AB,50:2E8BC0,100:00ADD8&height=130&section=footer" alt="" />

</div>
