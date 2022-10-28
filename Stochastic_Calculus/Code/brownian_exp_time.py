"""Brownian motion with exponential time.

Let x ~ exp(lambda), x independent of Bt. Then Yx = Bx.
"""

import numpy as np
from brownian_motion import brownian_motion


def bm_exp_time(delta_t=100, lambda_=1):
    """Brownian motion with exponential time."""
    Bt = brownian_motion(delta_t)
    Tt = np.random.exponential(scale=1 / lambda_, size=delta_t)
    Tt_norm = (Tt.round(2) * 100).astype(int)
    Xt = [Bt[tau] for tau in Tt_norm]

    return Xt
