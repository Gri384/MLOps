SHELL := /usr/bin/bash

.PHONY: up down build logs ps health

up:
	docker compose up -d --build

down:
	docker compose down -v

build:
	docker compose build

logs:
	docker compose logs -f --tail=200

ps:
	docker compose ps

health:
	@echo "Checking health endpoints";
	@curl -sf http://localhost:8001/health | jq . || true;
	@curl -sf http://localhost:8002/health | jq . || true;
	@curl -sf http://localhost:8003/health | jq . || true;
	@curl -sf http://localhost:8004/health | jq . || true;
	@curl -sf http://localhost:8005/health | jq . || true;
	@curl -sf http://localhost:8006/health | jq . || true;