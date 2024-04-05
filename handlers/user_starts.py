from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.default.defoult import button
from load import dp, db
from status.users import RegisterState


@dp.message_handler(commands='start')
async def start(message: types.Message):
    if db.get_user_chat_id(chat_id=message.chat.id):
        text = "Assalomu Alekum 👋"
        await message.answer(text=text, reply_markup=button)
    else:
        text = "Assalomu Alekum ismingizni kiriting 📝 "
        await message.answer(text=text)
        await RegisterState.full_name.set()


@dp.message_handler(state=RegisterState.full_name)
async def get_full_name(message: types.Message, state: FSMContext):
    await state.update_data(full_name=message.text, chat_id=message.chat.id)
    text = "Telefon raqamingizni kiriting ☎️ "
    await message.answer(text=text)
    await RegisterState.phone_number.set()


@dp.message_handler(state=RegisterState.phone_number)
async def get_phone_number(message: types.Message, state: FSMContext):
    await state.update_data(phone_number=message.text)
    text = "Manzilni kiriting📍 "
    await message.answer(text=text)
    await RegisterState.location_name.set()


@dp.message_handler(state=RegisterState.location_name)
async def get_location(message: types.Message, state: FSMContext):
    await state.update_data(location_name=message.text)
    data = await state.get_data()
    print(data)
    if db.add_user_chat(data):
        text = "Saccsessfully register ✅"
        await message.answer(text=text, reply_markup=button)
    else:
        text = "Bot problems 🛠"
    await message.answer(text=text)
    await state.finish()
