from pydantic import BaseModel, Field
from typing import List

class GateSchema(BaseModel):
    x: float = Field(..., description="X coordinate of the gate")
    y: float = Field(..., description="Y coordinate of the gate")
    status: str = Field(..., description="Gate operational status (e.g., 'open', 'throttled')")
    load: float = Field(..., description="Percentage load metric (0.0 to 1.0)")

class AgentSchema(BaseModel):
    id: int
    x: float
    y: float
    target_gate: str
    status: str = "normal"

class SimulationState(BaseModel):
    agents: List[AgentSchema]
    gates: dict[str, GateSchema]
    logs: List[dict]
