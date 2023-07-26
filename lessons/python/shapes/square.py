from .rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, lower_left: tuple = (1.0, 1.0), width: float = 2.0) -> None:
        super().__init__(lower_left, width, width)
