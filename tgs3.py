
from time import sleep
from pyrogram import Client, filters, types
from PIL import Image
import re
import asyncio

app = Client('session', api_id='25324742', api_hash='650234935921ca514f04bf733af430e1')

chat_id = "@datinganon_bot"

@app.on_message(chat_id)
async def spam(client: Client, message: types.Message):
    if "Вам найден собеседник, начинайте диалог." in message.text:  # Меняем это значение если хотим спамить в другом чате
        sleep(1.3)
        await app.send_message(chat_id, "Приветик, хочешь трахаться? я очень)")
        sleep(1.5)
        await app.send_message(chat_id, "тут я кончила 18 раз от руки хочешь посмотреть?) https://t.me/shoriof  ")

        if 'Вам найден собеседник, начинайте диалог.' in message.text:
             sleep(1.5)
             await app.send_sticker(chat_id, "CAACAgIAAxkBAAEHimRj2kEWCMHcI883ffJ3kFbpijS7NgAC5yQAAgTbuErwHbfUyBhwFi4E")
             sleep(1.5)

             if "Вам найден собеседник, начинайте диалог."  in message.text:  # Меняем это значение если хотим спамить в другом чате
                 await app.send_message(chat_id, "/stop")
                 sleep(1.3)
                 await app.send_message(chat_id, "Найти собеседника 🔍")

app.run()
