import random
import time
import os
import google.generativeai as genai
from typing import Dict, Any, List

class AIController:
    def __init__(self) -> None:
        self.logs: List[Dict[str, Any]] = []
        self.last_eval: float = time.time()
        self.log_id: int = 0
        
        # Google Services Integration: Gemini Generative AI
        self.gemini_active = False
        api_key = os.environ.get("GEMINI_API_KEY")
        if api_key:
            genai.configure(api_key=api_key)
            self.model = genai.GenerativeModel('gemini-1.5-flash')
            self.gemini_active = True

    def _generate_explanation(self, gate_name: str, load_percent: float) -> str:
        """Uses Google Gemini API to generate an explainable AI snippet, or falls back to template."""
        if self.gemini_active:
            prompt = f"Act as an automated stadium security AI. A gate named {gate_name} just reached {load_percent}% capacity. In exactly one short sentence, state what action the system took to prevent a stampede."
            try:
                response = self.model.generate_content(prompt)
                return f"[Gemini AI] {response.text.strip()}"
            except Exception as e:
                # Graceful fallback (Security standard)
                pass 
                
        return f"Urgent: {gate_name} congested because density surpassed 80%. Adaptive Infrastructure triggered: Throttling inflow."

    def evaluate(self, agents: List[Dict[str, Any]], gates: Dict[str, Dict[str, Any]]) -> None:
        """Evaluates crowding mechanisms based on Swarm proximity."""
        current_time = time.time()
        if current_time - self.last_eval < 2.0:
            return
            
        self.last_eval = current_time
        gate_counts: Dict[str, int] = {gate_name: 0 for gate_name in gates.keys()}
        
        for agent in agents:
            target = gates[agent["target_gate"]]
            dist = ((target["x"] - agent["x"])**2 + (target["y"] - agent["y"])**2)**0.5
            if dist < 150: 
                gate_counts[agent["target_gate"]] += 1
                
        for gate_name, data in gates.items():
            count = gate_counts[gate_name]
            data["load"] = min(1.0, count / 50.0)
            
            if data["load"] > 0.8 and data["status"] == "open":
                data["status"] = "throttled"
                
                # Google AI Generation
                msg = self._generate_explanation(gate_name, round(data["load"] * 100))
                self.add_log(msg, "urgent")
                
                from routing.graph import recalculate_routes
                recalculate_routes(agents, gates, origin_gate=gate_name)
                
            elif data["load"] < 0.4 and data["status"] == "throttled":
                data["status"] = "open"
                self.add_log(f"Recovery: {gate_name} wait time decreased. Re-opening physical gate.", "success")
                
    def add_log(self, message: str, msg_type: str) -> None:
        """Pushes a new AI decision log to the UI."""
        self.log_id += 1
        new_log = {
            "id": self.log_id,
            "type": msg_type,
            "text": message,
            "time": time.strftime("%H:%M:%S", time.localtime())
        }
        self.logs.insert(0, new_log)
        if len(self.logs) > 10:
            self.logs = self.logs[:10]

    def get_logs(self) -> List[Dict[str, Any]]:
        return self.logs
