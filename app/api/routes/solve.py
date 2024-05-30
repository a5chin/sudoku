from fastapi import APIRouter, Depends

from app.model.schema import Board, ResultResponse
from app.service import solve as sol

router = APIRouter()


@router.get(
    path="",
    response_model=ResultResponse,
    summary="",
    description="",
    response_description="",
)
async def solve(prob: Board = Depends(Board.get_board)) -> ResultResponse:  # noqa: B008
    """Solve Number Place.

    Args:
    ----
        prob (Board): Query of the Number Place problem

    Returns:
    -------
        ResultResponse: If the Number Place problem is not resolved, the result is None

    """
    result, is_solved = sol(prob.model_dump()["prob"])
    return ResultResponse(result=result, is_solved=is_solved)
