import logging
from logging import StreamHandler, FileHandler

from aiogram.types import Message

from config import chat_config


console_handler: StreamHandler = logging.StreamHandler()
file_handler: FileHandler = logging.FileHandler("logs/exceptions.log")


logging.basicConfig(
    format='%(asctime)s %(levelname)s %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    level=logging.ERROR,
    handlers=[console_handler, file_handler]
)


async def create_log(message: Message, error: Exception | dict, answer: str) -> None:
    msg: dict = dict(
        error=error,
        answer_to_user=answer,
        message=message
    )
    logging.error(msg=msg)
    await message.bot.send_message(chat_id=chat_config.get("logs_chat_id"), text=msg)
