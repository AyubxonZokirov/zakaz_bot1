from aiogram import types
from keyboards.default.zakaz_bersh import zakaz_buttonlar
from keyboards.default.asosiy_menyu import asosiy_buttonlar
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(text='ОФОРМИТЬ ЗАКАЗ 💰💳')
async def bot_zakaz(message: types.Message):

    await message.answer(f"ВЫБЕРИТЕ ВАШ ГОРОД🌆", reply_markup=zakaz_buttonlar)


@dp.message_handler(text='🔙 Назад')
async def bot_nazad(message: types.Message):

    await message.answer(f"🔝 Главное Меню", reply_markup=asosiy_buttonlar)

@dp.message_handler(text='🔝 Главное Меню')
async def bot_glavniy(message: types.Message):

    await message.answer(f"🔝 Главное Меню", reply_markup=asosiy_buttonlar)
