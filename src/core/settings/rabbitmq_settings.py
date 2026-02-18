from pydantic_settings import BaseSettings, SettingsConfigDict


class RabbitMQSettings(BaseSettings):
    url: str

    model_config = SettingsConfigDict(
        env_file=".env", extra="ignore", env_prefix="RMQ_"
    )
