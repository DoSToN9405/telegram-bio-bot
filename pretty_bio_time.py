from telethon import TelegramClient, functions
from telethon.sessions import StringSession
import asyncio
from datetime import datetime

# Список русских месяцев и дней недели
months = ['Января', 'Февраля', 'Марта', 'Апреля', 'Мая', 'Июня',
          'Июля', 'Августа', 'Сентября', 'Октября', 'Ноября', 'Декабря']
days = ['Понедельник', 'Вторник', 'Среда', 'Четверг',
        'Пятница', 'Суббота', 'Воскресенье']

# 🔐 Вставь сюда свои данные
api_id = 15364852
api_hash = 'a1eeff361f5291563a80b0bfe9aeb638'
session_string = '1ApWapzMBu5_IMiZh5dMQQO3r7UA6ezoNWX46IoB8zCD9khIFK5GlKFQO81TkLkSHdF2sJYROg-N7Lj6ofxRlKfGjM4xbEOR6sqyAm8NG3vUj2OIXM7-4v9Ac5uJ9a7phd4rTbRC06g2tEYxijdNZ84qeKVjTSbZwG_AEBUgznPNYPJrnAvDq4vXoWobJ0_dbNvYFTuwiCY_VKCW2oQIZVd928oaHvKyoTUNTXM-OHI2MxxuUFVkKV9cG8arn4pH7QkZ6WrAKc-Y1Uav9ZGjPH1noSCwpM8CFvYqghN4PBBRtDsYApHKMjmuREs-wSp93xAsspj7JLT11PVC1Pgv_H3j2AY38t10='

# Создаём клиента с использованием StringSession
client = TelegramClient(StringSession(session_string), api_id, api_hash)

# Функция приветствия по времени суток
def get_greeting(hour):
    if 5 <= hour < 12:
        return "🌅 Доброе утро!"
    elif 12 <= hour < 18:
        return "🌤 Добрый день!"
    elif 18 <= hour < 23:
        return "🌇 Добрый вечер!"
    else:
        return "🌙 Спокойной ночи!"

# Главная асинхронная функция для обновления био
async def update_bio():
    await client.start()
    while True:
        now = datetime.now()
        hour = now.hour
        greeting = get_greeting(hour)
        time_now = now.strftime("%H:%M")
        date_str = f"{now.day} {months[now.month - 1]} ({days[now.weekday()]})"
        bio = f"{greeting}\n⏰ {time_now} | {date_str}"

        try:
            await client(functions.account.UpdateProfileRequest(about=bio))
            print(f"Bio обновлено:\n{bio}\n")
        except Exception as e:
            print(f"Ошибка при обновлении био: {e}")

        await asyncio.sleep(60)

# Запуск клиента
with client:
    client.loop.run_until_complete(update_bio())
