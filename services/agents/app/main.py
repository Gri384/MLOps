import os
import socket
from datetime import datetime, timezone
from enum import Enum
from typing import Dict, Any, Optional

from fastapi import FastAPI, HTTPException

try:
    from openai import OpenAI
except Exception:  # pragma: no cover
    OpenAI = None  # type: ignore


class AgentRole(str, Enum):
    ORCHESTRATOR = "orchestrator"
    ARCHITECT = "architect"
    BACKEND = "backend"
    FRONTEND = "frontend"
    STRATEGY_RESEARCHER = "strategy_researcher"
    RISK_MANAGER = "risk_manager"
    QA_ENGINEER = "qa_engineer"
    DEVOPS = "devops"
    CRITIC = "critic"


def _init_llm() -> Optional["OpenAI"]:
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key or OpenAI is None:
        return None
    return OpenAI(api_key=api_key)


def create_app() -> FastAPI:
    service_name = os.getenv("APP_NAME", "agents")
    app = FastAPI(title=service_name)
    start_time = datetime.now(timezone.utc)
    hostname = socket.gethostname()
    llm_client = _init_llm()

    @app.get("/health")
    def health():
        now = datetime.now(timezone.utc)
        return {
            "status": "ok",
            "name": service_name,
            "hostname": hostname,
            "time": now.isoformat(),
            "uptime_seconds": (now - start_time).total_seconds(),
            "llm_connected": bool(llm_client is not None),
        }

    @app.post("/agents/plan")
    def plan(payload: Dict[str, Any]):
        """
        Составляет план изменений от имени заданной роли.
        payload: {"role": AgentRole, "objective": str, "context": {...}}
        """
        role = payload.get("role")
        objective = payload.get("objective")
        if not role or not objective:
            raise HTTPException(status_code=400, detail="role and objective are required")
        # Заглушка: в реальности используем LLM для генерации плана
        if llm_client:
            # Здесь можно вызвать gpt-5 (модели нового поколения) при наличии доступа.
            # client.chat.completions.create(...)
            pass
        return {
            "role": role,
            "objective": objective,
            "plan": [
                "Создать ветку",
                "Внести изменения в код",
                "Запустить тесты",
                "Открыть PR и запросить ревью Risk/QA/Critic",
            ],
        }

    @app.post("/agents/propose_code_change")
    def propose_code_change(payload: Dict[str, Any]):
        """
        Принимает предложение изменения кода от агента (например, новой стратегии),
        сохраняет артефакт предложения и возвращает шаги. Реальное применение кода — через CI/CD
        и ручное подтверждение или доверенную автоматизацию.
        payload: {"role": AgentRole, "title": str, "diff": str, "rationale": str}
        """
        role = payload.get("role")
        title = payload.get("title")
        diff = payload.get("diff")
        if not role or not title or not diff:
            raise HTTPException(status_code=400, detail="role, title and diff are required")
        # В реальном пайплайне: сохранить diff как артефакт, создать ветку/PR через GitHub API.
        return {
            "message": "proposal accepted",
            "role": role,
            "title": title,
            "actions": [
                "Создать feature-ветку",
                "Применить diff и запустить тесты",
                "Открыть PR, запросить ревью (risk, qa, critic)",
            ],
        }

    @app.post("/agents/restart_service")
    def restart_service(payload: Dict[str, Any]):
        """
        Запрос на перезапуск сервиса (используется DevOps-агентом после деплоя или изменения конфигурации).
        payload: {"service": str}
        """
        service = payload.get("service")
        allowed_services = {
            "market-data", "strategy-engine", "order-executor",
            "risk", "backtester", "agents", "ui",
        }
        if service not in allowed_services:
            raise HTTPException(status_code=400, detail="unknown service")
        # В реальном окружении: дернуть CI/CD job или docker compose restart в контролируемой среде
        return {"message": f"restart scheduled for {service}"}

    return app