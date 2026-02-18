from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from src.core.settings.settings import get_settings
from src.core.settings.tortoise_config import TORTOISE_CONFIG


def main() -> FastAPI:
    app = FastAPI(lifespan=lifespan)
    register_tortoise(app=app, config=TORTOISE_CONFIG, add_exception_handlers=True)

    @app.get("/")
    async def get_main() -> dict[str, str]:
        return {"pr": "video-rep"}

    return app


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator:
    settings = get_settings()
    app.state.settings = settings
    yield
