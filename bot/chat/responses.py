from aiogram.types import Message
from aiohttp import ClientResponse
from aiohttp.web_exceptions import (
    HTTPError,
    HTTPForbidden,
    HTTPBadGateway,
    HTTPBadRequest,
    HTTPUnauthorized,
    HTTPTooManyRequests,
    HTTPInternalServerError
)

from .logger import create_log


async def bad_response(response: ClientResponse, message: Message):
    result: dict = await response.json()
    error_message: str = result.get("error").get("message")
    await message.reply(text=error_message)
    await create_log(message=message, error=result, answer=error_message)
    if response.status == 400:
        raise HTTPBadRequest
    elif response.status == 401:
        raise HTTPUnauthorized
    elif response.status == 403:
        raise HTTPForbidden
    elif response.status == 429:
        raise HTTPTooManyRequests
    elif response.status == 500:
        raise HTTPInternalServerError
    elif response.status == 502:
        raise HTTPBadGateway
    error_data: dict = dict(
        headers=response.headers,
        content_type=response.content_type,
        reason=response.reason,
        body=response._body,
        text=await response.text()
    )
    raise HTTPError(**error_data)
