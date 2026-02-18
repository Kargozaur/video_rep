from pydantic_settings import BaseSettings, SettingsConfigDict


class RedisSettings(BaseSettings):
    url: str
    cache_url: str

    model_config = SettingsConfigDict(
        env_file=".env", extra="ignore", env_prefix="REDIS_"
    )
