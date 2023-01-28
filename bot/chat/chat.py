from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, Message

from bot.keyboards import MAIN_MENU
from .chat_cases import process_output, button_selection
from .constants import MAIN_MENU_MESSAGE


async def process_callback_inline_buttons(callback_query: CallbackQuery, state: FSMContext):
    await state.update_data(button=callback_query.data)
    await button_selection(callback_query)


async def process_input(message: Message, state: FSMContext):
    state_data: dict = await state.get_data()
    inline_button: str = state_data.get('button')
    await process_output(inline_button=inline_button, message=message)
    await state.finish()
    await message.bot.send_message(chat_id=message.chat.id, text=MAIN_MENU_MESSAGE, reply_markup=MAIN_MENU)
