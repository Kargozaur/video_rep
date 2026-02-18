from typing import Annotated

from fastapi import Depends, Request

from src.core.settings.settings import Settings


def settings_states(request: Request) -> Settings:
    return request.app.state.settings


SettingsDep = Annotated[Settings, Depends(settings_states)]
