from enum import Enum

from fastapi import APIRouter

from app.api.routes import healthz, solve


class Tags(Enum):
    """An enumeration class for defining tags for API routes.

    Attributes
    ----------
        HEALTHZ (str): Tag for health check routes.
        SOLVE (str): Tag for solving Number Place problem routes.

    """

    HEALTHZ = "healthz"
    SOLVE = "solve"


router = APIRouter()
router.include_router(router=solve.router, tags=[Tags.SOLVE], prefix="/solve")
router.include_router(router=healthz.router, tags=[Tags.HEALTHZ], prefix="/healthz")
