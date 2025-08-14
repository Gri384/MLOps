## Эндпоинты сервисов

Базовый формат: `http://localhost:<порт>`

### market-data (порт 8001)
- `GET /health` — статус сервиса
- `GET /` — краткое сообщение
- `GET /klines` — свечи Binance Testnet
  - Параметры: `symbol` (обяз.), `interval` (по умолчанию `1m`), `limit` (1–1000, по умолчанию 100)
  - Пример:
    ```bash
    curl "http://localhost:8001/klines?symbol=BTCUSDT&interval=1m&limit=5"
    ```

### strategy-engine (порт 8002)
- `GET /health` — статус сервиса
- `GET /` — заглушка

### order-executor (порт 8003)
- `GET /health` — статус сервиса
- `GET /` — заглушка

### risk (порт 8004)
- `GET /health` — статус сервиса
- `GET /` — заглушка

### backtester (порт 8005)
- `GET /health` — статус сервиса
- `GET /` — заглушка

### agents (порт 8006)
- `GET /health` — статус сервиса
- `GET /` — заглушка

### ui (порт 3000)
- Статическая страница со ссылками на `/health` всех сервисов