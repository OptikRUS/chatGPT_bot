from typing import Callable

from aiogram.types import Message


async def restyle_text(
        text: str,
        response_style: str
) -> str:
    """
    Смена стиля текста
    """
    if response_style == 'code':
        text = f'`{text}`'

    return text


async def replace_symbol(text: str) -> str:
    """
    Замена всех символов на валидные, для работы markdown
    """
    special_symbols = (
        '\\', '`', '*', '_', '{', '}', '[', ']', '=',
        '(', ')', '#', '+', '-', '.', '!', '/', '>', '<'
    )

    for symbol in special_symbols:
        text = text.replace(symbol, f'\\{symbol}')

    return text


async def slice_message(
        replace_symbol_func: Callable,
        message: Message,
        text: str,
        response_style: str = None,
        parse_mode: str = "MarkdownV2"
) -> None:
    """
    Разделение сообщения по лимиту в 4096 символов
    """
    markdown_text = await replace_symbol_func(text)

    if len(markdown_text) > 4096:
        for size in range(0, len(markdown_text), 4096):
            response_text = await restyle_text(text=markdown_text[size:size + 4096], response_style=response_style)

            await message.reply(text=response_text, parse_mode=parse_mode)

    else:
        response_text = await restyle_text(text=markdown_text, response_style=response_style)

        await message.reply(text=response_text, parse_mode=parse_mode)
