## Конфигурация и переменные окружения

Используйте `.env` (на основе `.env.example`). Не коммитьте реальные ключи.

### Инфраструктура
- `POSTGRES_DB` — имя БД (по умолчанию: `trading`)
- `POSTGRES_USER` — пользователь БД (по умолчанию: `trader`)
- `POSTGRES_PASSWORD` — пароль БД (по умолчанию: `trader_password`)
- `POSTGRES_PORT` — порт публикации Postgres (по умолчанию: `5432`)
- `REDIS_PORT` — порт Redis (по умолчанию: `6379`)
- `NATS_PORT` — порт NATS (по умолчанию: `4222`)
- `NATS_MONITOR_PORT` — порт мониторинга NATS (по умолчанию: `8222`)

### Binance Testnet
- `BINANCE_API_KEY` — API ключ Testnet (опционально для публичных GET)
- `BINANCE_API_SECRET` — секретный ключ Testnet
- `BINANCE_REST_BASE` — REST базовый URL (по умолчанию: `https://testnet.binance.vision`)
- `BINANCE_WS_BASE` — WS базовый URL (по умолчанию: `wss://testnet.binance.vision`)

### Приложение
- `ENV` — окружение (`development`/`staging`/`production`), по умолчанию: `development`
- `LOG_LEVEL` — уровень логирования (`DEBUG`/`INFO`/`WARNING`/`ERROR`), по умолчанию: `INFO`

Изменения переменных требуют перезапуска сервисов.

### Интеграции LLM
- `OPENAI_API_KEY` — ключ доступа к OpenAI (для работы агентов с GPT‑5). Если не задан, агенты работают без LLM.