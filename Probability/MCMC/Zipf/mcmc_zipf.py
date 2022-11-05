"""Metropolis-Hastings algorithm for Zipf's law."""

import numpy as np


def proposal(probability, M):
    """Proposal distribution.

     Markov birth-death process with rates (p) of birth and (1-p) of death.

     Parameters
     ----------
    probability : float
         Birth probability.
    M : int
         Number of states.

     Returns
     -------
     np.array
         Proposed probability transition function.
    """
    transition = np.zeros((M, M))

    for i in range(1, M - 1):
        transition[i, i + 1] = probability
        transition[i, i - 1] = 1 - probability
        transition[i, i] = 0

    transition[0, 1] = probability
    transition[0, 0] = 1 - probability
    transition[M - 1, M - 2] = 1 - probability
    transition[M - 1, M - 1] = probability

    return transition


def acceptance_probability(parameter, current, proposed):
    """Acceptance probability for proposed transition.

    Parameters
    ----------
    transition : np.array
        Probability transition function.
    current : int
        Current state.
    proposed : np.array
        Proposed state.

    Returns
    -------
    float
        Acceptance probability.
    """
    acceptance_ratio = (current**parameter) / (proposed**parameter)
    return np.min([1, acceptance_ratio])
