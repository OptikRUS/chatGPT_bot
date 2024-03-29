API_ERROR: str = f"""
⚠️ Что-то пошло не так.\n
"""

TIME_OUT_ERROR: str = f"""
⚠️ Время ответа от сервиса истекло.\n
"""

ANSWER_MESSAGE_IS_TOO_LONG_ERROR: str = f"""
⚠️ Слишком большая длина сообщения. Длина сообщения не должна привышать 500 символов.\n
"""

REQUEST_MESSAGE_IS_TOO_LONG_ERROR: str = f"""
⚠️ Превышен допустимый размер сообщения.\n
"""

UNAUTHORIZED_ERROR: str = f"""
⚠️ Ошибка авторизации.\n
"""

FORBIDDEN_ERROR: str = f"""
⚠️ Ошибка доступа.\n
"""

TOO_MANY_REQUESTS_ERROR: str = f"""
⚠️ Слишком много запросов.\n
"""

INTERNAL_SERVER_ERROR_ERROR: str = f"""
⚠️ Внутренняя ошибка сервиса.\n
"""

SERVER_502_ERROR: str = f"""
⚠️ Ошибка ответа сервиса.\n
"""
