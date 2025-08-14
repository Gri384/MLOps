import os
import socket
from datetime import datetime, timezone
from fastapi import FastAPI, HTTPException, Query
import httpx


BINANCE_REST_BASE = os.getenv("BINANCE_REST_BASE", "https://testnet.binance.vision")


def create_app() -> FastAPI:
    service_name = os.getenv("APP_NAME", "market-data")
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

    @app.get("/klines")
    async def klines(
        symbol: str = Query(..., examples=["BTCUSDT"]),
        interval: str = Query("1m", examples=["1m", "5m", "1h", "1d"]),
        limit: int = Query(100, ge=1, le=1000),
    ):
        url = f"{BINANCE_REST_BASE}/api/v3/klines"
        params = {"symbol": symbol.upper(), "interval": interval, "limit": limit}
        try:
            async with httpx.AsyncClient(timeout=10.0) as client:
                resp = await client.get(url, params=params)
                if resp.status_code != 200:
                    raise HTTPException(status_code=resp.status_code, detail=resp.text)
                data = resp.json()
                return {"symbol": symbol.upper(), "interval": interval, "limit": limit, "klines": data}
        except httpx.RequestError as e:
            raise HTTPException(status_code=502, detail=f"upstream error: {str(e)}")

    return app