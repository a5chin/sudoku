from pydantic import BaseModel


class ResultResponse(BaseModel):
    """Get answer model for Number Place.

    Attributes
    ----------
        result (list[list[int]]): The result of Number Place problem
        is_solved (bool): Either problem is solved or not

    """

    result: list[list[int]] | None
    is_solved: bool
