import os
from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path


BASE_DIR = Path(__file__).parent.parent


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=os.path.join("./.env"))
    HOST: str
    PORT: int
    LOGIN: str
    PASSWORD: str
    RABBITMQ_QUEUE_TASK: str

    @property
    def url(self) -> str:
        return f"amqp://{self.LOGIN}:{self.PASSWORD}@{self.HOST}:{self.PORT}"
