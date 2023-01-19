from aiogram import executor

from config.dispatcher import init_dispatcher
from config import polling_config


if __name__ == '__main__':
    dp = init_dispatcher()
    executor.start_polling(dp, **polling_config)
