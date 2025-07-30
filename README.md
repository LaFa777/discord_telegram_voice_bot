# Discord ➜ Telegram Voice Bot

Бот отслеживает вход пользователей в голосовой чат Discord и отправляет уведомления в Telegram.

## Установка

1. Установи зависимости:
```bash
uv pip install -r requirements.txt
```

## Запуск через докер
```bash
docker build -t discord-telegram-bot .
```
```bash
docker run -d \
  --name discord-telegram-bot \
  --env-file .env \
  --restart unless-stopped \
  discord-telegram-bot
```