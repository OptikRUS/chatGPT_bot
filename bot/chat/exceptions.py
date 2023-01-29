import logging

from asyncio import TimeoutError
from aiogram.types import Message
from aiogram.utils.exceptions import MessageIsTooLong

from .constants import API_ERROR, TIME_OUT_ERROR, MESSAGE_IS_TOO_LONG_ERROR

console_handler = logging.StreamHandler()
file_handler = logging.FileHandler("logs/exceptions.log")

logging.basicConfig(
    format='%(asctime)s %(levelname)s %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    level=logging.ERROR,
    handlers=[console_handler, file_handler]
)


def parse_error(error: Exception):
    if error.__class__ == TimeoutError:
        return TIME_OUT_ERROR
    elif error.__class__ == MessageIsTooLong:
        return MESSAGE_IS_TOO_LONG_ERROR
    return API_ERROR


def create_log(message: Message, error: Exception, answer: str) -> None:
    msg: dict = dict(
        error=error,
        answer_to_user=answer,
        message=message
    )
    logging.error(msg=msg)
