# ai_analyst/analyst.py

class SOCAnalyst:

    def analyze(self, event, detections, risk):

        if not detections:

            return {
                "verdict": "BENIGN",
                "confidence": 0.90,
                "summary": "No suspicious activity detected."
            }

        highest = max(
            detections,
            key=lambda x: x["score"]
        )

        return {
            "verdict": "SUSPICIOUS",
            "confidence": min(
                highest["score"] / 100,
                0.99
            ),
            "summary": (
                f"{highest['name']} detected from "
                f"{event.get('source_ip')}"
            ),
            "mitre": highest.get("mitre"),
            "risk": risk
        }
