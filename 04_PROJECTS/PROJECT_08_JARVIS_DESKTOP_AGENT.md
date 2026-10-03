# Project PROJ-08: Jarvis Desktop & Browser OS Agent

> An autonomous desktop assistant and browser agent capable of executing complex computer tasks, web research, file operations, and application workflows via natural language commands.

* **Project ID:** PROJ-08
* **Collaborators:** Kavya Gupta & Classmate
* **Target Sprint:** Q4 2026 / Sprint 3 (Autonomous Agents)
* **Status:** 💡 Ideation & Architectural Specification

---

## 🧭 Project Vision & Motivation
Modern AI assistants are trapped in web chat boxes without access to local computer state, applications, or browser automation. 
Inspired by **Anthropic's Computer Use**, **Perplexity Comet Browser**, and expanding upon our earlier **Kenny-desktop-health (PROJ-05)** MCP prototype, **Jarvis** is designed as an agentic operating layer over the user's laptop. 

Given a single natural language command (e.g., *"Search the web for the best flight options to Mumbai next Friday, compile them in an Excel sheet on my Desktop, and open the sheet"*), the agent plans, executes, verifies, and reports completion autonomously.

---

## 🏗️ System Architecture

```mermaid
graph TD
    User([User Prompt / Hotkey Trigger]) --> Planner[Agent Brain / LLM Planner]
    
    subgraph Core Agentic Loop
        Planner -->|1. Decompose Task| Plan[Execution Plan & Step State]
        Plan -->|2. Select Tool| ToolDispatcher[Tool Router & Dispatcher]
        ToolDispatcher -->|Validate Action| SafetyGate{Destructive Action?}
        SafetyGate -->|Yes| Confirm[Human-in-the-Loop Confirmation]
        Confirm -->|Approved| Executor[Action Execution]
        SafetyGate -->|No| Executor
        Executor -->|Execution Result| Observer[Observation / State Verification]
        Observer -->|Feedback Loop| Planner
    end

    subgraph Tooling Layer (System & Browser)
        Executor --> BrowserTool[Browser Automation: Playwright / Perplexity Style Web Search]
        Executor --> MCPTools[Model Context Protocol Tools: Filesystem, Shell, Process Manager]
        Executor --> GUITool[GUI & App Controller: Screen Capture & Hotkeys]
    end

    Planner -->|Task Complete| Response([Voice / HUD Output to User])
```

---

## 🛠️ Proposed Tech Stack

| Component | Technology | Rationale |
| :--- | :--- | :--- |
| **Agent Framework** | **LangGraph / Pydantic AI** | State persistence, cyclical agentic loops, and built-in human-in-the-loop approval gates. |
| **Core Brain (LLM)** | **Gemini 2.0 Flash / Claude 3.5 / Ollama (Local)** | Multimodal vision capabilities (for screen reading) and high-speed tool-calling latency. |
| **System & OS Layer** | **FastMCP (Python)** | Seamlessly extends PROJ-05; exposes file I/O, PowerShell commands, and system vitals via stdio. |
| **Browser Engine** | **Playwright / Browser-Use** | Headless and headed DOM automation, web scraping, form filling, and live session navigation. |
| **Interface** | **Python Tray App / Floating HUD (PyQt / Webview)** | Global hotkey listener (e.g. `Alt + Space`) triggering a lightweight command input bar. |

---

## 🎯 Core Functional Capabilities

### 1. Browser & Research Agent (Perplexity / Comet Style)
* Executes deep web searches across search engines.
* Opens target URLs, parses dynamic DOM elements, filters ads/clutter, and synthesizes answers with citations.
* Can navigate interactive websites (e.g., fill out forms, download files, book tickets with user confirmation).

### 2. Local OS Operations & Automation
* **File Management:** Search, create, read, organize, and edit local files (CSV, PDF, Markdown, codebases).
* **Application Control:** Launch desktop software (VS Code, Spotify, Browser, Notion) and trigger shortcuts.
* **Command Execution:** Run PowerShell/Terminal scripts with automatic error recovery (if a script fails, the agent reads stderr and self-corrects).

### 3. Safety & Permission Guardrails
* **Sandbox & Allowlisting:** Read operations run automatically; destructive write/delete/shell commands (`rm`, system file overwrites, payments) require explicit single-click user approval.

---

## 📅 Roadmap & Milestones
* **Phase 1: Architecture & Tooling Protocol (Post-Exams / Late Nov 2026)**
  * Define the unified tool schema using Pydantic models.
  * Integrate Playwright browser automation and FastMCP local system tools.
* **Phase 2: Core ReAct Agent Loop (Dec 2026)**
  * Implement the planning and self-correction loop in LangGraph.
  * Add live screen observation and DOM parsing.
* **Phase 3: HUD Interface & Shipped Release (Late Dec 2026)**
  * Build the floating desktop interface with hotkey launch.
  * Package into an executable installer or single-command local setup.
