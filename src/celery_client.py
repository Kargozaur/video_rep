from celery import Celery

from src.core.settings.settings import Settings

settings = Settings()
app = Celery(
    "video_rep",
    broker=settings.rmq.url,
    backend=settings.redis.url,
)

app.conf.update(
    worker_prefetch_multiplier=1,
    task_acks_late=True,
    task_limit_rate=600,
    task_soft_time_limit=540,
)
