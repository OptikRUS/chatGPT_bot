from aiogram import Dispatcher

from .start import send_main_menu


def init_common_handlers(dp: Dispatcher):
    dp.register_message_handler(send_main_menu, commands=['start'])
