from typing import Callable

from aiogram.types import Message

from .constants import parse_error
from .constants.exeptions import TextTooLongError
from .logger import create_log


def api_exceptions(api_case: Callable) -> Callable:
    async def wrapper(*args, **kwargs) -> None:
        try:
            if len(kwargs.get('prompt')) > 500:
                raise TextTooLongError
            await api_case(*args, **kwargs)
        except Exception as error:
            error_message_for_user: str = parse_error(error=error)
            message = kwargs.get("message") or next((arg for arg in args if isinstance(arg, Message)), None)
            await message.reply(text=error_message_for_user)
            message.values["api_case"] = api_case.__name__
            await create_log(message=message, error=error, answer=error_message_for_user)
    return wrapper
