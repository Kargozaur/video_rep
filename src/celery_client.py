import os

from celery import Celery
from dotenv import load_dotenv

load_dotenv()
app = Celery(
    "video_rep",
    worker_prefetch_multiplier=1,
    task_ack_late=True,
    task_limit_rate=600,
    task_soft_time_limit=540,
    broker=os.getenv("RMQ_URL"),
    backend=f"postgres+{os.getenv('DB_DRIVER')}//"
    f"{os.getenv('DB_USER')}:{os.getenv('DB_PASS')}"
    f"@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}",
)
