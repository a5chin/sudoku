"""Defines the available routers for the API and health checks."""

from app.api.routes.api import Tags
from app.api.routes.api import router as api_router
from app.api.routes.healthz import router as healthz_router

__all__ = ["api_router", "healthz_router", "Tags"]
