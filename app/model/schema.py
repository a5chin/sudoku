from fastapi import Query
from pydantic import BaseModel


class Sudoku(BaseModel):
    """Get answer model for Number Place.

    Args:
    ----
        prob (str): Query of Number Place problem

    """

    prob: str = Query(default=None)
