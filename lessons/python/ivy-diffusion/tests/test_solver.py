"""Test the solver module."""
import math

import numpy as np
from ivy_diffusion.solver import calculate_time_step, set_initial_profile, solve1d

DOMAIN_SIZE = 100
GRID_SPACING = 1.0
DIFFUSIVITY = 1.0
TIME_STEP = 0.475
TOLERANCE = 0.01
ZMAX = 500.0


def test_time_step():
    time_step = calculate_time_step(GRID_SPACING, DIFFUSIVITY)
    assert type(time_step) is float
    assert math.isclose(time_step, TIME_STEP, rel_tol=TOLERANCE)


def test_initial_profile_defaults():
    z = set_initial_profile()
    assert type(z) is np.ndarray
    assert len(z) == DOMAIN_SIZE
    assert math.isclose(z.max(), ZMAX, rel_tol=TOLERANCE)


def test_solve1d():
    z = np.zeros(DOMAIN_SIZE)
    z[DOMAIN_SIZE // 2] = ZMAX
    solve1d(z, time_step=TIME_STEP)
    assert type(z) is np.ndarray
    assert len(z) == DOMAIN_SIZE
    assert z.max() < ZMAX
    assert z.sum() == ZMAX
