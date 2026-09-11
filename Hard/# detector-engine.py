from dataclasses import dataclass


@dataclass
class Detection:
    rule_id: str
    name: str
    severity: str
    score: int
    description: str
    mitre: str


class DetectionEngine:

    def analyze(self, event: dict) -> list[Detection]:

        detections = []

        failed = event.get("failed_logins", 0)

        if failed >= 10:
            detections.append(
                Detection(
                    rule_id="DET-001",
                    name="SSH Brute Force",
                    severity="HIGH",
                    score=85,
                    description=f"{failed} failed login attempts",
                    mitre="T1110.001"
                )
            )

        ports = event.get("unique_ports", 0)

        if ports >= 20:
            detections.append(
                Detection(
                    rule_id="DET-002",
                    name="Port Scan",
                    severity="HIGH",
                    score=80,
                    description=f"{ports} unique ports accessed",
                    mitre="T1046"
                )
            )

        dns_requests = event.get("dns_requests", 0)

        if dns_requests >= 500:
            detections.append(
                Detection(
                    rule_id="DET-003",
                    name="DNS Anomaly",
                    severity="MEDIUM",
                    score=65,
                    description="Abnormally high DNS request volume",
                    mitre="T1071.004"
                )
            )

        return detections
