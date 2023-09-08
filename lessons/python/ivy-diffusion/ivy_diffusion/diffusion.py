"""Modeling the one-dimensional diffusion equation."""
from .solver import calculate_time_step, set_initial_profile, solve1d


class Diffusion:

    """Model one-dimensional diffusion with fixed boundary conditions.

    Examples
    --------
    >>> import numpy as np
    >>> from .diffusion import Diffusion
    >>> m = Diffusion(diffusivity=0.25)
    >>> m.concentration = np.zeros(m.shape)
    >>> m.concentration[m.shape//2] = 5
    >>> m.concentration
    array([0.0, 0.0, 0.0, 0.0, 0.0, 5.0, 0.0, 0.0, 0.0, 0.0])
    >>> m.time_step
    1.0
    >>> m.time
    0.0
    >>> m.update()
    >>> m.time
    1.0
    >>> m.concentration
    array([0.0, 0.0, 0.0, 0.0, 1.2, 2.5, 1.2, 0.0, 0.0, 0.0])
    >>> m.update()
    >>> m.time
    2.0
    >>> m.concentration
    array([0.0, 0.0, 0.0, 0.3, 1.2, 1.9, 1.2, 0.3, 0.0, 0.0])
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
        self.time_step = calculate_time_step(self.spacing, self.diffusivity)
        self.concentration = set_initial_profile(self.shape)

    def update(self):
        """Calculate concentration at the next time step."""
        solve1d(self.concentration, self.spacing, self.time_step, self.diffusivity)
        self.time += self.time_step
