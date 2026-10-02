class ResponseEngine:

    def block_ip(self, ip: str):
        return {
            "action": "block_ip",
            "target": ip,
            "status": "queued"
        }

    def isolate_host(self, host: str):

        return {
            "action": "isolate_host",
            "target": host,
            "status": "queued"
        }

    def notify(self, message: str):

        return {
            "action": "notify",
            "message": message,
            "status": "queued"
        }
