import aiohttp
from aiogram.types import Message

from config import chat_config


def code_request_data(prompt: str) -> dict:
    response_data: dict = dict(
        url="https://api.openai.com/v1/engines/code-cushman-001/completions",
        headers=chat_config.get('headers'),
        json=dict(
            prompt=prompt,
            max_tokens=1024,
            n=3,
            stop=None,
            temperature=0.7
        )
    )

    return response_data


def text_request_data(prompt: str) -> dict:
    response_data: dict = dict(
        url="https://api.openai.com/v1/engines/text-davinci-002/completions",
        headers=chat_config.get('headers'),
        json=dict(
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.7
        )
    )

    return response_data


def image_create_request_data(prompt: str) -> dict:
    response_data: dict = dict(
        url="https://api.openai.com/v1/images/generations",
        headers=chat_config.get('headers'),
        json=dict(
            prompt=prompt,
            response_format="url",
            model="image-alpha-001",
            num_images=3
        )
    )

    return response_data


async def image_variation_request_data(photo_url: str):
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(verify_ssl=False)) as request:
        photo = await request.get(photo_url)
        image_bytes = await photo.read()

    response_data: dict = dict(
        url="https://api.openai.com/v1/images/variations",
        headers=chat_config.get('headers'),
        data=dict(
            image=image_bytes,
            response_format='url',
            n='3',
            size='1024x1024'
        )
    )

    del response_data.get('headers')['Content-Type']

    return response_data
