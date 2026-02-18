from typing import Annotated

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

Port = Annotated[int, Field(..., ge=1, le=65535)]


class DBSettings(BaseSettings):
    user: str
    password: str
    host: str
    name: str
    port: Port

    model_config = SettingsConfigDict(env_file=".env", env_prefix="DB_", extra="ignore")

    @property
    def dsn(self) -> str:
        return f"postgres://{self.user}:{self.password}@{self.host}:{self.port}/{self.name}"
