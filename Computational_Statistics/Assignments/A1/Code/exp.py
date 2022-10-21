"""Exponential Distribution."""

import numpy as np


def exp_dist(lambda_, u_rvs):
    """Exponential distribution."""
    return -(1 / lambda_) * np.log(1 - u_rvs)
