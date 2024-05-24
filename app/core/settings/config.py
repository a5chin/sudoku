from functools import lru_cache

from app.core.settings import AppSettings


@lru_cache
def get_app_settings():
    return AppSettings()
