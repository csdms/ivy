"""A solver for the one-dimensional diffusion equation."""
import numpy as np

np.set_printoptions(precision=1, floatmode="fixed")


def calculate_time_step(grid_spacing, diffusivity):
    return grid_spacing**2 / diffusivity / 2.1


def set_initial_profile(domain_size=100, boundary_left=500, boundary_right=0):
    concentration = np.empty(domain_size)
    concentration[: int(domain_size / 2)] = boundary_left
    concentration[int(domain_size / 2) :] = boundary_right
    return concentration


def solve1d(concentration, grid_spacing=1.0, time_step=1.0, diffusivity=1.0):
    """Solve the one-dimensional diffusion equation with fixed boundary conditions.

    Parameters
    ----------
    concentration : ndarray
        The quantity being diffused.
    grid_spacing : float (optional)
        Distance between grid nodes.
    time_step : float (optional)
        Time step.
    diffusivity : float (optional)
        Diffusivity.

    Returns
    -------
    result : ndarray
        The concentration after a time step.

    Examples
    --------
    >>> import numpy as np
    >>> from solver import solve1d
    >>> z = np.zeros(5)
    >>> z[2] = 5
    >>> solve1d(z, diffusivity=0.25)
    array([   0.0,    1.2,    2.5,    1.2,    0.0])
    """
    flux = -diffusivity * np.diff(concentration) / grid_spacing
    concentration[1:-1] -= time_step * np.diff(flux) / grid_spacing


def diffusion_example():
    """An example of using `solve1d` in a diffusion problem."""
    print(example.__doc__)
    D = 100  # diffusivity
    Lx = 10  # domain length
    dx = 0.5  # grid spacing

    dt = calculate_time_step(dx, D)
    C = set_initial_profile(Lx)

    print("Time = 0\n", C)
    for t in range(1, 5):
        solve1d(C, dx, dt, D)
        print(f"Time = {t*dt:.4f}\n", C)


if __name__ == "__main__":
    diffusion_example()
