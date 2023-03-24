import aiohttp
from aiogram.types import Message

from .responses import bad_response


async def create_session(request_data: dict, message: Message) -> dict:
    print()
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(verify_ssl=False)) as request:
        print()
        async with request.post(**request_data) as response:
            print()
            if response.status == 200:
                return await response.json()
            else:
                await bad_response(response=response, message=message)
