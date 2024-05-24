from fastapi import APIRouter, status

router = APIRouter()


@router.get(
    path="",
    summary="",
    description="",
    response_description="",
    status_code=status.HTTP_200_OK,
)
async def healthz() -> dict[str, str]:
    """Health Check Endpoint.

    Returns
    -------
        dict[str, str]: Response of the Health Check Endpoint

    """
    return {"message": "It works!"}
