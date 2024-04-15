from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData

user_like_data = CallbackData('like', 'action', 'photo_id')
user_dislike_data = CallbackData('dislike', 'action', 'photo_id')


async def like_dislike_def(like, dislike, photo_id):
    like_button = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text=f"{like} 👍", callback_data=user_like_data.new(action="like", photo_id=photo_id)),
                InlineKeyboardButton(text=f"{dislike} 👎", callback_data=user_dislike_data.new(action="dislike", photo_id=photo_id))
            ]
        ]
    )
    return like_button


async def follow_button_def(chat_id):
    follow_button = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text=f"Follow ", callback_data=chat_id)
            ]
        ]
    )
    return follow_button


async def yes_or_no(chat_id):
    yes_or_no_button = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text=f"Yes", callback_data=chat_id),
                InlineKeyboardButton(text=f"No", callback_data=chat_id),
            ]
        ]
    )
    return yes_or_no_button
