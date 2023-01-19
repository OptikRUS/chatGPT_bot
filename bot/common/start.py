from aiogram import types


async def bot_start(msg: types.Message):
    await msg.answer(f'Привет, {msg.from_user.full_name}!')


async def bot_help(msg: types.Message):
    await msg.answer(f"Какая-то подсказка")


async def bot_test(msg: types.Message):
    allowed_commands = ['/start', '/help', '/text']
    commands = '\n'.join(allowed_commands)
    await msg.answer(f"Доступные команды:\n{commands}")
