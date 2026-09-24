# Q4 2026 Applied AI Engineer Sprint (October - December 2026)

> **Objective:** Transition from script prototypes to an **Internship-Ready Applied AI Engineer** by December 31, 2026, while building an active open-source contribution record for **GSoC 2027**.

---

## 🎯 The Three Hard Targets (By Dec 31, 2026)
1. **Ship 2 True Production Systems:** Live public URL, FastAPI backend, Docker container, `pytest` unit tests, and Langfuse observability.
2. **3–5 Merged Open Source PRs:** Active contributor badge in 1–2 target GSoC AI/Data repositories.
3. **Internship Pipeline Active:** Resume v2.0 deployed, 50+ personalized founder/CTO cold outreaches across NCR/remote.

---

## ⚡ Why 3 Months Works (Applied AI vs. Research AI)
Companies hiring early-career AI Engineers in late 2026 do **not** expect you to write custom CUDA kernels or train foundation models from scratch. They look for candidates who can solve business problems with modern AI tools:
* Can you build a low-latency, hallucination-resistant RAG pipeline?
* Can you enforce strict JSON schemas with Pydantic and handle asynchronous streaming?
* Can you wrap AI agents in FastAPI, containerize them in Docker, and test them with `pytest`?
* Can you navigate a massive open-source GitHub codebase and submit clean pull requests?

---

## 🛡️ Phase 0: Academic Defense Mode (September 25 – October 10)
> **Objective:** Master 3rd-semester syllabus, crush mid-sems (Oct 5–10), and protect 8.43+ CGPA.
* **Rule:** Zero cognitive guilt about pausing side-project coding. CGPA is an absolute threshold filter for top-tier internships.
* **Coding Activity:** Maintenance only (light 15-min syntax review or syllabus DSA/DBMS synergy).

---

## 📅 The 11.5-Week Execution Schedule (October 12 – December 31)

### 🍁 Sprint 1: October 12 – November 08 (4 Weeks) — Ship Production RAG & FastAPI (PROJ-03)
*Goal: Turn PROJ-03 into your first 100% shipped, public-facing production AI system.*

