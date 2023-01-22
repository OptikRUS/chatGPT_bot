from enum import Enum

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


class ChatButtons(Enum):
    generate_image: str = "Generate image"
    get_answer: str = "Get answer"
    generate_code: str = "Generate code"


# Главное меню Inline
MAIN_MENU = InlineKeyboardMarkup()

for button in ChatButtons:
    MAIN_MENU.add(InlineKeyboardButton(button.value, callback_data=button.name))
