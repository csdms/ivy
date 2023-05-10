"""A solver for the one-dimensional diffusion equation."""
import numpy as np

np.set_printoptions(formatter={"float": "{: 5.1f}".format})


def solve1d(concentration, spacing=1.0, time_step=1.0, diffusivity=1.0):
    """Solve the one-dimensional diffusion equation with fixed boundary conditions.

    Parameters
    ----------
    concentration : ndarray
        The quantity being diffused.
    spacing : float (optional)
        Grid spacing.
    time_step : float (optional)
        Time step.
    alpha : float (optional)
        Diffusivity.

    Returns
    -------
    result : ndarray
        The temperatures after time *time_step*.

    Examples
    --------
    >>> import numpy as np
    >>> from solver import solve1d
    >>> z = np.zeros(5)
    >>> z[2] = 5
    >>> solve1d(z, diffusivity=0.25)
    array([  0.0,   1.2,   2.5,   1.2,   0.0])
    """
    flux = -diffusivity * np.diff(concentration) / spacing
    concentration[1:-1] -= time_step * np.diff(flux) / spacing

    return concentration


def _run_example():
    """An example of running solve1d."""
    print(_run_example.__doc__)
    D = 100
    Lx = 10
    dx = 0.5
    C1 = 500
    C2 = 0
    C = np.empty(Lx)
    C[: int(Lx / 2)] = C1
    C[int(Lx / 2) :] = C2
    dt = dx * dx / D / 2.1
    print("Time = 0\n", C)

    for t in range(1, 3):
        solve1d(C, dx, dt, D)
        print(f"Time = {t}\n", C)


if __name__ == "__main__":
    _run_example()
