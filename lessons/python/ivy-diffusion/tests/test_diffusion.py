"""Tests for the diffusion module."""
import numpy as np
from ivy_diffusion.diffusion import Diffusion

SHAPE = 10
SPACING = 1.0
DIFFUSIVITY = 1.0
ZMAX = 5.0


def test_defaults():
    m = Diffusion()
    assert isinstance(m, Diffusion)
    assert m.shape == SHAPE
    assert m.spacing == SPACING
    assert m.diffusivity == DIFFUSIVITY
    assert m.time == 0.0
    assert m.time_step > 0.0
    assert type(m.concentration) is np.ndarray
    assert len(m.concentration) == SHAPE


def test_update():
    m = Diffusion()
    m.concentration = np.zeros(SHAPE)
    m.concentration[SHAPE // 2] = ZMAX
    m.update()
    assert m.time > 0.0
    assert m.concentration.max() < ZMAX
    assert m.concentration.sum() == ZMAX
