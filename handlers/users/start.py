from aiogram import types
import sqlite3
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.asosiy_menyu import asosiy_buttonlar

from loader import dp, db


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    name = message.from_user.first_name
    try:
        db.add_user(id=message.from_user.id, name=name)
    except sqlite3.IntegrityError as err:
        pass
    await message.answer(f"Hydra Marketing приветствует Вас, желаем хороших покупок и ровных подъёмов💥")
    await message.answer(f"🔝 Главное Меню", reply_markup=asosiy_buttonlar)

@dp.message_handler(text="ОТЗЫВЫ 🍚")
async def otziv(message: types.Message):
    await message.answer(text=f"Отзывы: @PrimaryDreams")

@dp.message_handler(text="ПОДДЕРЖКА👨‍💻")
async def tex_poderjka(message: types.Message):
    await message.answer(text="Тех.поддержка: @PrimaryDreams")
