import logging

from asyncio import TimeoutError
from aiogram.types import Message

from .constants import API_ERROR, TIME_OUT_ERROR

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
    return API_ERROR


def parse_log(message: Message | dict) -> None:
    message: Message = message.get("message") if message.__class__ == dict else message
    logging.error(msg=message)
