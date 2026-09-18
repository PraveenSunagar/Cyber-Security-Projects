from fastapi import FastAPI
from backend.api.events import router as events_router
from backend.api.alerts import router as alerts_router
from backend.api.incidents import router as incidents_router
app = FastAPI(
    title="SentinelX",
    version="1.0.0",
    description="AI-Powered SOC/XDR Platform"
)

app.include_router(events_router, prefix="/api/events", tags=["Events"])
app.include_router(alerts_router, prefix="/api/alerts", tags=["Alerts"])
app.include_router(incidents_router, prefix="/api/incidents", tags=["Incidents"])

@app.get("/")
def root():
    return {
        "name": "SentinelX",
        "status": "online",
        "version": "1.0.0"
    }


@app.get("/health")
def health():
    return {"status": "healthy"}
