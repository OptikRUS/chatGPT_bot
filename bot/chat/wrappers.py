from typing import Callable

from aiogram.types import Message

from .exceptions import parse_error, parse_log


def api_exceptions(api_case: Callable) -> Callable:
    async def wrapper(*args, **kwargs) -> None:
        try:
            await api_case(*args, **kwargs)
        except Exception as error:
            error_message_for_user: str = parse_error(error=error)
            if kwargs:
                parse_log(message=kwargs, error=error, answer=error_message_for_user)
                await kwargs.get('message').reply(text=error_message_for_user)
            elif args:
                for arg in args:
                    if arg.__class__ == Message:
                        parse_log(message=arg, error=error, answer=error_message_for_user)
                        await arg.reply(text=error_message_for_user)
    return wrapper
