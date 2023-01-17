from aiogram import executor

from config.initializers import init_dispatcher
from config import polling_config


dispatcher = init_dispatcher()


if __name__ == '__main__':
    executor.start_polling(dispatcher, **polling_config)
