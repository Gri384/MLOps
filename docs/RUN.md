## Запуск и управление

### Docker Compose
- Запуск (с пересборкой при необходимости):
  ```bash
  docker compose up -d --build
  ```
- Просмотр логов:
  ```bash
  docker compose logs -f --tail=200
  ```
- Остановка и удаление томов:
  ```bash
  docker compose down -v
  ```
- Перезапуск одного сервиса:
  ```bash
  docker compose up -d --build market-data
  ```

### Makefile
Доступные цели:
- `make up` — `docker compose up -d --build`
- `make down` — `docker compose down -v`
- `make build` — `docker compose build`
- `make logs` — хвост логов всех сервисов
- `make ps` — статус контейнеров
- `make health` — быстрые проверки `/health`

### Локальный запуск без Docker
1. Виртуальное окружение:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```
2. Зависимости:
   ```bash
   pip install -r requirements-dev.txt \
       -r services/market_data/requirements.txt \
       -r services/strategy_engine/requirements.txt \
       -r services/order_executor/requirements.txt \
       -r services/risk/requirements.txt \
       -r services/backtester/requirements.txt \
       -r services/agents/requirements.txt
   ```
3. Запуск всех сервисов:
   ```bash
   chmod +x scripts/dev_run.sh
   ./scripts/dev_run.sh
   ```
4. Остановка: `Ctrl+C`

### Порты по умолчанию
- market-data: 8001
- strategy-engine: 8002
- order-executor: 8003
- risk: 8004
- backtester: 8005
- agents: 8006
- ui: 3000 (только при Docker)

Изменение портов — через `docker-compose.yml` или переменные окружения сервиса.