from fastapi import FastAPI
from fastapi.responses import StreamingResponse, HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import json
import sys
import os

sys.path.insert(0, os.path.dirname(__file__))

from dotenv import load_dotenv
load_dotenv()

from groq import Groq
from state import AgentState
from langgraph.graph import StateGraph, END
from typing import Annotated
import operator

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

logs = []

def call_groq(system: str, user: str) -> str:
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": system},
            {"role": "user",   "content": user}
        ],
        temperature=0
    )
    return response.choices[0].message.content

def planner_node(state: AgentState) -> dict:
    critique = state.get("critique", "")
    retry_context = f"\nPrevious attempt failed. Critic said: {critique}" if critique else ""
    response = call_groq(
        system="You are a task planner. Break the goal into 3-5 concrete, executable steps. Respond with a JSON array of strings only. No markdown, no explanation.",
        user=f"Goal: {state['goal']}{retry_context}"
    )
    try:
        clean = response.strip().strip("```json").strip("```").strip()
        plan = json.loads(clean)
    except:
        plan = [state["goal"]]
    logs.append({"type": "planner", "steps": plan})
    return {"plan": plan, "current_step": 0, "step_results": []}

def executor_node(state: AgentState) -> dict:
    step = state["plan"][state["current_step"]]
    logs.append({"type": "executor", "step": state["current_step"]+1, "label": step})
    response = call_groq(
        system="You are a task executor. Complete the given step thoroughly and return a detailed result as plain text.",
        user=f"Step to execute: {step}\n\nContext from previous steps:\n{chr(10).join(state['step_results'])}"
    )
    result = f"Step {state['current_step']+1} — {step}:\n{response}"
    next_step = state["current_step"] + 1
    final = ""
    if next_step >= len(state["plan"]):
        all_results = state["step_results"] + [result]
        final = "\n\n---\n\n".join(all_results)
    return {"step_results": [result], "current_step": next_step, "final_output": final}

def critic_node(state: AgentState) -> dict:
    response = call_groq(
        system="""You are a quality critic. Evaluate the output against the original goal.
Respond ONLY with a JSON object (no markdown):
{"verdict": "accept" or "retry", "reason": "short explanation", "score": 1-10}
Accept if score >= 7.""",
        user=f"Original goal: {state['goal']}\n\nOutput produced:\n{state['final_output']}"
    )
    try:
        clean = response.strip().strip("```json").strip("```").strip()
        data = json.loads(clean)
    except:
        data = {"verdict": "accept", "reason": "parse error", "score": 8}
    verdict = data.get("verdict", "accept")
    reason  = data.get("reason", "")
    score   = data.get("score", 0)
    logs.append({"type": "critic", "score": score, "verdict": verdict, "reason": reason})
    return {
        "critique": f"{'ACCEPT' if verdict == 'accept' else 'RETRY'}: {reason}",
        "retry_count": state.get("retry_count", 0) + 1
    }

def should_continue_executing(state):
    return "execute" if state["current_step"] < len(state["plan"]) else "critique"

def critic_decision(state):
    if state.get("retry_count", 0) >= 3:
        return "done"
    return "done" if state.get("critique", "").startswith("ACCEPT") else "retry"

def build_graph():
    graph = StateGraph(AgentState)
    graph.add_node("planner", planner_node)
    graph.add_node("executor", executor_node)
    graph.add_node("critic", critic_node)
    graph.set_entry_point("planner")
    graph.add_edge("planner", "executor")
    graph.add_conditional_edges("executor", should_continue_executing, {"execute": "executor", "critique": "critic"})
    graph.add_conditional_edges("critic", critic_decision, {"done": END, "retry": "planner"})
    return graph.compile()

class GoalRequest(BaseModel):
    goal: str

@app.post("/run")
def run_agent(req: GoalRequest):
    global logs
    logs = []
    app_graph = build_graph()
    result = app_graph.invoke({
        "goal": req.goal,
        "plan": [],
        "current_step": 0,
        "step_results": [],
        "final_output": "",
        "critique": "",
        "retry_count": 0
    })
    return {
        "output": result["final_output"],
        "retries": result["retry_count"],
        "critique": result["critique"],
        "logs": logs
    }

@app.get("/", response_class=HTMLResponse)
def index():
    with open("index.html") as f:
        return f.read()
