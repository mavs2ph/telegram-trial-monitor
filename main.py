import time
import os
import requests
from datetime import datetime, timedelta
from telegram import Bot

# Securely load credentials from environment variables
BOT_TOKEN = os.getenv("BOT_TOKEN")
YOUR_TELEGRAM_ID = os.getenv("YOUR_TELEGRAM_ID")
SHORTIO_API_KEY = os.getenv("SHORTIO_API_KEY")
LINK_DOMAIN = os.getenv("LINK_DOMAIN")  # e.g. abc123.short.gy

# Sample list of trial users (fill in with real ones dynamically if needed)
trial_users = [
    {
        "username": "@testuser",
        "start_time": datetime.utcnow(),
        "link": f"https://{LINK_DOMAIN}/xyz123"
    }
]

bot = Bot(BOT_TOKEN)

while True:
    now = datetime.utcnow()
    for user in trial_users[:]:  # use a copy of the list to safely remove inside loop
        elapsed = now - user["start_time"]
        if elapsed >= timedelta(hours=1):
            bot.send_message(
                chat_id=YOUR_TELEGRAM_ID,
                text=f"⏰ 1 hour done: Remove {user['username']}"
            )
            trial_users.remove(user)
    time.sleep(30)

