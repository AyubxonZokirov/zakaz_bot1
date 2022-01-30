from aiogram import types
from loader import dp, db, bot
from data.config import Admins

# Add Baza bot
@dp.message_handler(commands="baza")
async def bot_baza(message: types.Message):
    db.create_table_users()
    await message.answer(text="Baza yaratildi")

# Print_User bot
@dp.message_handler(commands="print_users")
async def bot_baza(message: types.Message):
    allusers = db.select_all_users()
    if message.from_user.id not in Admins:
        return
    total_count_text = f"Umumiy foydalanuvchilar soni: {len(allusers)}"
    text = f"{total_count_text}"
    await bot.send_message(chat_id=message.from_user.id, text=text)


# Echo bot
# @dp.message_handler(state=None)
# async def bot_echo(message: types.Message):
#     await message.answer(message.text)
