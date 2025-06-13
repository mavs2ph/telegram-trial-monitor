import time
import requests
from datetime import datetime, timedelta
from telegram import Bot

# Get your Telegram bot token and your Telegram user ID
BOT_TOKEN = "YOUR_BOT_TOKEN"
YOUR_TELEGRAM_ID = "YOUR_TELEGRAM_ID"

# Short.io settings
SHORTIO_API_KEY = "YOUR_SHORTIO_API_KEY"
LINK_DOMAIN = "yourdomain.short.io"  # e.g. "abc123.short.gy"

# Replace with actual links + usernames later
trial_users = [
    {"username": "@testuser", "start_time": datetime.utcnow(), "link": "https://yourlink.short.io/xyz123"}
]

bot = Bot(BOT_TOKEN)

while True:
    now = datetime.utcnow()
    for user in trial_users:
        elapsed = now - user["start_time"]
        if elapsed >= timedelta(hours=1):
            bot.send_message(chat_id=YOUR_TELEGRAM_ID, text=f"⏰ 1 hour done: Remove {user['username']}")
            trial_users.remove(user)
    time.sleep(30)
