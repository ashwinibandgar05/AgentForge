# AgentForge 🔥
[![Deploy](https://img.shields.io/badge/Live-AgentForge-brightgreen?style=flat-square)](https://agentforge.onrender.com)

> An intelligent multi-agent AI system that forges any goal into high-quality results using a Planner → Executor → Critic loop.

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=flat-square)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-teal?style=flat-square)
![LangGraph](https://img.shields.io/badge/LangGraph-latest-purple?style=flat-square)
![Groq](https://img.shields.io/badge/Groq-LLaMA_3.3-orange?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)

---

## What is AgentForge?

AgentForge is a multi-agent AI system where three specialized AI agents collaborate to complete any goal you give them:

- 🧠 **Planner** — breaks your goal into 3–5 clear, executable steps
- ⚙️ **Executor** — runs each step using an LLM and builds the output
- 🔍 **Critic** — scores the output (1–10) and retries if quality is below 7

The system automatically retries up to 3 times until the Critic is satisfied, ensuring high-quality results every time.

---

## Demo

```
Goal: Compare FastAPI, Flask, and Django for building REST APIs

[PLANNER] Created 4 steps:
  1. Research FastAPI features and use cases
  2. Research Flask features and use cases
  3. Research Django REST Framework
  4. Write comparison with recommendation

[EXECUTOR] Running step 1...
[EXECUTOR] Running step 2...
[EXECUTOR] Running step 3...
[EXECUTOR] Running step 4...
[EXECUTOR] All steps completed. Sending to Critic.

[CRITIC] Score: 9/10 | Verdict: ACCEPT | Reason: Comprehensive comparison with clear recommendation

FINAL OUTPUT
...detailed comparison...
```

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Frontend | HTML, CSS, JavaScript |
| Backend | Python, FastAPI, Uvicorn |
| AI Agents | LangGraph, LangChain |
| LLM | Groq API (LLaMA 3.3 70B) |

---

## Project Structure

```
agentforge/
├── server.py        ← FastAPI backend + agent logic
├── agents.py        ← Planner, Executor, Critic agents
├── graph.py         ← LangGraph state machine wiring
├── state.py         ← Shared state between agents
├── index.html       ← Frontend website
├── requirements.txt ← Python dependencies
├── .env.example     ← API key template
└── README.md
```

---

## Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/ashwinibandgar05/AgentForge.git
cd agentforge
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Get your free Groq API key
- Go to 👉 [console.groq.com](https://console.groq.com)
- Sign up with Google (free, no credit card needed)
- Click **API Keys** → **Create API Key** → Copy it

### 4. Add your API key
```bash
cp .env.example .env
```
Open `.env` and paste your key:
```
GROQ_API_KEY=your_groq_api_key_here
```

### 5. Run the server
```bash
uvicorn server:app --reload
```

### 6. Open in browser
```
http://localhost:8000
```

---

## How It Works

```
User Goal
    ↓
[Planner] → breaks into steps
    ↓
[Executor] → runs each step with LLM
    ↓
[Critic] → scores output (1-10)
    ↓
Score ≥ 7? → Return final output
Score < 7? → Retry (back to Planner, max 3 times)
```

---

## Example Goals to Try

```
Research the top 3 Python frameworks for building REST APIs and compare them
```
```
Create a 3-month roadmap to learn Machine Learning from scratch
```
```
Write a business plan for a food delivery startup targeting college students
```
```
Explain the top 5 sorting algorithms with time complexity and use cases
```

---

## Skills Demonstrated

- ✅ Multi-agent AI system design
- ✅ LangGraph state machines with conditional routing
- ✅ FastAPI REST backend development
- ✅ Prompt engineering for structured LLM outputs
- ✅ Full-stack web development (HTML/CSS/JS + Python)
- ✅ Free LLM API integration (Groq + LLaMA 3.3)
- ✅ Self-correcting AI with retry logic

---

## License

MIT License — free to use, modify, and distribute.

---

<p align="center">Built with ❤️ using Python, LangGraph, and Groq</p>
