import pulp

from app.model.board import Board


class Solver:
    """A class to represent a Number Place solver using linear programming.

    Methods
    -------
        _add_constraints:
            Add all necessary constraints to the linear programming problem.
        _set_values:
            Set values from the initial cell as constraints in the problem.
        solve:
            Solve the Number Place and returns the solved cell.

    """

    def __init__(self: "Solver") -> None:
        """Construct all the necessary attributes for the Solver object."""
        self.prob = pulp.LpProblem("NumberPlace", pulp.LpMinimize)
        self.x = pulp.LpVariable.dicts(
            "x",
            (
                range(Board.BOARD_SIZE),
                range(Board.BOARD_SIZE),
                range(1, Board.BOARD_SIZE + 1),
            ),
            cat="Binary",
        )

    def _add_constraints(self: "Solver") -> None:
        """Add all necessary constraints to the linear programming problem."""
        for num in range(1, Board.BOARD_SIZE + 1):
            for i in range(Board.BOARD_SIZE):
                self.prob += (
                    pulp.lpSum(self.x[i][j][num] for j in range(Board.BOARD_SIZE)) == 1
                )
                self.prob += (
                    pulp.lpSum(self.x[j][i][num] for j in range(Board.BOARD_SIZE)) == 1
                )

            for block_row in range(Board.BLOCK_SIZE):
                for block_col in range(Board.BLOCK_SIZE):
                    self.prob += (
                        pulp.lpSum(
                            self.x[block_row * Board.BLOCK_SIZE + i][
                                block_col * Board.BLOCK_SIZE + j
                            ][num]
                            for i in range(Board.BLOCK_SIZE)
                            for j in range(Board.BLOCK_SIZE)
                        )
                        == 1
                    )

        for row in range(Board.BOARD_SIZE):
            for col in range(Board.BOARD_SIZE):
                self.prob += (
                    pulp.lpSum(
                        self.x[row][col][num] for num in range(1, Board.BOARD_SIZE + 1)
                    )
                    == 1
                )

    def _set_values(
        self: "Solver", prob: list[list[int]], values: tuple = range(1, 10)
    ) -> None:
        """Set values of Number Place Problem."""
        for row in range(Board.BOARD_SIZE):
            for col in range(Board.BOARD_SIZE):
                if (num := prob[row][col]) in values:
                    self.prob += self.x[row][col][num] == 1

    def solve(self: "Solver", prob: list[list[int]]) -> tuple[list[list[int]], bool]:
        """Solve the Number Place.

        Args:
        ----
            prob (list[list[int]]): The problem of Number Place.
            values (tupple): Numbers to treat as problem.

        Returns:
        -------
            tuple[[list[list[int]]], bool]:
                The solved Number Place cell if a solution exists.
                None: If no solution exists.

        """
        self._add_constraints()
        self._set_values(prob, values=range(1, Board.BOARD_SIZE + 1))

        self.prob.solve()

        if pulp.LpStatus[self.prob.status] != "Optimal":
            return None, False

        result = [
            [
                next(
                    num
                    for num in range(1, Board.BOARD_SIZE + 1)
                    if pulp.value(self.x[row][col][num]) == 1
                )
                for col in range(Board.BOARD_SIZE)
            ]
            for row in range(Board.BOARD_SIZE)
        ]

        return Board(result).tolist(), True
