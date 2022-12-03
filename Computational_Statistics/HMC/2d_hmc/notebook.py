"""Notebook: implentation of HMC on a simple 2D problem.

Sampling from a distribution for two variables that is bivariate Gaussian, with mean zero, standard deviations of one and correlation 0.95.

The momentum variables have a Gaussian distribution with means of zero, standard deviations of one and zero correlation.
"""

import numpy as np
import pandas as pd


class HMC:
    def __init__(
        self,
        mean_target,
        covar_matrix_target,
        mean_momentum,
        covar_matrix_momentum,
        step_size,
        num_steps,
    ):
        # Define the target distribution
        self.mean_target = mean_target
        self.covar_matrix_target = covar_matrix_target

        # Define the momentum distribution
        self.mean_momentum = np.array([0, 0])
        self.covar_matrix_momentum = np.array([[1, 0], [0, 1]])


# Define the Hamiltonian


def Hamiltonian(position, momentum):
    """Return the Hamiltonian for the bivariate Gaussian distribution.

    Args:
        position (np.array): position vector
        momentum (np.array): momentum vector

    Returns:
        float: Hamiltonian
    """
    kinetic = -0.5 * np.dot(momentum, momentum)
    potential = -0.5 * np.dot(position, np.dot(covar_matrix_target, position))
    return kinetic + potential


# Define the target distribution
mean_target = np.array([0, 0])
covar_matrix_target = np.array([[1, 0.95], [0.95, 1]])

# Define the momentum distribution
mean_momentum = np.array([0, 0])
covar_matrix_momentum = np.array([[1, 0], [0, 1]])
