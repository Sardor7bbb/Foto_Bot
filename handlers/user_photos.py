from aiogram import types
from aiogram.dispatcher import FSMContext

from load import dp, db


@dp.message_handler(text="Rasim Joylash")
async def get_photos(message: types.Message, state: FSMContext):
    photo = db.get_photo_id(chat_id=message.chat.id)
    if photo:
        await message.answer_photo(photo=photo[0][2])
        text = "Rasim mavjud"
    else:
        text = "Iltimos yoqtirgan rasmingizni yuboring: "
        await state.set_state("update_user_photos")
    await message.answer(text=text)


@dp.message_handler(state="update_user_photos", content_types=types.ContentTypes.PHOTO)
async def get_photos(message: types.Message, state: FSMContext):
    await state.update_data(photo_id=message.photo[-1].file_id, chat_id=message.chat.id)
    data = await state.get_data()
    if db.update_photos_id(data):
        text = "Rasim qoshildi "
    else:
        text = "Rasim qoshilmadi "
    await message.answer(text=text)
    await state.set_state("update_user_photos")
