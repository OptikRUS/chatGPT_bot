from typing import Optional

from pydantic import BaseSettings, Field, root_validator


class AdvancedSettings(BaseSettings):
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


class EnvSettings(AdvancedSettings):
    env: str = Field("dev", env="ENV")


class BotSettings(AdvancedSettings):
    token: str = Field("bot_token", env="BOT_TOKEN")
    token_dev: Optional[str] = Field("bot_token", env="BOT_TOKEN_DEV")
    validate_token: bool = Field(True, env="BOT_VALIDATE_TOKEN")

    @root_validator
    def get_token(cls, values: dict):
        if EnvSettings().env == "dev":
            values["token"] = values.get("token_dev")
            values.pop("token_dev")
        return values


class PollingSettings(AdvancedSettings):
    skip_updates: bool = Field(True, env="BOT_SKIP_UPDATES")
    reset_webhook: bool = Field(True, env="BOT_POLLING_RESET_WEBHOOK")
    timeout: int = Field(20, env="BOT_POLLING_TIMEOUT")
    relax: float = Field(0.1, env="BOT_POLLING_RELAX")
    fast: bool = Field(True, env="BOT_POLLING_FAST")


class ChatApiSettings(AdvancedSettings):
    token: str = Field("openai_api_key", env="OPENAI_API_KEY")
    token_dev: Optional[str] = Field("openai_api_key_dev", env="OPENAI_API_KEY_DEV")
    log_chat_id: int = Field(415707746, env="LOG_CHAT_ID")
    log_chat_id_dev: Optional[int] = Field(415707746, env="LOG_CHAT_ID_DEV")
    headers: dict = dict()

    @root_validator
    def set_headers(cls, values):
        if EnvSettings().env == "dev":
            values["token"] = values.get("token_dev")
            values["log_chat_id"] = values.get("log_chat_id_dev")
            values.pop("token_dev")
            values.pop("log_chat_id_dev")

        token = values.get("token")
        values["headers"] = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}"
        }

        return values

