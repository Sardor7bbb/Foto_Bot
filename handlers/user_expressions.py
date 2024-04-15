from aiogram.dispatcher import FSMContext

from keyboards.inline.like_dislike import like_dislike_def, user_dislike_data, user_like_data
from load import dp, db
from aiogram import types


@dp.callback_query_handler(text=user_like_data.filter(action='like'))
async def like_dislike_handler(call: types.CallbackQuery, callback_data: dict):
    photo_id = callback_data.get('photo_id')
    is_like = db.check_user_like(chat_id=call.message.chat.id, photo_id=int(photo_id))
    if is_like:
        db.user_delete_like(chat_id=call.message.chat.id, photo_id=int(photo_id))
        if is_like[3] is False:
            db.user_like(chat_id=call.message.chat.id, photo_id=photo_id, is_like=True)
    else:
        db.user_like(chat_id=call.message.chat.id, photo_id=photo_id, is_like=True)
    likes, dislikes = db.get_foto_likes(photo_id)
    likes = likes[0][0]
    dislikes = dislikes[0]
    await call.message.edit_reply_markup(reply_markup=await like_dislike_def(likes, dislikes, photo_id))


@dp.callback_query_handler(text=user_dislike_data.filter(action='dislike'))
async def dislike_handler(call: types.CallbackQuery, callback_data: dict):
    photo_id = callback_data.get('photo_id')
    is_like = db.check_user_like(chat_id=call.message.chat.id, photo_id=int(photo_id))
    if is_like:
        db.user_delete_like(chat_id=call.message.chat.id, photo_id=int(photo_id))
        if is_like[3] is True:
            db.user_like(chat_id=call.message.chat.id, photo_id=photo_id, is_like=False)

    else:
        db.user_like(chat_id=call.message.chat.id, photo_id=photo_id, is_like=False)
    likes, dislikes = db.get_foto_likes(photo_id)
    likes = likes[0][0]
    dislikes = dislikes[0]
    await call.message.edit_reply_markup(reply_markup=await like_dislike_def(likes, dislikes, photo_id))
