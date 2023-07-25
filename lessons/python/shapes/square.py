import numpy as np

from .rectangle import Rectangle


class Square(Rectangle):
    def __init__(
        self, lower_left: tuple = (1.0, 1.0), side_length: float = 2.0
    ) -> None:
        upper_right = (lower_left[0] + side_length, lower_left[1] + side_length)
        super().__init__(lower_left, upper_right)
