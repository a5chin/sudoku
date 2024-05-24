from enum import Enum

from fastapi import APIRouter

from app.api.routes import healthz


class Tags(Enum):
    HEALTHZ = "healthz"


router = APIRouter()
router.include_router(router=healthz.router, tags=[Tags.HEALTHZ], prefix="/healthz")
