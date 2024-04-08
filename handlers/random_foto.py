from aiogram.dispatcher import FSMContext

from keyboards.inline.like_dislike import like_dislike_def
from load import dp, db
from aiogram import types

@dp.message_handler(text="Rasimlar")
async def get_random_foto(message: types.Message, state: FSMContext):
    data = await state.get_data()
    print(data)
    photo = db.get_random_foto_id(message.chat.id)
    if photo is False:
        text = "Hamma rasmlarni ko'rib bo'ldingiz"
        await message.answer(text=text)
    else:
        print(data)
        if photo:
            await state.update_data(photo_id=photo[0])
            likes, dislikes = db.get_foto_likes(photo_id=photo[0])
            likes = likes[0][0]
            dislikes = dislikes[0]
            await message.answer_photo(photo=photo[2], reply_markup=await like_dislike_def(likes, dislikes, photo[0]))
        else:
            text = "Aktiv rasim mavjud emas"
            await message.answer(text=text)
