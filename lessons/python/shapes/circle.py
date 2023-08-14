import numpy as np

from .shape import Shape

MANY_POINTS = 100


class Circle(Shape):
    def __init__(self, center: tuple = (1.0, 1.0), radius: float = 1.0) -> None:
        self.c = center
        self.r = radius
        theta = np.linspace(0.0, 2 * np.pi, MANY_POINTS)
        x = self.c[0] + self.r * np.cos(theta)
        y = self.c[1] + self.r * np.sin(theta)
        super().__init__(x, y)

    def calculate_area(self) -> None:
        self.area = np.pi * self.r**2
