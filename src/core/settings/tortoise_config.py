from src.core.settings.settings import Settings

settings = Settings()  # ty:ignore[missing-argument]
TORTOISE_CONFIG = {
    "connections": {"default": settings.db.dsn},
    "apps": {
        "models": {
            "models": ["src.reporter.reporter", "aerich.models"],
            "default_connection": "default",
        },
    },
    "use_tz": True,
    "timezone": "UTC",
}
