import aiohttp
from aiogram.types import Message


async def create_session(request_data: dict, message: Message) -> dict:
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(verify_ssl=False)) as request:
        async with request.post(**request_data) as response:
            result = await response.json()
            if response.status == 400:
                error_message = result.get("error").get("message")
                await message.reply(text=error_message)
            else:
                return result
