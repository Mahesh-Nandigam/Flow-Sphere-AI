from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from api.websockets import setup_routes

app = FastAPI(title="FlowSphere OS API", description="Operating System for Physical Spaces")

# Security: Restrict CORS strictly to the React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

setup_routes(app)

@app.get("/")
def read_root():
    return {"message": "FlowSphere Adaptive Infrastructure Control Layer is running."}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
