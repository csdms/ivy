from .shape import Shape


class Rectangle(Shape):
    def __init__(
        self, lower_left: tuple = (1.0, 1.0), upper_right: tuple = (3.0, 2.0)
    ) -> None:
        self.ll = lower_left
        self.ur = upper_right
        x = [self.ll[0], self.ur[0], self.ur[0], self.ll[0]]
        y = [self.ll[1], self.ll[1], self.ur[1], self.ur[1]]
        super().__init__(x, y)

    def calculate_area(self) -> None:
        width = self.ur[0] - self.ll[0]
        height = self.ur[1] - self.ll[1]
        self.area = width * height
