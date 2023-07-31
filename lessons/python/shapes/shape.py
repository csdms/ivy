from abc import ABC, abstractmethod

import numpy as np


class Shape(ABC):
    @abstractmethod
    def __init__(self, x: np.ndarray, y: np.ndarray) -> None:
        self.x = x
        self.y = y
        self.n_sides = len(x)
        self.area = None

    @abstractmethod
    def calculate_area(self) -> None:
        ...
