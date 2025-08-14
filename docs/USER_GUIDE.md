## Обзор
Многоагентная платформа для безопасной разработки и эксплуатации торгового бота под Binance Spot Testnet. Состоит из набора сервисов (FastAPI) и статического UI. На старте доступны health-эндпоинты и REST-прокси свечей `/klines` в `market-data`.

Внимание: это не финансовый совет. Начинайте только с Testnet/paper и соблюдайте риск-лимиты.

## Требования
- Docker и Docker Compose (рекомендуется) ИЛИ Python 3.11+ и `uvicorn` для локального запуска без Docker
- Опционально: ключи Binance Spot Testnet

## Быстрый старт (Docker)
1. Скопируйте переменные окружения:
   ```bash
   cp .env.example .env
   ```
2. (Опционально) Укажите ключи Testnet в `.env`.
3. Запустите инфраструктуру и сервисы:
   ```bash
   docker compose up -d --build
   ```
4. Проверьте работу сервисов:
   - UI: `http://localhost:3000`
   - Health: `http://localhost:8001/health` ... `http://localhost:8006/health`

Остановить:
```bash
docker compose down -v
```

## Быстрый старт (без Docker)
1. Создайте виртуальное окружение:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```
2. Установите зависимости:
   ```bash
   pip install -r requirements-dev.txt \
       -r services/market_data/requirements.txt \
       -r services/strategy_engine/requirements.txt \
       -r services/order_executor/requirements.txt \
       -r services/risk/requirements.txt \
       -r services/backtester/requirements.txt \
       -r services/agents/requirements.txt
   ```
3. Запустите все сервисы:
   ```bash
   chmod +x scripts/dev_run.sh
   ./scripts/dev_run.sh
   ```
4. Откройте `http://localhost:8001/health` (и порты 8002–8006). UI в этом режиме не поднимается автоматически (можно открыть статический `services/ui/public/index.html` локально).

## Конфигурация
- Переменные окружения описаны в `docs/CONFIG.md`. Базовые значения — в `.env.example`.
- По умолчанию используется Binance Spot Testnet (`BINANCE_REST_BASE=https://testnet.binance.vision`).

## Как проверить получение свечей (Testnet)
Пример запроса к `market-data`:
```bash
curl "http://localhost:8001/klines?symbol=BTCUSDT&interval=1m&limit=5"
```
Ответ содержит массив свечей в формате Binance.

## Сервисы и эндпоинты
См. `docs/ENDPOINTS.md`.

## Типовые сценарии
- Проверить, что все сервисы живы:
  - Откройте UI `http://localhost:3000` и ссылками перейдите на `/health`
  - Или выполните: `make health`
- Получить свечи для бэктеста: запрос к `/klines`
- Подготовить .env и включить тестовые ключи — см. `docs/CONFIG.md`

## Обновления и рестарт
- Пересобрать и поднять: `docker compose up -d --build`
- Только пересобрать: `docker compose build`
- Перезапуск одного сервиса: `docker compose up -d --build market-data`

## Безопасность
- Не храните реальные ключи в репозитории. Используйте `.env` только локально.
- Подробнее см. `docs/SECURITY.md`.

## Частые проблемы
- Docker отсутствует или недоступен — используйте режим без Docker.
- Порты заняты — измените порты в `docker-compose.yml`.
- Ошибки сетевого доступа к Testnet — проверьте доступность `https://testnet.binance.vision`.
- Подробнее: `docs/TROUBLESHOOT.md`.

## Дальнейшие шаги
- Ознакомьтесь с `docs/AGENTS.md` — роли, процесс и план развития.
- Настройте ключи Testnet и выполните пробные запросы.
- Подготовьте свои стратегии (интерфейс будет добавлен в следующих релизах).