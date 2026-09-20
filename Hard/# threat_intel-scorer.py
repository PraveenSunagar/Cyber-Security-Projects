# threat_
class RiskScorer:

    def calculate(self, detections):

        if not detections:
            return {
                "score": 0,
                "severity": "LOW"
            }

        score = max(d.score for d in detections)

        if score >= 90:
            severity = "CRITICAL"
        elif score >= 80:
            severity = "HIGH"
        elif score >= 50:
            severity = "MEDIUM"
        else:
            severity = "LOW"

        return {
            "score": score,
            "severity": severity
        }
