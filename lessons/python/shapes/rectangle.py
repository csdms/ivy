from .shape import Shape


class Rectangle(Shape):
    def __init__(
        self, lower_left: tuple = (1.0, 1.0), width: float = 3.0, height: float = 2.0
    ) -> None:
        self.ll = lower_left
        self.w = width
        self.h = height
        x = [self.ll[0], self.ll[0] + self.w, self.ll[0] + self.w, self.ll[0]]
        y = [self.ll[1], self.ll[1], self.ll[1] + self.h, self.ll[1] + self.h]
        super().__init__(x, y)

    def calculate_area(self) -> None:
        self.area = self.w * self.h
