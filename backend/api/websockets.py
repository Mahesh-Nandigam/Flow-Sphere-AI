import asyncio
from fastapi import WebSocket, WebSocketDisconnect
from simulation.engine import AgentSimulation

def setup_routes(app):
    sim = AgentSimulation()

    @app.websocket("/ws")
    async def websocket_endpoint(websocket: WebSocket):
        await websocket.accept()
        try:
            while True:
                # Run one tick of the engine
                sim.tick()
                
                # Broadcast the state
                state = sim.get_state()
                await websocket.send_json(state)
                
                # Approx 10 frames per second
                await asyncio.sleep(0.1)
        except WebSocketDisconnect:
            print("Client disconnected")
