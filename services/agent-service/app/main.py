
import utils.session
from fastapi import FastAPI

app = FastAPI(
    title="Sahayak AI Agent Service",
    description="AI agent service for Sahayak AI",
    version="0.1.0",
)


@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "service": "agent-service"
    }
