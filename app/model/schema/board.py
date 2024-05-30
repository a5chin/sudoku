from typing import Annotated

from annotated_types import Len
from fastapi import Query
from fastapi.exceptions import RequestValidationError
from pydantic import BaseModel, ConfigDict, Json, ValidationError


class Board(BaseModel):
    """A class representing Number Place board.

    Attributes
    ----------
        model_config (ConfigDict): Configuration dictionary for the model.

        prob (list[list[int]]): A 9x9 grid representing the board with integer values.

    """

    model_config = ConfigDict(from_attributes=True)

    prob: Annotated[
        list[
            Annotated[
                list[int],
                Len(min_length=9, max_length=9),
            ]
        ],
        Len(min_length=9, max_length=9),
    ]

    @classmethod
    def get_board(
        cls: "Board",
        prob: Json = Query(...),  # noqa: B008
    ) -> "Board":
        """Get Query parameter.

        Args:
        ----
            cls (Board): The BaseModel class.
            prob (Json, optional): Number Place problem. Defaults to Query(...).

        Raises:
        ------
            RequestValidationError: Raised when there is an error with the request.

        Returns:
        -------
            Board: Returns a Board instance.

        """
        try:
            return cls.model_validate(Board(prob=prob))
        except ValidationError as exc:
            raise RequestValidationError(errors=exc.errors()) from exc
