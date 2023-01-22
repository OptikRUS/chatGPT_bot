from aiogram import Dispatcher

from .chat import process_callback_inline_buttons, process_input


def init_chat_handlers(dp: Dispatcher):
    from bot.keyboards import ChatButtons

    dp.register_callback_query_handler(
        process_callback_inline_buttons,
        lambda c: c.data in [button.name for button in ChatButtons]
    )
    dp.register_message_handler(process_input)
