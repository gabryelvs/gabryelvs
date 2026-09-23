# Hi, I'm Gabryel 👋

**Software engineer** based in **London**. I build production-shaped APIs in **Python / FastAPI** and **Java / Spring Boot**, focused on fintech problems — payments, ledgers, and resilient services — and ship fullstack tools with **React / TypeScript** when the API needs a face.

🎓 BSc Computer Science, University of Greenwich, graduating July 2027 · open to graduate and junior software engineer roles in London.

🔭 Currently building a backend portfolio of small, well-engineered services — each tested, run in CI, containerised, and deployed live with interactive docs you can try.

🌐 **See it all in one place → [gabryelverissimo.dev](https://gabryelverissimo.dev)**

---

### 🚀 Featured projects

**[PayLedger](https://github.com/gabryelvs/payledger)** — Double-entry payments & ledger API · [▶ Live demo](https://payledger-gv.vercel.app/docs)
A payments backend built the way real banks work: money stored as integer minor units (no float errors), an append-only **double-entry ledger**, **race-safe transfers** via database row locking (proven under parallel load), and **atomically idempotent** writes — the idempotency key is claimed inside the same transaction as the transfer, so concurrent retries can't double-charge. Every wallet, statement and transaction is **ownership-checked**: only the owner can access it, and someone else's wallet 404s like a missing one.
`FastAPI` · `PostgreSQL` · `SQLAlchemy` · `Alembic` · `Docker` · `GitHub Actions`

**[FX-Service](https://github.com/gabryelvs/fx-service)** — Async currency-exchange API · [▶ Live demo](https://fx-service-gv.fly.dev/docs)
Serves live exchange rates and conversions. Caches ECB rates in Redis, refreshes them on a background schedule, and **keeps serving last-known rates when the upstream provider is down** (stale fallback).
`FastAPI` · `httpx (async)` · `Redis` · `Docker` · `GitHub Actions`

**[Webhook-Dispatcher](https://github.com/gabryelvs/webhook-dispatcher)** — Reliable webhook delivery
Delivers webhooks via a **Redis queue + a separate worker process**, with HMAC-SHA256 signing, **exponential backoff**, a **dead-letter queue**, and manual replay. At-least-once delivery with de-duplication.
`FastAPI` · `Redis` · `Docker` · `GitHub Actions`

**[Taskboard API](https://github.com/gabryelvs/taskboard-api)** — Trello-like task manager API · [▶ Live demo](https://taskboard-api-h3yu.onrender.com/swagger-ui.html)
A task board backend in Java/Spring Boot: **JWT auth with refresh-token rotation** — reusing a rotated refresh token **revokes every session for that user** — role-based project membership with **404-no-leak authorization**, and **transactional drag-and-drop card ordering** with pessimistic column locking, proven by 62 Testcontainers integration tests.
`Java` · `Spring Boot` · `PostgreSQL` · `Docker` · `GitHub Actions`

**[Webhook Inspector](https://github.com/gabryelvs/webhook-inspector)** — Fullstack webhook debugging tool · [▶ Live demo](https://webhook-inspector-gv.vercel.app)
Create a disposable URL, point any webhook at it, and watch requests arrive live — headers, pretty-printed body, and query params. Hardened for a public endpoint: **bodies streamed and capped at 1 MB**, **per-client rate limiting keyed on the real client IP behind the proxy** (no trusting `X-Forwarded-For`), and a capture route that **always returns 200 so a database fault never breaks the sender's webhook**. The debugging counterpart to Webhook-Dispatcher.
`FastAPI` · `PostgreSQL` · `React` · `TypeScript` · `Tailwind` · `Docker`

**[SECTOR—9](https://github.com/gabryelvs/store-demo)** — Animated demo storefront · [▶ Live demo](https://store-demo-gv.fly.dev)
A storefront demo built as a **client-facing sales asset** for freelance work — the thing a prospect clicks through instead of reading a proposal. The catalogue sits behind a **single data seam**, so a real backend replaces the mock data without touching a page. The cart is a **pure reducer** with totals derived in integer pence and **storage rehydration that validates what it reads**, so a stale bag can never render a wrong total. Quick-view, cart and mobile-nav overlays each **trap focus, mark the background inert for screen readers, and stand down under `prefers-reduced-motion`**. 26 statically prerendered routes, **Lighthouse 99–100** with zero layout shift.
`Next.js 16` · `React 19` · `TypeScript` · `Tailwind 4` · `GSAP` · `Vitest` · `Docker`

**[OWASP Security Lab](https://github.com/gabryelvs/owasp-security-lab)** — Break it & fix it 🔐
An intentionally-vulnerable FastAPI app demonstrating **six OWASP Top 10** issues (SQL injection, broken access control, SSRF, JWT auth flaws, and more). Each vuln ships with a **working exploit, a hardened fix, and tests proving both** — defensive, secure-coding focused.
`FastAPI` · `pytest` · `Docker` · `CodeQL` · `GitHub Actions`

---

### 🛠️ Tech I work with

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat&logo=fastapi&logoColor=white)
![Java](https://img.shields.io/badge/Java-007396?style=flat&logo=openjdk&logoColor=white)
![Spring Boot](https://img.shields.io/badge/Spring_Boot-6DB33F?style=flat&logo=springboot&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=flat&logo=postgresql&logoColor=white)
![Redis](https://img.shields.io/badge/Redis-DC382D?style=flat&logo=redis&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-D71F00?style=flat&logo=sqlalchemy&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=flat&logo=githubactions&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=flat&logo=git&logoColor=white)

Also: C#, SQL, JavaScript · React · Next.js · TypeScript · Tailwind CSS · GSAP · Spring Security · Testcontainers · Vitest · REST API design · test-driven development · web accessibility · cloud deployment (Vercel, Render, Fly.io) · AI-assisted development (Claude)

---

### 📫 Connect

[![Portfolio](https://img.shields.io/badge/Portfolio-6366F1?style=flat&logo=vercel&logoColor=white)](https://gabryelverissimo.dev)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/gabryel-ver%C3%ADssimo-b1b931261)
📧 [hello@gabryelverissimo.dev](mailto:hello@gabryelverissimo.dev)
