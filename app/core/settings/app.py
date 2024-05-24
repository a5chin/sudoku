from pydantic_settings import BaseSettings


class AppSettings(BaseSettings):
    allowed_hosts: list[str] = ["*"]
    api_prefix_v1: str = "/api/v1"
    debug: bool = False
    docs_url: str = "/docs"
    open_api_prefix: str = ""
    open_api_url: str = "openapi.json"
    redoc_url: str = "/redoc"
    title: str = "Sudoku API"
    version: str = "0.0.1"

    class Config:
        env_file: str = ".env.development"
        validate_assignment: bool = True

    @property
    def fastapi_kwargs(self: "AppSettings") -> dict[str, bool | str]:
        return {
            "debug": self.debug,
            "docs_url": self.docs_url,
            "open_api_prefix": self.open_api_prefix,
            "open_api_url": self.open_api_url,
            "redoc_url": self.redoc_url,
            "title": self.title,
            "version": self.version,
        }
