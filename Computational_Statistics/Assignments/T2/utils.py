"""Implementation of Hamiltonian Monte Carlo and random-walk Metropolis."""
from scipy.stats import multivariate_normal
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
        self.step_size = np.random.uniform(0.0104, 0.0156, 1)
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
        samples = np.zeros((num_samples, 100))
        momentums = np.zeros((num_samples, 100))
        hamiltonians = np.zeros(num_samples)

        # Initialize the position and momentum
        position = np.random.multivariate_normal(
            self.mean_target, self.covar_matrix_target
        )
        # momentum = np.random.multivariate_normal(
        #     self.mean_momentum, self.covar_matrix_momentum
        # )

        # Initialize the acceptance rate
        acceptance_rate = 0

        for i in range(num_samples):
            # Store the current position and momentum
            momentum = np.random.multivariate_normal(
                self.mean_momentum, self.covar_matrix_momentum
            )
            current_position = position
            current_momentum = momentum
            hamiltonians[i] = self.Hamiltonian(current_position, current_momentum)

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
            momentums[i] = momentum

        # Compute the acceptance rate
        acceptance_rate /= num_samples

        return samples, momentums, hamiltonians, acceptance_rate


class MHRW:
    """Random-walk Metropolis"""

    def __init__(self, mean_target, cov_matrix_target):
        """Metropolis-Hastings random-walk."""
        self.cov_matrix_target = cov_matrix_target
        self.mean_target = mean_target

    def rw_proposal(self, q):
        """Random walk proposal."""
        std_dev = np.random.uniform(0.0176, 0.0264, 100)
        w = np.random.normal(0, std_dev, 100)
        return q + w

    def target(self, q):
        """Target distribution."""
        return multivariate_normal.pdf(q, cov=self.cov_matrix_target)

    def rw_acceptance_probability(self, current, proposed):
        """Acceptance probability for proposed transition."""

        acceptance_ratio = self.target(proposed) / self.target(current)
        return np.min([1, acceptance_ratio])

    def run(self, size):
        """Run algorithm."""

        q_current = np.random.multivariate_normal(
            self.mean_target, self.cov_matrix_target
        )
        MH_sample = [q_current]  # Initialize the chain with the initial state

        for step in range(size):

            q_proposed = self.rw_proposal(MH_sample[-1])
            a_prob = self.rw_acceptance_probability(MH_sample[-1], q_proposed)
            points_vector = [MH_sample[-1], q_proposed]
            next_index = np.random.choice([0, 1], p=[1 - a_prob, a_prob])
            x_next = points_vector[next_index]
            MH_sample.append(x_next)

        return np.array(MH_sample)
