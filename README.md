# AgentForge 🔥
[![Deploy](https://img.shields.io/badge/Live-AgentForge-brightgreen?style=flat-square)](https://agentforge.onrender.com)

> An intelligent multi-agent AI system that forges any goal into high-quality results using a Planner → Executor → Critic loop.

## What is AgentForge?
Three AI agents collaborate to complete any goal:
- 🧠 **Planner** — breaks your goal into 3–5 clear steps
- ⚙️ **Executor** — runs each step using an LLM
- 🔍 **Critic** — scores output (1–10), retries if below 7

## Tech Stack
| Layer | Technology |
|-------|-----------|
| Frontend | HTML, CSS, JavaScript |
| Backend | Python, FastAPI, Uvicorn |
| AI Agents | LangGraph, LangChain |
| LLM | Groq API (LLaMA 3.3 70B) |

## Run Locally
```bash
pip install -r requirements.txt
uvicorn server:app --reload
```

## Skills Demonstrated
- ✅ Multi-agent AI system design
- ✅ LangGraph state machines with conditional routing
- ✅ FastAPI REST backend development
- ✅ Prompt engineering for structured LLM outputs
- ✅ Full-stack web development
- ✅ Free LLM API integration (Groq + LLaMA 3.3)
