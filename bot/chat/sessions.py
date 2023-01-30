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
                await message.reply(text=error_message)
                await create_log(message=message, error=result, answer=error_message)
            elif response.status == 502:
                result = await response.text()
                print("===502===")
                print(result)
                await message.reply(text=result, parse_mode=ParseMode.HTML)
                await create_log(message=message, error=ClientResponseError, answer=result)
            if response.status == 429:
                result = await response.json()
                error_message = result.get("error").get("message")
                await message.reply(text=error_message)
                await create_log(message=message, error=result, answer=error_message)

            else:
                return await response.json()
