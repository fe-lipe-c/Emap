"""Zipf distribution probability mass function (PMF)"""

import numpy as np


def zipf_pmf(k, M, a):
    """Zipf distribution PMF."""
    return (1 / k**a) / np.sum([1 / i**a for i in range(1, M + 1)])


def zipf_rvs(M, a, size=1, seed=1):
    """Zipf random variables."""
    np.random.seed(seed)
    probabilities = [zipf_pmf(k, M, a) for k in range(1, M + 1)]
    return np.random.choice(M, size=size, p=probabilities) + 1
