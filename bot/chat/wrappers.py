from typing import Callable

from aiogram.types import Message

from .exceptions import parse_error, create_log


def api_exceptions(api_case: Callable) -> Callable:
    async def wrapper(*args, **kwargs) -> None:
        try:
            await api_case(*args, **kwargs)
        except Exception as error:
            error_message_for_user: str = parse_error(error=error)
            message = kwargs.get("message") or next((arg for arg in args if isinstance(arg, Message)), None)
            await message.reply(text=error_message_for_user)
            message.values["api_case"] = api_case.__name__
            await create_log(message=message, error=error, answer=error_message_for_user)
    return wrapper
