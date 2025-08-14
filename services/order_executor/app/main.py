import os
import socket
from datetime import datetime, timezone
from fastapi import FastAPI


def create_app() -> FastAPI:
    service_name = os.getenv("APP_NAME", "order-executor")
    app = FastAPI(title=service_name)
    start_time = datetime.now(timezone.utc)
    hostname = socket.gethostname()

    @app.get("/health")
    def health():
        now = datetime.now(timezone.utc)
        return {
            "status": "ok",
            "name": service_name,
            "hostname": hostname,
            "time": now.isoformat(),
            "uptime_seconds": (now - start_time).total_seconds(),
        }

    @app.get("/")
    def root():
        return {"message": f"{service_name} is running"}

    return app