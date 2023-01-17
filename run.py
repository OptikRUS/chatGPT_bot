from aiogram import executor

from config.initializers import init_dispatcher
from config import polling_config


if __name__ == '__main__':
    dispatcher = init_dispatcher()
    executor.start_polling(dispatcher, **polling_config)
