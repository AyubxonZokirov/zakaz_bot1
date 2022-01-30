from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

asosiy_buttonlar = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='ОФОРМИТЬ ЗАКАЗ 💰💳')
        ],
        [
            KeyboardButton(text='ОТЗЫВЫ 🍚')
        ],
        [
            KeyboardButton(text='ПОДДЕРЖКА👨‍💻')
        ]
    ], resize_keyboard=True
)
otmena_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🚫 Отмена')
        ],
    ], resize_keyboard=True
)
oplata_button = ReplyKeyboardMarkup(
    keyboard=[
        [
           KeyboardButton(text='ОПЛАТИТЬ ЗАКАЗ 👍🎁')
        ],
        [
            KeyboardButton(text='🚫 Отмена')
        ]
    ], resize_keyboard=True
)
