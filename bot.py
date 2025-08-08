import discord
import requests
import os
from dotenv import load_dotenv

load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

intents = discord.Intents.default()
intents.voice_states = True
intents.members = True

client = discord.Client(intents=intents)

def send_telegram_message(text):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": TELEGRAM_CHAT_ID, "text": text})

@client.event
async def on_ready():
    print(f"Logged in as {client.user.name}")

@client.event
async def on_voice_state_update(member, before, after):
    if before.channel is None and after.channel is not None:
        message = f"{member.display_name} зашел в голосовой канал '{after.channel.name}'. Количество челиков: {len(after.channel.members)}"
        print(message)
        send_telegram_message(message)

client.run(DISCORD_TOKEN)
