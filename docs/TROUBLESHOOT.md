## Устранение неполадок

### Docker не найден / не запускается
- Установите Docker Desktop (Windows/Mac) или Docker Engine + Compose (Linux)
- Проверьте: `docker --version`, `docker compose version`

### Порты заняты
- Измените порты в `docker-compose.yml`
- Либо остановите мешающие процессы

### Сервисы не поднимаются
- Посмотрите логи: `docker compose logs -f --tail=200`
- Убедитесь, что `.env` скопирован из `.env.example`

### Нет доступа к Testnet Binance
- Проверьте доступ к `https://testnet.binance.vision`
- Убедитесь, что параметры запроса корректны: символ, интервал, лимит

### Локальный запуск без Docker: проблемы с venv
- Установите пакет для venv в вашей ОС (например, Ubuntu: `sudo apt install python3-venv`)
- Создайте окружение заново: `python3 -m venv .venv && source .venv/bin/activate`

### `jq: command not found`
- Скрипты используют `curl`; `jq` не обязателен. Установите при желании.

### UI недоступен без Docker
- В локальном режиме UI не поднимается автоматически. Откройте `services/ui/public/index.html` в браузере или используйте Docker.

### Как проверить, что все работает?
- Health: `make health` или откройте ссылки из UI
- Klines: `curl "http://localhost:8001/klines?symbol=BTCUSDT&interval=1m&limit=2"`