
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Rasimlar"),
            KeyboardButton(text="Rasim Joylash"),
        ],
        [
            KeyboardButton(text="Menyu")
        ]
    ], resize_keyboard=True
)

