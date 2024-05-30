from functools import lru_cache

from app.core.settings import AppSettings


@lru_cache
def get_app_settings() -> AppSettings:
    """Get App Settings.

    Returns
    -------
        AppSettings: Class containing settings for the app

    """
    return AppSettings()
