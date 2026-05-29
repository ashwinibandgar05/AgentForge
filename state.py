from typing import TypedDict, Annotated
import operator

class AgentState(TypedDict):
    goal: str
    plan: list[str]
    current_step: int
    step_results: Annotated[list, operator.add]
    final_output: str
    critique: str
    retry_count: int
