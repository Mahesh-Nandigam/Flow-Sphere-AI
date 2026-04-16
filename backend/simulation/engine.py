import random
from core.intelligence import AIController

class AgentSimulation:
    def __init__(self, num_agents=150):
        self.num_agents = num_agents
        self.agents = []
        self.ai = AIController()
        
        self.gates = {
            "Gate 1": {"x": 100, "y": 700, "status": "open", "load": 0.2},
            "Gate 2": {"x": 500, "y": 700, "status": "open", "load": 0.4},
            "Gate 3": {"x": 900, "y": 700, "status": "open", "load": 0.3}
        }
        
        # Initialize agents
        for i in range(self.num_agents):
            self.agents.append({
                "id": i,
                "x": random.uniform(200, 800),
                "y": random.uniform(100, 500),
                "target_gate": random.choice(list(self.gates.keys())),
                "status": "normal"
            })

    def tick(self):
        # Update agent positions (Swarm Intelligence & Physics mock)
        for agent in self.agents:
            target = self.gates[agent["target_gate"]]
            
            # Simple vector movement towards target
            dt_x = target["x"] - agent["x"]
            dt_y = target["y"] - agent["y"]
            
            dist = (dt_x**2 + dt_y**2)**0.5
            if dist > 10:
                speed = 2.0
                agent["x"] += (dt_x / dist) * speed
                agent["y"] += (dt_y / dist) * speed
                
            # If agent reaches gate, respawn them for continuous simulation
            if dist <= 10:
                agent["x"] = random.uniform(200, 800)
                agent["y"] = random.uniform(100, 200)
                agent["target_gate"] = random.choice(list(self.gates.keys()))
                
        # Let AI evaluate stadium metrics (Agent density mapping)
        self.ai.evaluate(self.agents, self.gates)

    def get_state(self):
        return {
            "agents": self.agents,
            "gates": self.gates,
            "logs": self.ai.get_logs()
        }
