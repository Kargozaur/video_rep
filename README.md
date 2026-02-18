docker-compose --env-file .env_db up
aerich init -t src.core.settings.tortoise_config.TORTOISE_CONFIG
aerich migrate --name 
aerich upgrade