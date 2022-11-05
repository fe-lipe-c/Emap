"""Gamma Distribution."""

import numpy as np
from exp import exp_dist


def gamma_dist(a, b, size, seed=1):
    """Gamma distribution."""
    np.random.seed(seed)
    gamma_rv = np.zeros(size)
    if type(a) is int:
        for _ in range(a):
            u_rv = np.random.uniform(size=size)
            gamma_rv += exp_dist(b, u_rv)
    else:
        print("Erro")
    return gamma_rv
