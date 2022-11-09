"""Script to draw samples of a uniform distribution on a disc.

Metropolis-Hastings version.
"""

import numpy as np
import pandas as pd
import altair as alt


def proposal(x, sigma):
    """Random walk proposal."""
    return x + sigma * np.random.randn(2)


def acceptance_probability(R, current, proposed):
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
