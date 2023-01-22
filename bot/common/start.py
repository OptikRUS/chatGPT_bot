from aiogram.types import Message

from bot.keyboards import MAIN_MENU
from ..chat.constants import MAIN_MENU_MESSAGE


async def send_main_menu(message: Message):
    await message.bot.send_message(chat_id=message.chat.id, text=MAIN_MENU_MESSAGE, reply_markup=MAIN_MENU)
