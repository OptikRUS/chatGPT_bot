from random import choice

from .examples import (
    IMAGE_GENERATION_REQUEST_EXAMPLES,
    TEXT_GENERATION_REQUEST_EXAMPLES,
    CODE_GENERATION_REQUEST_EXAMPLES,
    IMAGE_VARIATION
)


REMEMBER: str = """
Помните, чем более конкретно и ясно вы формулируете запрос, тем лучше результат будет соответствовать вашим ожиданиям.\n
"""


def image_generation_message() -> str:
    message: str = f"""
    {REMEMBER}
Например:\n"{choice(IMAGE_GENERATION_REQUEST_EXAMPLES)}"\n\nВведите запрос для генерации изображения:
    """
    return message


def text_generation_message() -> str:
    message: str = f"""
    {REMEMBER}
Например:\n"{choice(TEXT_GENERATION_REQUEST_EXAMPLES)}"\n\nВведите запрос для генерации текста:
    """
    return message


def code_generation_message() -> str:
    message: str = f"""
    {REMEMBER}
Например:\n"{choice(CODE_GENERATION_REQUEST_EXAMPLES)}"\n\nВведите запрос для генерации кода:
    """
    return message


def edit_image_generation_message() -> str:
    message: str = f"""
    {IMAGE_VARIATION}\nОтправьте документ в формате png:
    """
    return message
