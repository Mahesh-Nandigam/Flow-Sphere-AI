import pytest
from core.intelligence import AIController

def test_stampede_throttle_trigger():
    """
    Test Validation: Ensure the AI correctly detects a load > 80% 
    and automatically shifts physical infrastructure status to 'throttled'.
    """
    ai = AIController()
    
    # Mocking massive congestion strictly at Gate 1 (>80%)
    mock_agents = [{"x": 100, "y": 700, "target_gate": "Gate 1", "status": "normal"} for _ in range(45)]
    mock_gates = {
        "Gate 1": {"x": 100, "y": 700, "status": "open", "load": 0.0},
        "Gate 2": {"x": 500, "y": 700, "status": "open", "load": 0.0}
    }
    
    # Advance internal eval timer artificially so execution bypasses rate limit
    ai.last_eval = 0 
    
    ai.evaluate(mock_agents, mock_gates)
    
    assert mock_gates["Gate 1"]["load"] >= 0.8
    assert mock_gates["Gate 1"]["status"] == "throttled"
    
def test_ai_log_generation():
    """
    Test Validation: Ensure XAI engine correctly logs the reason for throttling.
    """
    ai = AIController()
    mock_agents = [{"x": 100, "y": 700, "target_gate": "Gate 1", "status": "normal"} for _ in range(45)]
    mock_gates = {"Gate 1": {"x": 100, "y": 700, "status": "open", "load": 0.0}}
    ai.last_eval = 0 
    
    ai.evaluate(mock_agents, mock_gates)
    
    logs = ai.get_logs()
    assert len(logs) == 1
    assert "Urgent" in logs[0]["text"] or "[Gemini AI]" in logs[0]["text"]
    assert logs[0]["type"] == "urgent"
