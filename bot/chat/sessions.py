import aiohttp
from aiogram.types import Message, ParseMode
from aiohttp.web import HTTPBadRequest, HTTPTooManyRequests, HTTPBadGateway

from .exceptions import create_log


async def create_session(request_data: dict, message: Message) -> dict:
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(verify_ssl=False)) as request:
        async with request.post(**request_data) as response:
            if response.status == 400:
                result: dict = await response.json()
                error_message: str = result.get("error").get("message")
                await message.reply(text=error_message)
                await create_log(message=message, error=result, answer=error_message)
                raise HTTPBadRequest
            elif response.status == 502:
                result: str = await response.text()
                print("===502===")
                print(result)
                await message.reply(text=result, parse_mode=ParseMode.HTML)
                await create_log(message=message, error=result, answer=result)
                raise HTTPBadGateway
            elif response.status == 429:
                result: dict = await response.json()
                error_message: str = result.get("error").get("message")
                await message.reply(text=error_message)
                await create_log(message=message, error=result, answer=error_message)
                raise HTTPTooManyRequests

            else:
                return await response.json()
