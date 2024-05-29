from fastapi import HTTPException
from starlette.requests import Request
from starlette.responses import JSONResponse


async def http_error_handler(_: Request, exception: HTTPException) -> JSONResponse:
    """Handle HTTP errors and return a JSON response with error details.

    Args:
    ----
        _ (Request): The incoming request object.
        exception (HTTPException): The HTTPException object containing error details.

    Returns:
    -------
        JSONResponse: A JSON response containing the error details.

    """
    return JSONResponse(
        content={"errors": [exception.detail]}, status_code=exception.status_code
    )
