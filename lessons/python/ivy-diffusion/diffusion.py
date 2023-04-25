"""Modeling the one-dimensional diffusion equation."""
import numpy as np


class Diffusion:

    """Model one-dimensional diffusion with fixed boundary conditions.

    Examples
    --------
    >>> import numpy as np
    >>> from diffusion import Diffusion
    >>> m = Diffusion(diffusivity=0.25)
    >>> m.concentration = np.zeros(m.shape)
    >>> m.concentration[int(m.shape/2)] = 5
    >>> m.concentration
    array([  0.0,   0.0,   0.0,   0.0,   0.0,   5.0,   0.0,   0.0,   0.0,
             0.0])
    >>> m.time
    0.0
    >>> m.update()
    >>> m.time
    1.0
    >>> m.concentration
    array([  0.0,   0.0,   0.0,   0.0,   1.2,   2.5,   1.2,   0.0,   0.0,
             0.0])
    """

    def __init__(self, shape=10, spacing=1.0, diffusivity=1.0):
        """Create a new diffusion model.

        Parameters
        ---------
        shape : int, optional
            The number of nodes in the solution grid.
        spacing : float, optional
            Grid spacing.
        diffusivity : float, optional
            Diffusivity.
        """
        self.shape = shape
        self.spacing = spacing
        self.diffusivity = diffusivity
        self.time = 0.0
        self.time_step = self.spacing**2 / (4.0 * self.diffusivity)

        self.concentration = np.random.random(self.shape)

    def solve(self):
        """Solve the 1D diffusion equation."""
        flux = -self.diffusivity * np.diff(self.concentration) / self.spacing
        self.concentration[1:-1] -= self.time_step * np.diff(flux) / self.spacing

    def update(self):
        """Calculate concentration at the next time step."""
        self.solve()
        self.time += self.time_step
