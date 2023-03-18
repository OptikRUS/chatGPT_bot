from pydantic import BaseSettings, Field, root_validator


class AdvancedSettings(BaseSettings):
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


class BranchValidate(AdvancedSettings):
    branch_name: str = Field(..., env="ENV")
    dev_bot_token: str = Field(..., env='DEV_BRANCH_BOT_TOKEN')
    dev_api_token: str = Field(..., env='DEV_API_CHAT_TOKEN')
    dev_logs_chat: int = Field(..., env='DEV_LOGS_CHAT')


class BotSettings(AdvancedSettings):
    token: str = Field("bot_token", env="BOT_TOKEN")
    validate_token: bool = Field(True, env="BOT_VALIDATE_TOKEN")

    @root_validator(pre=True)
    def check_branch(cls, values):
        branch_name: dict[str] = BranchValidate().dict()

        if branch_name.get('branch_name') == 'dev':
            values.update({'token': branch_name.get('dev_bot_token')})

        return values


class PollingSettings(AdvancedSettings):
    skip_updates: bool = Field(True, env="BOT_SKIP_UPDATES")
    reset_webhook: bool = Field(True, env="BOT_POLLING_RESET_WEBHOOK")
    timeout: int = Field(20, env="BOT_POLLING_TIMEOUT")
    relax: float = Field(0.1, env="BOT_POLLING_RELAX")
    fast: bool = Field(True, env="BOT_POLLING_FAST")


class ChatApiSettings(AdvancedSettings):
    token: str = Field("openai_api_key", env="OPENAI_API_KEY")
    log_chat_id: int = Field(..., env="LOGS_CHAT")
    headers: dict = dict()

    @root_validator(pre=True)
    def set_headers(cls, values):
        branch_name: dict[str] = BranchValidate().dict()

        if branch_name.get('branch_name') == 'dev':
            dict_for_update: dict = {
                'token': branch_name.get('dev_api_token'),
                'log_chat_id': branch_name.get('dev_logs_chat')
            }

            values.update(dict_for_update)

        token = values.get("token")
        values["headers"] = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}"
        }

        return values
