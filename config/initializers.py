from aiogram import Bot, Dispatcher


def init_dispatcher() -> Dispatcher:
    from config import bot_config

    bot: Bot = Bot(**bot_config)
    dp: Dispatcher = Dispatcher(bot)
    return dp
