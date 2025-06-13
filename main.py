import os
import time
import requests
from datetime import datetime, timedelta
from telegram import Bot

# Load sensitive data from environment variables
BOT_TOKEN = os.environ.get("BOT_TOKEN")
YOUR_TELEGRAM_ID = os.environ.get("YOUR_TELEGRAM_ID")
SHORTIO_API_KEY = os.environ.get("SHORTIO_API_KEY")
LINK_DOMAIN = os.environ.get("LINK_DOMAIN")  # e.g. MJWnsk.short.gy

bot = Bot(BOT_TOKEN)

# Example trial user list (you can update this dynamically later)
trial_users = [
    {
        "username": "@testuser",  # Replace with actual usernames
        "start_time": datetime.utcnow(),
        "link": f"https://{LINK_DOMAIN}/your-short-link"
    }
]

# Monitor trial users
while True:
    now = datetime.utcnow()
    for user in trial_users[:]:  # Iterate over a copy to allow safe removal
        elapsed = now - user["start_time"]
        if elapsed >= timedelta(hours=1):
            bot.send_message(
                chat_id=YOUR_TELEGRAM_ID,
                text=f"⏰ 1 hour done: Remove {user['username']} - {user['link']}"
            )
            trial_users.remove(user)
    time.sleep(30)
