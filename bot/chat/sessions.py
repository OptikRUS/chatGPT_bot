import aiohttp
from aiogram.types import Message, ParseMode
from aiohttp import ClientResponseError

from .exceptions import create_log


async def create_session(request_data: dict, message: Message) -> dict:
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(verify_ssl=False)) as request:
        async with request.post(**request_data) as response:
            if response.status == 400:
                result = await response.json()
                error_message = result.get("error").get("message")
                create_log(message=message, error=result, answer=error_message)
                await message.reply(text=error_message)
            elif response.status == 502:
                result = await response.text()
                await message.reply(text=result, parse_mode=ParseMode.HTML)
                create_log(message=message, error=ClientResponseError, answer=result)
            else:
                return await response.json()
