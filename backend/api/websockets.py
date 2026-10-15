import asyncio
from fastapi import WebSocket, WebSocketDisconnect
from simulation.engine import AgentSimulation

def setup_routes(app):
    sim = AgentSimulation()

    @app.get("/api/state")
    @app.get("/state")
    def get_simulation_state():
        sim.tick()
        return sim.get_state()

    @app.websocket("/api/ws")
    @app.websocket("/ws")
    async def websocket_endpoint(websocket: WebSocket):
        await websocket.accept()
        try:
            while True:
                sim.tick()
                state = sim.get_state()
                await websocket.send_json(state)
                await asyncio.sleep(0.1)
        except WebSocketDisconnect:
            print("Client disconnected")
