
def get_handlers() -> list:
    from .common import init_common_handlers
    from .chat import init_chat_handlers

    all_handlers: list = list()

    # регистрация хэндлеров
    all_handlers.append(init_common_handlers)
    all_handlers.append(init_chat_handlers)

    return all_handlers
