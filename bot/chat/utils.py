import openai
from openai.openai_object import OpenAIObject

from config import chat_config


openai.api_key = chat_config.get("token")


async def code_generation(prompt: str) -> str:
    """
    Генерация кода
    """
    response: OpenAIObject = openai.Completion.create(
        engine="code-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )
    return response.choices[0].text


async def text_generation(prompt: str) -> str:
    """
    Генерация текста
    """
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=2048,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response.choices[0].text


async def image_generation(prompt: str) -> str:
    """
    Генерация изображения
    """
    response = openai.Image.create(
        prompt=prompt,
        model="image-alpha-001"
    )
    return response['data'][0]['url']


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
