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

## Перезапуск докера

```bash
docker stop discord-telegram-bot
docker rm discord-telegram-bot
```

```bash
docker build -t discord-telegram-bot .
```

```bash
sudo systemctl daemon-reexec
sudo systemctl daemon-reload
sudo systemctl enable discord-telegram-bot
sudo systemctl start discord-telegram-bot
```

Проверяем работоспособность
```bash
sudo systemctl status discord-telegram-bot
sudo journalctl -u discord-telegram-bot -f
```