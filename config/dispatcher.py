from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage


def init_dispatcher() -> Dispatcher:
    from config import bot_config
    from bot.handlers import get_handlers

    bot: Bot = Bot(**bot_config)
    dispatcher: Dispatcher = Dispatcher(bot, storage=MemoryStorage())

    for register_handler in get_handlers():
        register_handler(dispatcher)

    return dispatcher