* **Week 1 (Oct 12 – Oct 18): Production Python & FastAPI Service**
  * Master `Pydantic v2` for structured validation.
  * Build an asynchronous FastAPI backend (`async def`, background tasks, streaming responses).
  * **Free Resource:** [FastAPI Official Tutorial](https://fastapi.tiangolo.com/tutorial/) & [Pydantic Documentation](https://docs.pydantic.dev/).
* **Week 2 (Oct 19 – Oct 25): Retrieval Architecture (ChromaDB + Hybrid Search)**
  * Document parsing (PDF/Markdown) and recursive character chunking with token overlap.
  * Connect ChromaDB with local/free embedding models (Hugging Face / Gemini).
  * **Free Resource:** [DeepLearning.AI: Advanced Retrieval for AI with Chroma](https://www.deeplearning.ai/short-courses/advanced-retrieval-for-ai/).
* **Week 3 (Oct 26 – Nov 01): Observability, Evaluation & Pytest**
  * Integrate **Langfuse** for live latency, token cost, and trace monitoring.
  * Write automated tests using `pytest` (mocking vector search and LLM calls).
  * **Free Resource:** [Langfuse Open Source Docs](https://langfuse.com/docs) & [Corey Schafer PyTest Playlist](https://www.youtube.com/@coreyms).
* **Week 4 (Nov 02 – Nov 08): Containerization & Public Deployment**
  * Write a production multi-stage `Dockerfile`.
  * Deploy live to **Render** or **Hugging Face Spaces** with a clean UI.
  * **Deliverable:** **PROJ-03 Shipped** with a live public URL and public GitHub repository!

---

### ❄️ Sprint 2: November 09 – December 06 (4 Weeks) — GSoC 2027 Open Source Infiltration
*Goal: Establish credibility in open source and get 3–5 pull requests merged.*

* **Why November for GSoC 2027?** Maintainers select contributors who have already demonstrated familiarity with their codebase, testing standards, and community before official project proposals open.
* **Target Repositories (Pick 1 or 2):**
  1. **LiteLLM** (`BerriAI/litellm`): Fast-moving, Python, proxy for 100+ LLMs. High volume of `good first issue` tags.
  2. **Chroma** (`chroma-core/chroma`): Python/C++, open-source vector store. Excellent community for retrieval issues.
  3. **Scikit-Learn** or **LlamaIndex**: Established ecosystems with recurring GSoC project slots.
* **Weekly Execution:**
  * **Week 5 (Nov 09 – Nov 15): Setup & Codebase Familiarization**
    * Clone target repo, set up the local development environment, run test suite locally.
    * Join the organization's Discord/Slack and introduce yourself in `#contributing`.
  * **Week 6 (Nov 16 – Nov 22): PR #1 & #2 (Low-Hanging Fruit)**
    * Filter issues by `good first issue`, `documentation`, or `type: bug`.
    * Fix docs typos, add missing type hints, or add missing edge-case unit tests.
  * **Week 7 (Nov 23 – Nov 29): PR #3 & #4 (Substantive Bug Fix / Feature)**
    * Claim an open bug fix or implement a small requested feature with unit tests.
  * **Week 8 (Nov 30 – Dec 06): Relationship Building & Proposal Alignment**
    * Actively review other contributors' PRs, answer discussions, and identify potential GSoC proposal areas.

---

### 🚀 Sprint 3: December 07 – December 31 (3.5 Weeks) — Multi-Agent System & Internship Funnel
*Goal: Package your portfolio, build proof of agentic engineering, and trigger outbound applications.*

* **Week 9–10 (Dec 07 – Dec 20): Autonomous Agent System (PROJ-08)**
  * Build an advanced multi-agent system using **LangGraph** with state persistence and human-in-the-loop controls.
  * Alternatively, elevate **ORCA** (SIH 2nd place project) into a standalone, live web platform.
  * **Free Resource:** [DeepLearning.AI: LangChain & LangGraph Courses](https://www.deeplearning.ai/short-courses/).
* **Week 11 (Dec 15 – Dec 21): Resume v3.0 & Portfolio Overhaul**
  * Update [RESUME_v2.0.md](file:///C:/Users/kavya/Documents/antigravity/fearless-faraday/08_CAREER/RESUME_v2.0.md):
    * 2 Production Shipped URLs (RAG Engine + Agent System).
    * Section for **Open Source Contributions** listing merged PRs in major repos.
    * SIH 2026 2nd Place Award.
* **Week 12 (Dec 22 – Dec 31): Cold Outreach & Internship Blitz**
  * Target: 50 personalized outreach messages (using the value-first framework in [NETWORKING_SYSTEM.md](file:///C:/Users/kavya/Documents/antigravity/fearless-faraday/05_NETWORKING/NETWORKING_SYSTEM.md)).
  * Reach out to founders, CTOs, and tech leads at AI startups across NCR (Gurgaon Cyber City / Sector 44) and remote teams.
  * Pitch with working live demo links, not generic cover letters.

---

## 📚 Essential Free Resources Hub

| Focus Area | Top Free Resource | Direct Link |
| :--- | :--- | :--- |
| **FastAPI Backend** | FastAPI Official Documentation & Tutorial | [fastapi.tiangolo.com](https://fastapi.tiangolo.com/tutorial/) |
| **Modern Python & Testing** | Hypermodern Python (Packaging & Pytest) | [cjolowicz.github.io](https://cjolowicz.github.io/posts/hypermodern-python-01-setup/) |
| **Vector DBs & RAG** | Chroma & DeepLearning.AI Short Courses | [deeplearning.ai/short-courses](https://www.deeplearning.ai/short-courses/) |
| **Docker** | Docker Curriculum by Prakhar Srivastav | [docker-curriculum.com](https://docker-curriculum.com/) |
| **GSoC Playbook** | Google Summer of Code Student Guide | [google.github.io/gsocguides/student](https://google.github.io/gsocguides/student/) |
| **Full Stack AI** | Full Stack LLM Bootcamp (Free Lectures) | [fullstackdeeplearning.com](https://fullstackdeeplearning.com/llm-bootcamp/) |
