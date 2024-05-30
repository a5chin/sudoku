from fastapi.exceptions import RequestValidationError
from fastapi.openapi.constants import REF_PREFIX
from fastapi.openapi.utils import validation_error_response_definition
from pydantic import ValidationError
from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY


async def http422_error_handler(
    _: Request, exception: RequestValidationError | ValidationError
) -> JSONResponse:
    """Error handler for HTTP 422 Unprocessable Entity status code.

    Args:
    ----
        _ (Request): The request object.
        exception (RequestValidationError | ValidationError): The exception object.

    Returns:
    -------
        JSONResponse: JSON response containing the exception errors.

    """
    return JSONResponse(
        content={"errors": exception.errors()},
        status_code=HTTP_422_UNPROCESSABLE_ENTITY,
    )


validation_error_response_definition["properties"] = {
    "errors": {
        "title": "Errors",
        "type": "array",
        "items": {"$ref": f"{REF_PREFIX}ValidationError"},
    }
}
