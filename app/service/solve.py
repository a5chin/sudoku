from app.model import Board, Solver


def solve(prob: list[list[int]]) -> Board:
    """Solve Number Place.

    Args:
    ----
        prob (list[list[int]]): The problem of Number Place

    Returns:
    -------
        Board: The Number Place Board

    """
    solver = Solver()

    return solver.solve(prob)
