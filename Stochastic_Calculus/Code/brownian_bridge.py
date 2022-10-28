"""Brownian Bridge."""

import numpy as np
from brownian_motion import brownian_motion


def brownian_bridge(delta_t=1000):
    """Brownian bridge."""
    Bt = brownian_motion(delta_t)
    Xt = np.zeros(delta_t)

    for t in range(delta_t):
        Xt[t] = Bt[t] - (t / delta_t) * Bt[-1]

    return Xt
