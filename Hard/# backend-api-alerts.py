from fastapi import APIRouter

router = APIRouter()

alerts = []


@router.get("/")
def get_alerts():

    return {
        "count": len(alerts),
        "alerts": alerts
    }


@router.post("/")
def create_alert(alert: dict):

    alerts.append(alert)

    return {
        "status": "created",
        "alert": alert
    }

