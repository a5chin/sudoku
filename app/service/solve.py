from app.model import Board, Solver


def solve(prob: list[list[int]]) -> tuple[Board, bool]:
    """Solve Number Place.

    Args:
    ----
        prob (list[list[int]]): The problem of Number Place

    Returns:
    -------
        tuple[Board, bool]: The solved Number Place cell if a solution exists.
                            None: If no solution exists.

    """
    solver = Solver()

    return solver.solve(prob)
