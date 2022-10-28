"""Brownian Motion."""

import numpy as np


def brownian_motion(delta_t=100):
    """Brownian motion with a simple random walk."""
    # Bt = np.zeros(delta_t)
    et = np.random.choice([1, -1], delta_t, p=[0.5, 0.5])
    Bt = np.cumsum(et)

    return Bt
