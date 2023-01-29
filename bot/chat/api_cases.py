from aiogram.types import InputMediaPhoto, Message

from .sessions import create_session
from .request_data import code_request_data, text_request_data, image_create_request_data
from .wrappers import api_exceptions


@api_exceptions
async def code_generation(prompt: str, message: Message) -> None:
    """
    Генерация кода из OpenAI API
    """

    request_data: dict = code_request_data(prompt=prompt)
    result: dict = await create_session(request_data=request_data, message=message)
    code: str = result.get("choices")[0].get("text")
    await message.reply(text=code)


@api_exceptions
async def text_generation(prompt: str, message: Message) -> None:
    """
    Генерация текста из OpenAI API
    """

    request_data: dict = text_request_data(prompt=prompt)
    result: dict = await create_session(request_data=request_data, message=message)
    text: str = result.get("choices")[0].get("text")
    await message.reply(text=text)


@api_exceptions
async def image_generation(prompt: str, message: Message) -> None:
    """
    Генерация изображения из OpenAI API
    """

    request_data: dict = image_create_request_data(prompt=prompt)
    result: dict = await create_session(request_data=request_data, message=message)
    media: list[InputMediaPhoto] = [InputMediaPhoto(media=image.get("url")) for image in result.get("data")]
    await message.reply_media_group(media=media)
