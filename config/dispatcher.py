from aiogram import Bot, Dispatcher


def init_dispatcher() -> Dispatcher:
    from config import bot_config
    from bot.handlers import get_handlers

    bot: Bot = Bot(**bot_config)
    dispatcher: Dispatcher = Dispatcher(bot)

    for register_handler in get_handlers():
        register_handler(dispatcher)

    return dispatcher
