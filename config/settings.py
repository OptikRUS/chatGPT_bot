from pydantic import BaseSettings, Field


class BotSettings(BaseSettings):
    token: str = Field("bot_token", env="BOT_TOKEN")
    validate_token: bool = Field(True, env="BOT_VALIDATE_TOKEN")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


class PollingSettings(BaseSettings):
    skip_updates: bool = Field(True, env="BOT_SKIP_UPDATES")
    reset_webhook: bool = Field(True, env="BOT_POLLING_RESET_WEBHOOK")
    timeout: int = Field(20, env="BOT_POLLING_TIMEOUT")
    relax: float = Field(0.1, env="BOT_POLLING_RELAX")
    fast: bool = Field(True, env="BOT_POLLING_FAST")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


class ChatApiSettings(BaseSettings):
    token: str = Field("api_token", env="API_CHAT_TOKEN")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
