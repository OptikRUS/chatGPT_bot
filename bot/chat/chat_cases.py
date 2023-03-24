from aiogram.types import Message, CallbackQuery, file, PhotoSize

from .api_cases import image_generation, text_generation, code_generation, image_variation
from .constants import (
    image_generation_message, code_generation_message, text_generation_message,
    GENERATE_TEXT_BUTTON, GENERATE_CODE_BUTTON, GENERATE_IMAGE_BUTTON, EDIT_IMAGE_BUTTON,
    WAIT_CODE, WAIT_TEXT, WAIT_IMAGE, WRONG_INPUT
)
from .constants.errors import ANSWER_MESSAGE_IS_TOO_LONG_ERROR
from .constants.message_generators import edit_image_generation_message


async def process_output(inline_button: str, message: Message) -> None:
    prompt: str | None = None
    photo_url: str | None = None
    photos_info = message.document
    content_type: str = message.content_type

    if content_type == 'document' and photos_info:
        photo_url = await photos_info.get_url()

    elif content_type == 'text':
        prompt: str = message.text

    else:
        await message.bot.send_message(chat_id=message.chat.id, text=WRONG_INPUT)

    if not prompt and not photos_info:
        await message.bot.send_message(chat_id=message.chat.id, text=WRONG_INPUT)
    elif prompt and len(prompt) > 500:
        await message.bot.send_message(chat_id=message.chat.id, text=ANSWER_MESSAGE_IS_TOO_LONG_ERROR)

    else:
        if inline_button == GENERATE_IMAGE_BUTTON:
            await message.bot.send_message(text=WAIT_IMAGE, chat_id=message.chat.id)
            await image_generation(prompt=prompt, message=message)
        elif inline_button == GENERATE_TEXT_BUTTON:
            await message.bot.send_message(text=WAIT_TEXT, chat_id=message.chat.id)
            await text_generation(prompt=prompt, message=message)
        elif inline_button == GENERATE_CODE_BUTTON:
            await message.bot.send_message(text=WAIT_CODE, chat_id=message.chat.id)
            await code_generation(prompt=prompt, message=message)
        elif inline_button == EDIT_IMAGE_BUTTON:
            await message.bot.send_message(text=WAIT_IMAGE, chat_id=message.chat.id)
            await image_variation(photo_url=photo_url, message=message)


async def button_selection(callback_query: CallbackQuery) -> None:
    if callback_query.data == GENERATE_IMAGE_BUTTON:
        await callback_query.bot.send_message(
            chat_id=callback_query.message.chat.id, text=image_generation_message()
        )
    elif callback_query.data == GENERATE_TEXT_BUTTON:
        await callback_query.bot.send_message(
            chat_id=callback_query.message.chat.id, text=text_generation_message()
        )
    elif callback_query.data == GENERATE_CODE_BUTTON:
        await callback_query.bot.send_message(
            chat_id=callback_query.message.chat.id, text=code_generation_message()
        )
    elif callback_query.data == EDIT_IMAGE_BUTTON:
        await callback_query.bot.send_message(
            chat_id=callback_query.message.chat.id, text=edit_image_generation_message()
        )
