import random

def recalculate_routes(agents, gates, origin_gate):
    """
    Mock Graph Algorithm (Dijkstra/A* abstract representation)
    Dynamically re-assigns agents heading to the throttled gate
    toward the least congested open gates (Swarm Intelligence).
    """
    open_gates = [name for name, data in gates.items() if data["status"] == "open"]
    
    if not open_gates:
        return # No alternative paths
        
    for agent in agents:
        if agent["target_gate"] == origin_gate:
            # Rebalance 50% of the agents headings to that gate
            if random.random() > 0.5:
                # Distribute intelligently among open gates (not just funneling to one)
                new_target = random.choice(open_gates)
                agent["target_gate"] = new_target
                agent["status"] = "warning" # Color them yellow to visualize the reroute
