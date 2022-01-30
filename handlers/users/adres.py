from aiogram import types
from keyboards.default.asosiy_menyu import otmena_button
from keyboards.default.maxsulotlar_button import maxsulot_buttonlar
from data.config import Admins
from aiogram.dispatcher.filters.builtin import CommandHelp
from loader import dp, db, bot

@dp.message_handler(text=('Hashish Isolator 1гр 1890₽','Hashish Isolator 2гр 3490₽','Marijuana GorillaGlue 1гр 1790₽','Marijuana GorillaGlue 2гр 3290₽','Mephedrone(Pacific)VHQ 1гр 2690₽','Mephedrone(Pacific)VHQ 2гр 4790₽','Ecstasy Barcelona 2шт 2090₽','Ecstasy Barcelona 3шт 2990₽','Alpha-pVp blue crystal 1гр 2490₽','Alpha-pVp blue crystal 2гр 4390₽','Amfetamin Premium 1гр 1390₽','Amfetamin Premium 2гр 2490₽',
                          'Лирика Pfizer 300мг 14шт 2290₽','Марки  LSD 250мг 2шт 2090₽','Марки  LSD 250мг 3шт 2990₽','Cocaine  VHQ FishScale 0.5г 6490₽','Cocaine  VHQ FishScale 0.5г 6490₽','Methadone VHQ 0.5гр 2890₽','Methadone VHQ 1гр 5190₽',"Heroine '999' 0.5гр 2690₽","Heroine '999' 1гр 4790₽"))
async def bot_adres(message: types.Message):
    msg = message.text
    msg_user = message.from_user.username
    for a in Admins:
        await bot.send_message(chat_id=a, text=f"{msg}\nОт @{msg_user}")
    await bot.send_message(chat_id=message.from_user.id, text=f"Напишите(район/улицу вашего города) \n По этим данным бот найдет ближайший, актуальный JPS адрес с координатами, фото и его описанием.\n \n Пример: \n Район Ленинский. \n Улица Пушкина. \n \n *Если вы не указываете желаемое территориальное местоположение клада, или даете ложные придуманные районы улицы то адрес будет выбран ботом автоматически в указанном вами городе ", reply_markup=otmena_button)

@dp.message_handler(text='🚫 Отмена')
async def bot_nazad(message: types.Message):

    await message.answer(f"🔝 Главное Меню", reply_markup=maxsulot_buttonlar)