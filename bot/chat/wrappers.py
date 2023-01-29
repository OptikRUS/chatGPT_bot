from typing import Callable

from aiogram.types import Message

from config import chat_config
from .exceptions import parse_error, create_log


def api_exceptions(api_case: Callable) -> Callable:
    async def wrapper(*args, **kwargs) -> None:
        try:
            await api_case(*args, **kwargs)
        except Exception as error:
            error_message_for_user: str = parse_error(error=error)
            message = kwargs.get("message") or next((arg for arg in args if isinstance(arg, Message)), None)
            msg_for_log_chat: dict = create_log(message=message, error=error, answer=error_message_for_user)
            await message.reply(text=error_message_for_user)
            await message.bot.send_message(chat_id=chat_config.get("log_chat_id"), text=msg_for_log_chat)
    return wrapper
