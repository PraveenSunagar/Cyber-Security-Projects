# backend/api/

from fastapi import APIRouter

from backend.schemas import SecurityEvent
from detector.engine import DetectionEngine
from threat_intel.scorer import RiskScorer

router = APIRouter()

detector = DetectionEngine()
risk = RiskScorer()


@router.post("/")
def analyze_event(event: SecurityEvent):

    data = event.model_dump()

    detections = detector.analyze(data)

    risk_result = risk.calculate(detections)

    return {
        "event": data,
        "detections": [
            {
                "rule_id": d.rule_id,
                "name": d.name,
                "severity": d.severity,
                "score": d.score,
                "description": d.description,
                "mitre": d.mitre
            }
            for d in detections
        ],
        "risk": risk_result
    }
