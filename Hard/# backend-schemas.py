from pydantic import BaseModel


class SecurityEvent(BaseModel):

    source_ip: str
    destination_ip: str | None = None

    event_type: str

    failed_logins: int = 0
    unique_ports: int = 0
    dns_requests: int = 0

    username: str | None = None

    timestamp: str | None = None
