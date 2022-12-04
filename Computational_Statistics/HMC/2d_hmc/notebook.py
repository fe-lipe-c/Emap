"""Notebook: implentation of HMC on a simple 2D problem.

Sampling from a distribution for two variables that is bivariate Gaussian, with
mean zero, standard deviations of one and correlation 0.95.

The momentum variables have a Gaussian distribution with means of zero,
standard deviations of one and zero correlation.
"""

import numpy as np
from numpy import linalg


class HMC:
    """Hamiltonian Monte Carlo Algorithm."""

    def __init__(
        self,
        mean_target,
        covar_matrix_target,
        mean_momentum,
        covar_matrix_momentum,
        step_size,
        num_steps,
    ):
        """Initialize the HMC algorithm."""
        # Define the target distribution
        self.mean_target = mean_target
        self.covar_matrix_target = covar_matrix_target

        # Define the momentum distribution
        self.mean_momentum = mean_momentum
        self.covar_matrix_momentum = covar_matrix_momentum

        # Define the step size and number of steps
        self.step_size = step_size
        self.num_steps = num_steps

    def Hamiltonian(self, position, momentum):
        """Return the Hamiltonian for the bivariate Gaussian distribution.

        Args:
            position (np.array): position vector
            momentum (np.array): momentum vector

        Returns:
            float: Hamiltonian
        """
        kinetic = 0.5 * np.dot(momentum, momentum)
        potential = 0.5 * np.dot(
            position,
            np.dot(
                np.linalg.inv(self.covar_matrix_target),
                position,
            ),
        )
        return kinetic + potential

    def leapfrog_steps(self, position, momentum):
        """Perform a single leapfrog step.

        Args:
            position (np.array): position vector
            momentum (np.array): momentum vector

        Returns:
            tuple: position and momentum vectors
        """
        # Update momentum
        momentum = momentum - 0.5 * self.step_size * np.dot(
            np.linalg.inv(self.covar_matrix_target),
            position,
        )

        for i in range(self.num_steps):
            # Update position
            position = position + self.step_size * np.dot(
                np.linalg.inv(self.covar_matrix_momentum), momentum
            )

            # Update momentum
            if i != self.num_steps - 1:
                momentum = momentum - self.step_size * np.dot(
                    linalg.inv(self.covar_matrix_target),
                    position,
                )
            else:
                momentum = momentum - 0.5 * self.step_size * np.dot(
                    linalg.inv(self.covar_matrix_target),
                    position,
                )
                momentum = -momentum

        return position, momentum

    def sample(self, num_samples):
        """Sample from the target distribution.

        Args:
            num_samples (int): number of samples

        Returns:
            np.array: samples
        """
        # Initialize the samples
        samples = np.zeros((num_samples, 2))

        # Initialize the position and momentum
        position = np.random.multivariate_normal(
            self.mean_target, self.covar_matrix_target
        )
        momentum = np.random.multivariate_normal(
            self.mean_momentum, self.covar_matrix_momentum
        )

        # Initialize the acceptance rate
        acceptance_rate = 0

        for i in range(num_samples):
            # Store the current position and momentum
            current_position = position
            current_momentum = momentum

            # Perform leapfrog steps
            position, momentum = self.leapfrog_steps(position, momentum)

            # Compute the acceptance probability
            acceptance_probability = np.exp(
                self.Hamiltonian(current_position, current_momentum)
                - self.Hamiltonian(position, momentum)
            )

            # Accept or reject the sample
            if np.random.rand() < acceptance_probability:
                acceptance_rate += 1
            else:
                position = current_position

            # Store the sample
            samples[i] = position

        # Compute the acceptance rate
        acceptance_rate /= num_samples

        return samples, acceptance_rate


# Define the target distribution
mean_target = np.array([0, 0])
covar_matrix_target = np.array([[1, 0.95], [0.95, 1]])

# Define the momentum distribution
mean_momentum = np.array([0, 0])
covar_matrix_momentum = np.array([[1, 0], [0, 1]])

# Algorithm hyperparameters
epsilon = 0.25
steps = 25
samples = 1000

# Run the algorithm
hmc_samples, acceptance_rate = HMC(
    mean_target,
    covar_matrix_target,
    mean_momentum,
    covar_matrix_momentum,
    epsilon,
    steps,
).sample(samples)

hmc_samples
acceptance_rate
