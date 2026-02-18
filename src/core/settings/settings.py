from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

from src.core.settings.db_settings import DBSettings


class Settings(BaseSettings):
    db: DBSettings = Field(default_factory=DBSettings)

    model_config = SettingsConfigDict(
        env_file=".env",
        env_delimiter="_",
        case_sensitive=False,
        extra="ignore",
        env_file_encoding="utf-8",
    )


def get_settings() -> Settings:
    return Settings()
