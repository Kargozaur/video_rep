from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class RabbitMQSettings(BaseSettings):
    url: str = Field("RMQ_URL")

    model_config = SettingsConfigDict(
        env_file=".env", extra="ignore", env_prefix="RMQ_"
    )
