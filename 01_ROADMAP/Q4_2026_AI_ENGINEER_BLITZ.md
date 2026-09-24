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

## 📅 The 12-Week Sprint Schedule

### 🍁 Month 1: October 2026 — Ship Production RAG & FastAPI (PROJ-03)
*Goal: Turn PROJ-03 into your first 100% shipped, public-facing production AI system.*

* **Week 1 (Oct 01 – Oct 07): Production Python & FastAPI Service**
  * Master `Pydantic v2` for structured inputs/outputs and data validation.
  * Build an asynchronous FastAPI backend (`async def`, background tasks, streaming responses).
  * **Free Resource:** [FastAPI Official Tutorial](https://fastapi.tiangolo.com/tutorial/) & [Pydantic Documentation](https://docs.pydantic.dev/).
* **Week 2 (Oct 08 – Oct 14): Retrieval Architecture (ChromaDB + Hybrid Search)**
  * Implement document parsing (PDF/Markdown), recursive character chunking with token overlap.
  * Connect ChromaDB/Qdrant vector store with local/free embedding models (Hugging Face / Gemini).
  * **Free Resource:** [DeepLearning.AI: Advanced Retrieval for AI with Chroma](https://www.deeplearning.ai/short-courses/advanced-retrieval-for-ai/).
* **Week 3 (Oct 15 – Oct 21): Observability, Evaluation & Pytest**
  * Integrate **Langfuse** for live latency, token cost, and trace monitoring.
  * Write automated tests using `pytest` (mocking vector search and LLM calls).
  * **Free Resource:** [Langfuse Open Source Docs](https://langfuse.com/docs) & [Corey Schafer PyTest Playlist](https://www.youtube.com/@coreyms).
* **Week 4 (Oct 22 – Oct 31): Containerization & Public Deployment**
  * Write a production multi-stage `Dockerfile`.
  * Deploy live to **Render** or **Hugging Face Spaces** with a clean UI (Streamlit or React).
  * **Deliverable:** **PROJ-03 Shipped** with a live public URL and public GitHub repository!

---

### ❄️ Month 2: November 2026 — GSoC 2027 Open Source Infiltration
*Goal: Establish credibility in open source before official GSoC organization announcements.*

* **Why Start in November for GSoC 2027?**
  * GSoC organizations are announced in February/March, but maintainers pick contributors who have **already been active** in their repos during the winter.
* **Target Repositories (Pick 1 or 2):**
  1. **LiteLLM** (`BerriAI/litellm`): Fast-moving, Python, proxy for 100+ LLMs. High volume of "good first issues".
  2. **Chroma** (`chroma-core/chroma`): Python/C++, open-source vector store. Great community for indexing/RAG.
  3. **LangChain / LlamaIndex**: Massive ecosystems with active integrations and documentation tracks.
  4. **Scikit-Learn** or **SymPy**: Classic Python open-source mainstays with dedicated GSoC slots.
* **Weekly Execution:**
  * **Week 5 (Nov 01 – Nov 07): Setup & Codebase Familiarization**
    * Clone target repo, set up the development environment, run the full test suite locally.
    * Join the organization's Discord/Slack and introduce yourself in `#contributing`.
  * **Week 6 (Nov 08 – Nov 14): PR #1 & #2 (Low-Hanging Fruit)**
    * Filter issues by `good first issue`, `documentation`, or `type: bug`.
    * Fix typos in docs, add missing type hints, or add missing edge-case unit tests.
  * **Week 7 (Nov 15 – Nov 21): PR #3 & #4 (Substantive Bug Fix / Feature)**
    * Claim an open bug fix or implement a small requested feature.
    * Follow contribution guidelines strictly: write tests, format code with `ruff`/`black`, submit descriptive PR.
  * **Week 8 (Nov 22 – Nov 30): Relationship Building**
    * Actively review other contributors' PRs and help answer questions in issues.
    * Document your open-source journey on LinkedIn.

---

### 🚀 Month 3: December 2026 — Multi-Agent System & Internship Funnel
*Goal: Package your portfolio, build proof of agentic engineering, and trigger outbound applications.*

* **Week 9–10 (Dec 01 – Dec 14): Autonomous Agent System (PROJ-08)**
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
