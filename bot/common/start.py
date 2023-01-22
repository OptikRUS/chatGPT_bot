from aiogram.types import Message

from bot.keyboards import MAIN_MENU


async def send_main_menu(message: Message):
    await message.bot.send_message(chat_id=message.chat.id, text="Main menu:", reply_markup=MAIN_MENU)
