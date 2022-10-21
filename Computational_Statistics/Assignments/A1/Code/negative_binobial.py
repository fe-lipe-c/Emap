"""Negative Binomial Probability Mass Function.

The negative binomial r.v., with parameters (a,1/(b+1)), has the following probability mass function:
# P(x) = binom{x+a-1}{x} [1/(b+1)]**(x) [b/(b+1)]**(a)
"""

import numpy as np
from scipy import binom


def neg_binomial_pmf(a, b, size):
    """Negative Binomial probility mass function."""

    neg_bin_pmf = np.zeros(size)

    for x in range(size):
        neg_binomial_pmf[x] = (
            binom(x + a - 1, x) * (1 / (b + 1)) ** (x) * (b / (b + 1)) ** (a)
        )

    return neg_binomial_pmf
