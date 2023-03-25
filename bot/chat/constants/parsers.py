from asyncio import TimeoutError
from aiogram.utils.exceptions import MessageTextIsEmpty
from aiohttp.web_exceptions import (
    HTTPForbidden,
    HTTPBadGateway,
    HTTPBadRequest,
    HTTPUnauthorized,
    HTTPTooManyRequests,
    HTTPInternalServerError
)

from .errors import (
    API_ERROR,
    TIME_OUT_ERROR,
    FORBIDDEN_ERROR,
    SERVER_502_ERROR,
    UNAUTHORIZED_ERROR,
    TOO_MANY_REQUESTS_ERROR,
    REQUEST_MESSAGE_IS_TOO_LONG_ERROR,
    INTERNAL_SERVER_ERROR_ERROR
)


def parse_error(error: Exception) -> str:
    if error.__class__ == TimeoutError:
        return TIME_OUT_ERROR
    elif error.__class__ == HTTPBadRequest:
        return API_ERROR
    elif error.__class__ == HTTPUnauthorized:
        return UNAUTHORIZED_ERROR
    elif error.__class__ == HTTPForbidden:
        return FORBIDDEN_ERROR
    elif error.__class__ == HTTPTooManyRequests:
        return TOO_MANY_REQUESTS_ERROR
    elif error.__class__ == HTTPInternalServerError:
        return INTERNAL_SERVER_ERROR_ERROR
    elif error.__class__ == HTTPBadGateway:
        return SERVER_502_ERROR
    elif error.__class__ == MessageTextIsEmpty:
        return REQUEST_MESSAGE_IS_TOO_LONG_ERROR
    return API_ERROR
