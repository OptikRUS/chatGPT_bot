from pydantic import Field, root_validator

from .base import AdvancedSettings


class EnvSettings(AdvancedSettings):
    env: str = Field("dev", env="ENV")
    bot_token: str = Field("bot_token", env="BOT_TOKEN")
    bot_token_dev: str = Field("bot_token_dev", env="BOT_TOKEN_DEV")
    api_token: str = Field("openai_api_key", env="OPENAI_API_KEY")
    api_token_dev: str = Field("openai_api_key_dev", env="OPENAI_API_KEY_DEV")
    log_chat_id: int = Field(415707746, env="LOG_CHAT_ID")
    log_chat_id_dev: int = Field(415707746, env="LOG_CHAT_ID_DEV")

    @root_validator
    def _env_validation(cls, values: dict):
        if values.get("env") == "dev":
            values.update({
                "bot_token": values.get("bot_token_dev"),
                "api_token": values.get("api_token_dev"),
                "log_chat_id": values.get("log_chat_id_dev")
            })

        values.pop("bot_token_dev")
        values.pop("api_token_dev")
        values.pop("log_chat_id_dev")

        return values


class BotSettings(AdvancedSettings):
    token: str = Field(EnvSettings().bot_token)
    validate_token: bool = Field(True, env="BOT_VALIDATE_TOKEN")


class PollingSettings(AdvancedSettings):
    skip_updates: bool = Field(True, env="BOT_SKIP_UPDATES")
    reset_webhook: bool = Field(True, env="BOT_POLLING_RESET_WEBHOOK")
    timeout: int = Field(20, env="BOT_POLLING_TIMEOUT")
    relax: float = Field(0.1, env="BOT_POLLING_RELAX")
    fast: bool = Field(True, env="BOT_POLLING_FAST")


class ChatApiSettings(AdvancedSettings):
    token: str = Field(EnvSettings().api_token)
    logs_chat_id: int = Field(EnvSettings().log_chat_id)
    headers: dict = dict()

    @root_validator
    def set_headers(cls, values: dict):
        token = values.get("token")
        values["headers"] = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}"
        }

        return values
