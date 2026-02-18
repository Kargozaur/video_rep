import asyncio
from typing import Self

from tortoise import Tortoise

from src.celery_client import app
from src.core.settings.tortoise_config import TORTOISE_CONFIG
from src.reporter.reporter import Report
from src.services.renderer import VideoRenderer


async def _run_video(report_id: int) -> dict | str:
    await Tortoise.init(TORTOISE_CONFIG)
    report = None
    try:
        report = await Report.get_or_none(id=report_id)
        if not report:
            return f"Report {report_id} not found"
        report.status = "pending"
        await report.save()
        renderer = VideoRenderer(report.data)
        video_path = await renderer.generate()
        report.status = "done"
        await report.save()
        return {"status": "success", "path": video_path}

    except Exception as exc:
        if report:
            report.status = "error"
            await report.save()
        raise exc

    finally:
        await Tortoise.close_connection()


@app.task(name="generate_video_report", bind=True, default_retry_delay=60)
def generate_video_task(self: Self, report_id: int) -> dict | str:
    return asyncio.run(_run_video(report_id))
