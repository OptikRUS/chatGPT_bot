from aiogram import Dispatcher
from aiogram.dispatcher.filters import CommandStart, CommandHelp

from .start import bot_help, bot_start, bot_test


def init_common_handlers(dp: Dispatcher):
    dp.register_message_handler(bot_start, CommandStart())
    dp.register_message_handler(bot_help, CommandHelp())
    dp.register_message_handler(bot_test, commands=["test"])
