from aiogram import types
from load import dp, db


@dp.message_handler(commands='start')
async def start(message: types.Message):
    query = "CREATE TABLE pefw (id INTEGER PRIMARY KEY, username TEXT, password TEXT)"
    db.cursor.execute(query)
    db.connect.commit()
    text = "Assalomu Alekum"
    await message.answer(text=text)
