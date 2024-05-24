from fastapi import HTTPException
from starlette.requests import Request
from starlette.responses import JSONResponse


async def http_error_handler(_: Request, exception: HTTPException) -> JSONResponse:
    return JSONResponse(
        content={"errors": [exception.detail]}, status_code=exception.status_code
    )
