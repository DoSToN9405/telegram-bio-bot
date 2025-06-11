GNU nano 8.4              pretty_bio_time.py
from telethon import TelegramClient, functions
import asyncio
from datetime import datetime

# Russian months and weekdays
months = ['Января', 'Февраля', 'Марта', 'Апреля', 'Мая', 'Июня',
          'Июля', 'Августа', 'Сентября', 'Октября', 'Ноября', 'Декабря>
days = ['Понедельник', 'Вторник', 'Среда', 'Четверг',
        'Пятница', 'Суббота', 'Воскресенье']

# Your Telegram API credentials
api_id = 15364852
api_hash = 'a1eeff361f5291563a80b0bfe9aeb638'
session_name = 'my_session'

client = TelegramClient(session_name, api_id, api_hash)

def get_greeting(hour):
    if 5 <= hour < 12:
        return "🌅 Доброе утро!"
    elif 12 <= hour < 18:
        return "🌤 Добрый день!"
    elif 18 <= hour < 23:
        return "🌇 Добрый вечер!"
    else:
        return "🌙 Спокойной ночи!"

async def update_bio():
    await client.start()
    while True:
        now = datetime.now()
        hour = now.hour
        greeting = get_greeting(hour)
        time_now = now.strftime("%H:%M")
        date_str = f"{now.day} {months[now.month - 1]} ({days[now.week>
        bio = f"{greeting}\n⏰ {time_now} | {date_str}"

        try:
            await client(functions.account.UpdateProfileRequest(about=>
            print(f"Bio updated:\n{bio}\n")
        except Exception as e:
            print(f"Error updating bio: {e}")

        # Wait 60 seconds (adjust as needed)
        await asyncio.sleep(60)

# Run the client
with client:
    client.loop.run_until_complete(update_bio())
