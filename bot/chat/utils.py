from aiogram.types import Message
from typing import Callable


async def replace_symbol(text: str) -> str:
    """
    Замена всех символов на валидные, для работы markdown
    """
    special_symbol = ('\\', '`', '*', '_', '{', '}', '[', ']', '(', ')', '#', '+', '-', '.', '!')

    for i in special_symbol:
        text = text.replace(i, f'\\{i}')

    return text


async def slice_message(
        replace_symbol_func: Callable,
        message: Message,
        text: str,
        parse_mode: str = "MarkdownV2"
) -> None:
    """
    Разделение сообщения по лимиту в 4096 символов
    """
    markdown_text = await replace_symbol_func(text)

    if len(markdown_text) > 4096:
        for x in range(0, len(markdown_text), 4096):
            await message.reply(text=markdown_text[x:x + 4096], parse_mode=parse_mode)

    else:
        await message.reply(text=markdown_text, parse_mode=parse_mode)
