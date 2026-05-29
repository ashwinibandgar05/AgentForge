# GenAI Adaptive Urban Traffic Management — Pune
### Case Study Implementation | Python

---

## Project Structure

```
genai_traffic_management/
├── main.py          ← Full system (run this)
├── requirements.txt ← Dependencies
└── README.md        ← This file
```

---

## How to Run

```bash
pip install numpy
python main.py
```

---

## What Each Module Does

| Module | Class | Technique | What it does |
|--------|-------|-----------|--------------|
| GAN | `TrafficGAN` | Generative Adversarial Network | Synthesizes realistic Pune traffic scenarios from 5-year training data |
| LLM Advisor | `LLMIncidentAdvisor` | Large Language Model | Generates English + Marathi citizen alerts & natural-language signal commands |
| Forecaster | `GenerativeForecaster` | Transformer / Spatio-temporal | Predicts congestion 30–60 min ahead |
| RL Controller | `RLSignalController` | Q-Learning (RL) | Selects optimal signal timings to minimize wait, CO₂, emergency delay |
| Orchestrator | `TrafficManagementSystem` | System integration | Runs the full pipeline per intersection cycle |

---

## Architecture (from presentation)

```
DATA INGESTION         GEN AI PROCESSING       OUTPUT / ACTION
─────────────          ─────────────────       ───────────────
CCTV Streams     →     GAN (Synthetic Data) →  Adaptive Signal Timings
GPS Vehicle Data →     LLM (Incident Adv.)  →  Emergency Corridors
Weather API      →     Diffusion Forecaster →  Citizen Alerts (SMS/App)
Event Calendars  →     RL Signal Controller →  Dashboard Analytics
Historical DB    →                          →  City Planner Reports
```

---

## Results (Shivajinagar Pilot — from presentation)

| Metric | Before Gen AI | After Gen AI |
|--------|--------------|-------------|
| Wait Time (sec) | 87 | 34 |
| Throughput (veh/hr) | 1,200 | 1,950 |
| CO₂/vehicle (g) | 48 | 18 |
| Emergency Delay (min) | 8.2 | 2.1 |

---

## Production Upgrade Path

- Replace `TrafficGAN` with a **PyTorch DCGAN** trained on real CCTV feeds
- Replace `GenerativeForecaster` with a **Hugging Face Transformer** fine-tuned on Pune traffic sequences
- Replace `RLSignalController` with **Stable-Baselines3 PPO** agent in a SUMO/CARLA simulator
- Replace `LLMIncidentAdvisor` with a **fine-tuned GPT-4/Llama** model on PMC incident reports
