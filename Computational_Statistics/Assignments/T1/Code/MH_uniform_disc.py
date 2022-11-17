"""Script to draw samples of a uniform distribution on a disc.

Metropolis-Hastings version.
"""

import numpy as np
import pandas as pd
import altair as alt


def rw_proposal(x, sigma):
    """Random walk proposal."""
    return x + np.multiply(np.array(sigma), np.random.randn(2))


def rw_acceptance_probability(R, current, proposed):
    """Acceptance probability for proposed transition."""
    if proposed[0] > R or proposed[0] < 0:
        return 0
    else:
        pass

    if proposed[1] > 2 * np.pi or proposed[1] < 0:
        return 0
    else:
        pass

    acceptance_ratio = proposed[0] / current[0]
    return np.min([1, acceptance_ratio])


def local_opt_proposal(current, sigma):
    """Local optimization proposal.

    x_{t} = x_{t-1} + sigma/2 * nabla log(pi)|_{x_{t-1}} + sigma W,

    where W is a standard normal random variable and pi(r,theta) = r / (R * pi)
    """

    nabla_log_pi = np.array([1 / current[0], 0])
    return (
        current
        + np.multiply(np.array(sigma) / 2, nabla_log_pi)
        + np.multiply(np.array(sigma), np.random.randn(2))
    )


def local_opt_acceptance_probability(R, current, proposed, sigma):
    """Acceptance probability for proposed transition.

    Local optimization proposal.
    """
    if proposed[0] > R or proposed[0] < 0:
        return 0
    else:
        pass

    if proposed[1] > 2 * np.pi or proposed[1] < 0:
        return 0
    else:
        pass

    nabla_log_pi = np.array([1 / current[0], 0])
    acceptance_ratio_1 = proposed[0] / current[0]
    # acceptance_ratio_2_1 = np.exp(
    #     -np.linalg.norm(current - proposed - sigma / 2 * np.array([1 / proposed[0], 0]))
    #     ** 2
    #     / (2 * sigma**2)
    # )
    # acceptance_ratio_2_2 = np.exp(
    #     -np.linalg.norm(proposed - current - sigma / 2 * np.array([1 / current[0], 0]))
    #     ** 2
    #     / (2 * sigma**2)
    # )

    acceptance_ratio_2 = acceptance_ratio_2_1 / acceptance_ratio_2_2
    acceptance_ratio = acceptance_ratio_1 * acceptance_ratio_2

    return np.min([1, acceptance_ratio])
