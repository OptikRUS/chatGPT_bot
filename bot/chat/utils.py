import openai
from aiogram.types import InputMediaPhoto, Message
from openai import InvalidRequestError
from openai.openai_object import OpenAIObject

from config import chat_config
from .constants import UNSAFE_REQUEST


openai.api_key = chat_config.get("token")


async def code_generation(prompt: str, message: Message) -> None:
    """
    Генерация кода
    """
    try:
        response: OpenAIObject = openai.Completion.create(
            engine="code-davinci-002",
            prompt=prompt,
            max_tokens=1024,
            n=3,
            stop=None,
            temperature=0.7,
        )
        code: str = response.choices[0].text
        await message.bot.send_message(chat_id=message.chat.id, text=code)
    except InvalidRequestError:
        await message.bot.send_message(chat_id=message.chat.id, text=UNSAFE_REQUEST)


async def text_generation(prompt: str, message: Message) -> None:
    """
    Генерация текста
    """
    try:
        response: OpenAIObject = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=2048,
            n=1,
            stop=None,
            temperature=0.5,
        )
        answer: str = response.choices[0].text
        await message.bot.send_message(chat_id=message.chat.id, text=answer)
    except InvalidRequestError:
        await message.bot.send_message(chat_id=message.chat.id, text=UNSAFE_REQUEST)


async def image_generation(prompt: str, message: Message) -> None:
    """
    Генерация изображения
    """
    try:
        response: OpenAIObject = openai.Image.create(
            prompt=prompt,
            model="image-alpha-001",
            n=3
        )
        media: list[InputMediaPhoto] = [InputMediaPhoto(media=image.url) for image in response['data']]
        await message.bot.send_media_group(chat_id=message.chat.id, media=media)
    except InvalidRequestError:
        await message.bot.send_message(chat_id=message.chat.id, text=UNSAFE_REQUEST)


# async def image_edit(prompt: str, image_bytes: bytes) -> str:
#     """
#     Редактирование изображения
#     """
#     example_prompt: str = "Сделай изображение более художественным"
#     response = openai.Image.create(
#         image=image_bytes,
#         model="image-davinci-002",
#         prompt=prompt,
#         size="1024x1024",
#         output_format="jpg"
#     )
#     return response['data'][0]['url']
