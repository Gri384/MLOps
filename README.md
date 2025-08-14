# Binance Multi-Agent Trading Bot (Monorepo)

Многоагентная платформа для разработки и эксплуатации торгового бота под Binance Spot Testnet, ориентированная на безопасную разработку, бэктесты и постепенный выход в прод.

## Сервисы
- market-data: подписки на маркет-данные (скелет)
- strategy-engine: исполнение стратегий (скелет)
- order-executor: отправка ордеров (скелет)
- risk: риск-правила и лимиты (скелет)
- backtester: бэктест-движок API (скелет)
- agents: координация ролей агентов (скелет)
- ui: статический UI-заглушка
- infra: Postgres, Redis, NATS (вырезаем Kafka для простоты)

## Быстрый старт
1. Скопируйте переменные окружения:
   ```bash
   cp .env.example .env
   ```
2. (Опционально) Отредактируйте ключи Binance Testnet в `.env`.
3. Соберите и запустите:
   ```bash
   docker compose up -d --build
   ```
4. Проверки здоровья (после запуска):
   - Market Data: `http://localhost:8001/health`
   - Strategy Engine: `http://localhost:8002/health`
   - Order Executor: `http://localhost:8003/health`
   - Risk: `http://localhost:8004/health`
   - Backtester: `http://localhost:8005/health`
   - Agents: `http://localhost:8006/health`
   - UI: `http://localhost:3000`

## Стандартные переменные окружения
Смотрите `.env.example`. По умолчанию используется Spot Testnet.

## Разработка
- Каждая служба — изолированный Python-проект (FastAPI) или статический UI.
- Общение между сервисами предполагается через NATS/HTTP, но в MVP реализованы только HTTP health-эндоинты.

## Документация
- Руководство пользователя: `docs/USER_GUIDE.md`
- Запуск: `docs/RUN.md`
- Конфигурация: `docs/CONFIG.md`
- Эндпоинты: `docs/ENDPOINTS.md`
- Устранение неполадок: `docs/TROUBLESHOOT.md`
- Безопасность: `docs/SECURITY.md`
- Агенты и процесс: `docs/AGENTS.md`

## Безопасность
- Не используйте реальные ключи в `.env`. Начинайте с Testnet/paper.

## Лицензия
MIT (или выберите вашу).