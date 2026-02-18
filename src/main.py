from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from src.core.settings.settings import get_settings
from src.core.settings.tortoise_config import TORTOISE_CONFIG
from src.reporter.reporter import Report
from src.tasks.video_randerer import generate_video_task


def main() -> FastAPI:
    app = FastAPI(lifespan=lifespan)
    register_tortoise(app=app, config=TORTOISE_CONFIG, add_exception_handlers=True)

    @app.get("/")
    async def get_main() -> dict[str, str]:
        return {"pr": "video-rep"}

    @app.post("/report")
    async def create_report(data: dict) -> dict:
        title = data.get("title", "Untitled report")
        report = await Report.create(title=title, data=data, status="pending")
        generate_video_task.delay(report.id)
        return {"id": report.id, "message": "rendering"}

    return app


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator:
    settings = get_settings()
    app.state.settings = settings
    yield
