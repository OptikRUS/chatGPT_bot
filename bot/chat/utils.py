from typing import Callable, Optional


def restyle_text(text: str, response_style: str) -> str:
    """
    Смена стиля текста
    """
    if response_style == 'code':
        text = f'`{text}`'

    return text


def replace_symbol(text: str) -> str:
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


def slice_message(replace_symbol_func: Callable, text: str, response_style: Optional[str] = None) -> list[str]:
    """
    Разделение сообщения по лимиту в 4096 символов
    """
    text_parts: list[str] = list()
    markdown_text: str = replace_symbol_func(text)

    if len(markdown_text) > 4096:
        for size in range(0, len(markdown_text), 4096):
            response_text = restyle_text(text=markdown_text[size:size + 4096], response_style=response_style)
            text_parts.append(response_text)
    else:
        response_text = restyle_text(text=markdown_text, response_style=response_style)
        text_parts.append(response_text)

    return text_parts
