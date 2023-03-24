from enum import Enum

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


class ChatButtons(Enum):
    generate_image: str = "Генерация изображения 🖼️"
    generate_text: str = "Генерация текста 📝"
    generate_code: str = "Генерация кода 💻"
    edit_image: str = "Редактирование фото ️🖼️"


# Главное меню Inline
MAIN_MENU = InlineKeyboardMarkup()

for button in ChatButtons:
    MAIN_MENU.add(InlineKeyboardButton(callback_data=button.name, text=button.value))
