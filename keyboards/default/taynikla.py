from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

razgavor_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Тайник')
        ],
        [
            KeyboardButton(text='Магнит')
        ],
        [
            KeyboardButton(text='🚫 Отменаㅤ')
        ]
    ], resize_keyboard=True
)