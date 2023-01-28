from aiogram.types import Message

from .constants import API_ERROR


def api_exceptions(func):
    async def wrapper(*args, **kwargs):
        try:
            await func(*args, **kwargs)
        except Exception as e:
            # параметр e для будущих логов
            for arg in args:
                if arg.__class__ == Message:
                    await arg.reply(text=API_ERROR + str(e))
    return wrapper