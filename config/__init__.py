import os

from .settings import ChatApiSettings, BotSettings, PollingSettings

base_dir: str = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

chat_config: dict[str] = ChatApiSettings().dict()
bot_config: dict[str, bool] = BotSettings().dict()
polling_config: dict[str, bool, int, float] = PollingSettings().dict()
