"""Metropolis-Hastings algorithm for Beta distribution."""

import numpy as np


def proposal():
    """Proposal distribution.

    Uniform distribution over the interval [0, 1].

    """
    return np.random.uniform()


def acceptance_probability(a, b, current, proposed):
    """Acceptance probability for proposed transition.

    Parameters
    ----------
    a : float
    b : float
    current : float
        Current state.
    proposed : float
        Proposed state.

    Returns
    -------
    float
        Acceptance probability.
    """
    up_term = proposed ** (a - 1) * (1 - proposed) ** (b - 1)
    down_term = current ** (a - 1) * (1 - current) ** (b - 1)
    acceptance_ratio = up_term / down_term

    return np.min([1, acceptance_ratio])
