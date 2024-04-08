from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.default.defoult import button
from keyboards.inline.like_dislike import follow_button_def, yes_or_no
from load import dp, db, bot
from status.users import RegisterState


@dp.message_handler(text="Search 🔍")
async def user_search(message: types.Message, state: FSMContext):
    text = "User nameni kiriting: "
    await message.answer(text=text)
    await state.set_state("user_search")


@dp.message_handler(state="user_search")
async def get_user_search(message: types.Message, state: FSMContext):
    user = db.get_username(full_name=message.text)
    if user:
        text = f"{user[0][2]} topildi"
        await message.answer(text=text, reply_markup=await follow_button_def(chat_id=user[0][1]))
    else:
        text = "User not found"
        await message.answer(text=text)
    await state.finish()

@dp.callback_query_handler()
async def user_follow_button(call: types.CallbackQuery, state: FSMContext):
    user_chat_id = call.data
    chat_id = call.message.chat.id
    print(user_chat_id)
    print(chat_id)
    await bot.send_message(chat_id=user_chat_id, text=f"Ushbu foydalanuvchi sizga follow bosdi: {chat_id}", reply_markup=await yes_or_no(chat_id))
