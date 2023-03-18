from pydantic import BaseSettings


class AdvancedSettings(BaseSettings):
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
