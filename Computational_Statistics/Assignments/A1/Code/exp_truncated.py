"""Truncated Exponential Distribution."""

import numpy as np


def exp_truncated(lambda_, a, u_rvs):
    """Truncated exponential distribution."""
    return a - (1 / lambda_) * np.log(1 - u_rvs)


def exp_truncated_alt(lambda_, a, b, u_rvs):
    r"""Alternate formula to generate an exponential distribution.

    The formula is
    x = - 1\lambda * ln(e^(-lambda * a) - u(e^(-lambda * a)- e^(- lambda b)))
    """
    return -(1 / lambda_) * np.log(
        np.exp(-lambda_ * a) - u_rvs * (np.exp(-lambda_ * a) - np.exp(-lambda_ * b))
    )
