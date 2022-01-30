from aiogram import types
from keyboards.default.taynikla import razgavor_button
from keyboards.default.asosiy_menyu import asosiy_buttonlar,oplata_button,otmena_button
from aiogram.dispatcher.filters.builtin import CommandHelp
from data.config import Admins
from loader import dp, db, bot


@dp.message_handler(text=('Тайник','Магнит'))
async def bot_vibor(message: types.Message):

    await message.answer(f"Следуя пошаговой инструкции процесс взаимодействия с нашим магазинов принесет Вам только положительные эмоции и гарантированный результат успешных покупок! \n \
========================== \n \n 1. Выберите способ оплаты (QIWI Wallet или с помощью банковской карты(к оплате принимается любой банк мира - например Сбер, ВТБ, АльфаБанк и тд) \n \
2. Предоставьте фотогорафию чека боту или ваш никнейм в телеграм боту, для проверки платежа. 3. Ожидайте! Проверка займет 5-10 минут, после чего бот вышлет Вам точные гео-координаты, адрес, фотографии и инструкцию, полностью описывающая Ваш клад. \n \n \
➖➖➖➖➖➖➖➖➖➖➖➖➖ \n VISA QIWI WALLET \n \n +7 963 393-97-84 \n \n *Комментарии к платежу не оставлять! После оплаты предоставить фотографию чека! \n \n \
➖➖➖➖➖➖➖➖➖➖➖➖➖ \n КАРТА \n \n 4890 4947 8783 8846 \n \n *Выбрать «Перевод в другой банк» \n Комментарии к платежу не оставлять! После оплаты предоставить фотографию чека! \n ", reply_markup=oplata_button)

@dp.message_handler(text='ОПЛАТИТЬ ЗАКАЗ 👍🎁')
async def bot_oplata(message: types.Message):

    await message.answer(f"После поступления средств бот автоматически выдаст адрес и координаты с фото описанием.По завершению операции отправьте БОТУ скриншот об оплате или ник в телеграм.\n \
Приятного время проведения🖐️", reply_markup=otmena_button)

@dp.message_handler(content_types=['photo'])
async def bot_scren(message: types.Message):
    await message.photo[-1].download()
    user = message.from_user.username
    imgid = message.photo[-1].file_id
    for a in Admins:
        await bot.send_photo(chat_id=a, photo=imgid, caption=f"От @{user}")
    await message.answer(f"Выполняется проверка. В случае успешного подтверждения платежа Вы получите сообщение о зачислении в течении 3х минут.", reply_markup=otmena_button)

@dp.message_handler(text='🚫 Отменаㅤ')
async def bot_nazad3(message: types.Message):

    await message.answer(f"🔝 Главное Меню", reply_markup=asosiy_buttonlar)

@dp.message_handler(content_types=['text'])
async def bot_adres2(message: types.Message):
    user = message.from_user.username
    for a in Admins:
        await bot.send_message(chat_id=a, text=f"{message.text}\nОт @{user}")
    await message.answer(f"Выберите вид тайника🧊", reply_markup=razgavor_button)