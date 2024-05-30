import unittest

import pytest
from fastapi.exceptions import RequestValidationError

from app.api.routes.solve import solve
from app.model.schema import Board


class GetResultTestCase(unittest.IsolatedAsyncioTestCase):
    """Test case for solving a Number Place problem."""

    def setUp(self: "GetResultTestCase") -> None:
        """Set up the test case with a Number Place problem and its solution."""
        # Number Place problem info
        self.prob = [
            [8, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 3, 6, 0, 0, 0, 0, 0],
            [0, 7, 0, 0, 9, 0, 2, 0, 0],
            [0, 5, 0, 0, 0, 7, 0, 0, 0],
            [0, 0, 0, 0, 4, 5, 7, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 3, 0],
            [0, 0, 1, 0, 0, 0, 0, 6, 8],
            [0, 0, 8, 5, 0, 0, 0, 1, 0],
            [0, 9, 0, 0, 0, 0, 4, 0, 0],
        ]
        self.result = [
            [8, 1, 2, 7, 5, 3, 6, 4, 9],
            [9, 4, 3, 6, 8, 2, 1, 7, 5],
            [6, 7, 5, 4, 9, 1, 2, 8, 3],
            [1, 5, 4, 2, 3, 7, 8, 9, 6],
            [3, 6, 9, 8, 4, 5, 7, 2, 1],
            [2, 8, 7, 1, 6, 9, 5, 3, 4],
            [5, 2, 1, 9, 7, 4, 3, 6, 8],
            [4, 3, 8, 5, 2, 6, 9, 1, 7],
            [7, 9, 6, 3, 1, 8, 4, 5, 2],
        ]

    async def test_solve(self: "GetResultTestCase") -> None:
        """Test the solve function with a Number Place problem."""
        self.prob = Board.get_board(self.prob)
        response = await solve(self.prob)

        self.assertEqual(response.result, self.result)
        self.assertEqual(response.is_solved, True)


class GetBoardTestCase(unittest.TestCase):
    """Test case for getting a Number Place problem."""

    def setUp(self: "GetBoardTestCase") -> None:
        """Set up the test case with a Number Place problem and its solution."""
        # Number Place problem info
        self.prob = [
            [0, 9, 0, 6, 0, 1, 0, 2, 0],
            [8, 0, 0, 0, 0, 0, 0, 0, 3],
            [0, 0, 0, 8, 4, 2, 5, 0, 0],
            [7, 0, 6, 0, 0, 0, 9, 0, 8],
            [0, 0, 1, 0, 5, 0, 7, 0, 0],
            [3, 0, 5, 0, 0, 0, 4, 0, 6],
            [0, 0, 9, 5, 1, 8, 6, 0, 0],
            [4, 0, 0, 0, 0, 0, 0, 0, 1],
            [0, 1, 0, 2, 0, 4, 0, 8, 0],
        ]

    def test_get_board(self: "GetBoardTestCase") -> None:
        """Test the get function with a Number Place problem."""
        prob = Board.get_board(self.prob)

        self.assertIsInstance(prob, Board)

        with pytest.raises(RequestValidationError):
            Board.get_board(self.prob[:1])

        with pytest.raises(RequestValidationError):
            Board.get_board(self.prob[:][:1])


if __name__ == "__main__":
    unittest.main()
