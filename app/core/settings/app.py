from pydantic import ConfigDict
from pydantic_settings import BaseSettings


class AppSettings(BaseSettings):
    """Class containing settings for the app.

    Attributes
    ----------
        model_config (ConfigDict): Configuration dictionary for the model.

        allowed_hosts (list[str]): List of allowed hosts. Defaults to ["*"].
        api_prefix_v1 (str): API prefix for version 1. Defaults to "/api/v1".
        debug (bool): Boolean flag for debug mode. Defaults to False.
        docs_url (str): URL for the documentation. Defaults to "/docs".
        open_api_prefix (str): Prefix for the OpenAPI. Defaults to ""
        open_api_url (str): URL for the OpenAPI. Defaults to "openapi.json".
        redoc_url (str): URL for ReDoc. Defaults to "/redoc".
        title (str): Title of the API. Defaults to "Sudoku API".
        version (str): Version of the API. Defaults to "0.0.1".

    """

    allowed_hosts: list[str] = ["*"]
    api_prefix_v1: str = "/api/v1"
    debug: bool = False
    docs_url: str = "/docs"
    open_api_prefix: str = ""
    open_api_url: str = "openapi.json"
    redoc_url: str = "/redoc"
    title: str = "Sudoku API"
    version: str = "0.0.1"

    model_config = ConfigDict(env_file=".env.development", validate_assignment=True)

    @property
    def fastapi_kwargs(self: "AppSettings") -> dict[str, bool | str]:
        """Method to return FastAPI kwargs.

        Args:
        ----
            self (AppSettings): Instance of AppSettings.

        Returns:
        -------
            dict[str, bool | str]: FastAPI kwargs dictionary.

        """
        return {
            "debug": self.debug,
            "docs_url": self.docs_url,
            "open_api_prefix": self.open_api_prefix,
            "open_api_url": self.open_api_url,
            "redoc_url": self.redoc_url,
            "title": self.title,
            "version": self.version,
        }
