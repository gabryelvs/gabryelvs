# Hi, I'm Gabryel 👋

Computer Science student (final year, University of Greenwich) and aspiring **backend software engineer** based in **London**. I build production-shaped APIs in **Python / FastAPI**, focused on fintech problems — payments, ledgers, and resilient services.

🔭 Currently building a backend portfolio of small, well-engineered services — each tested, run in CI, containerised, and deployed live with interactive docs you can try.

🌐 **See it all in one place → [portfolio-gabryelverissimo.vercel.app](https://portfolio-gabryelverissimo.vercel.app/)**

---

### 🚀 Featured projects

**[PayLedger](https://github.com/gabryelvs/payledger)** — Double-entry payments & ledger API · [▶ Live demo](https://payledger-gv.fly.dev/docs)
A payments backend built the way real banks work: money stored as integer minor units (no float errors), an append-only **double-entry ledger**, **race-safe transfers** via database row locking (proven under parallel load), and **idempotent** writes to prevent double-charges.
`FastAPI` · `PostgreSQL` · `SQLAlchemy` · `Alembic` · `Docker` · `GitHub Actions`

**[FX-Service](https://github.com/gabryelvs/fx-service)** — Async currency-exchange API · [▶ Live demo](https://fx-service-gv.fly.dev/docs)
Serves live exchange rates and conversions. Caches ECB rates in Redis, refreshes them on a background schedule, and **keeps serving last-known rates when the upstream provider is down** (stale fallback).
`FastAPI` · `httpx (async)` · `Redis` · `Docker` · `GitHub Actions`

**[Webhook-Dispatcher](https://github.com/gabryelvs/webhook-dispatcher)** — Reliable webhook delivery
Delivers webhooks via a **Redis queue + a separate worker process**, with HMAC-SHA256 signing, **exponential backoff**, a **dead-letter queue**, and manual replay. At-least-once delivery with de-duplication.
`FastAPI` · `Redis` · `Docker` · `GitHub Actions`

**[OWASP Security Lab](https://github.com/gabryelvs/owasp-security-lab)** — Break it & fix it 🔐
An intentionally-vulnerable FastAPI app demonstrating **six OWASP Top 10** issues (SQL injection, broken access control, SSRF, JWT auth flaws, and more). Each vuln ships with a **working exploit, a hardened fix, and tests proving both** — defensive, secure-coding focused.
`FastAPI` · `pytest` · `Docker` · `CodeQL` · `GitHub Actions`

---

### 🛠️ Tech I work with

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat&logo=fastapi&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=flat&logo=postgresql&logoColor=white)
![Redis](https://img.shields.io/badge/Redis-DC382D?style=flat&logo=redis&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-D71F00?style=flat&logo=sqlalchemy&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=flat&logo=githubactions&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=flat&logo=git&logoColor=white)

Also: C#, SQL, JavaScript · REST API design · test-driven development · cloud deployment (Fly.io)

---

### 📫 Connect

[![Portfolio](https://img.shields.io/badge/Portfolio-6366F1?style=flat&logo=vercel&logoColor=white)](https://portfolio-gabryelverissimo.vercel.app/)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/gabryel-ver%C3%ADssimo-b1b931261)
📧 gabryelverissimo12@gmail.com
