from aiogram import types
from keyboards.default.maxsulotlar_button import maxsulot_buttonlar
from keyboards.default.asosiy_menyu import asosiy_buttonlar
from keyboards.default.zakaz_bersh import zakaz_buttonlar
from aiogram.dispatcher.filters.builtin import CommandHelp
from loader import dp

@dp.message_handler(text=('Альметьевск','Анапа','Артем','Александров','Архенгельск','Асбест',
                          'Астрахань','Ачинск','Балашиха','Балашов','Барнаул','Батайск','Белгород',
                          'Белово','Белогорск(Амурская обл)','Белорецк','Белореченск','Бердск','Березники',
                          'Березовский(Сврдл обл)','Бийск','Биробиджан','Благовещенск (Амурская обл)',
                          'Борисоглебск','Боровичи','Братск','Брянск','Бугульма','Буденновск','Бузулук',
                          'Великие Луки','Великий Новгород','Верхняя Пышма','Видное','Владивосток',
                          'Владикавказ','Владимир','Волгоград','Волгодонск','Волжск','Вологда','Волжский',
                          'Вольск','Воркута','Воскресенск','Воткинск','Всеволожск','Выборг','Вязьма','Гатчина',
                          'Георгиевск','Горно-Алтайскv','Губкин','Гуково','Густь-Хрустальный','Дербент',
                          'Дзержинск','Димитровград','Дмитров','Долгопрудный','Донской','Дубна','Евпатория',
                          'Егорьевск','Ейск','Екатеринбург','Елабуга','Елец','Ессентуки','Железногорск(Красноя край)',
                          'Железногорск (Курская обл)','Жигулевск','Жуковский','Заречный','Зеленогорск','Зеленодольск',
                          'Златоуст','Иваново','Ивантеевка','Ижевск','Избербаш','Иркутск','Искитим','Ишим',
                          'Ишимбай','Йошкар-Ола','Казань','Калининград','Калуга','Каменск- Уральский','Каменск - Шахтинский',
                          'Камышин','Канск','Каспийск'))
async def bot_maxsulot(message: types.Message):

    await message.answer(f"Выберите товар и его количество", reply_markup=maxsulot_buttonlar)


@dp.message_handler(text='🔙 Назадㅤ')
async def bot_nazad2(message: types.Message):

    await message.answer(f"🔝 Меню", reply_markup=zakaz_buttonlar)

@dp.message_handler(text='🔝 Главное Меню')
async def bot_glavniy2(message: types.Message):

    await message.answer(f"🔝 Главное Меню", reply_markup=asosiy_buttonlar)