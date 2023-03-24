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


async def image_edit_request_data(message: Message):
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(verify_ssl=False)) as request:
        photo = await request.get(await message.document.get_url())
        image_bytes = await photo.read()

    data = aiohttp.FormData()
    data.add_field('image', image_bytes, content_type='image/png', filename='image.png')
    data.add_field('response_format', 'url')
    data.add_field('n', '3')
    data.add_field('size', '1024x1024')

    # data = {
    #     'image': {
    #         'value': image_bytes,
    #         'content_type': 'image/png',
    #     },
    #     'response_format': "url",
    #     'n': '3',
    #     'size': "1024x1024"
    # }

    response_data: dict = dict(
        url="https://api.openai.com/v1/images/variations",
        headers=chat_config.get('headers'),
        data=data,
    )

    response_data.get('headers').update(
        {
            'Content-Type': 'multipart/form-data'
        }
    )

    return response_data
