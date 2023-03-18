from pydantic import BaseSettings


class AdvancedSettings(BaseSettings):
    class Config:
        allow_mutation = False
        env_file = ".env"
        env_file_encoding = "utf-8"
