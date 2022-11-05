"""Beta from uniform rv."""

import numpy as np
from gamma import gamma_dist


def beta_dist(a, b, size, seed=1):
    """Beta distribution."""
    # np.random.seed(seed)
    # beta_rv = np.zeros(size)
    if a == 0 or b == 0:
        return print("Erro: a,b > 0")
    if type(a) is int and type(b) is int:
        x = gamma_dist(a, 1, size, seed)
        y = gamma_dist(b, 1, size, seed + 1)
        try:
            beta_rv = x / (x + y)
            return beta_rv
        except ZeroDivisionError:
            return print("Erro")
    else:
        print("Erro: a and b must be integers")
