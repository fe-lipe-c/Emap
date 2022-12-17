"""General tools for the project."""

from scipy.stats import multivariate_normal
import altair as alt
import pandas as pd
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

        # Save leapfrog path
        self.leapfrog_path = []

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

        path = []
        for i in range(self.num_steps):
            # Update position
            position = position + self.step_size * np.dot(
                np.linalg.inv(self.covar_matrix_momentum), momentum
            )
            path.append(position)

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

        self.leapfrog_path.append(path)
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
        momentums = np.zeros((num_samples, 2))
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

    def plot_contour(self, mean, cov, n=100, color_scheme="viridis"):
        """Create a grid of points at which to evaluate the density of the bivariate Gaussian."""

        x, y = np.mgrid[-4:4:100j, -4:4:100j]
        positions = np.vstack([x.ravel(), y.ravel()])

        density = multivariate_normal.pdf(positions.T, mean, cov)
        density = pd.DataFrame({"x": x.ravel(), "y": y.ravel(), "z": density})

        chart_contour = (
            alt.Chart(density)
            .mark_rect()
            .encode(
                alt.X("x:Q", title="x", bin=alt.Bin(maxbins=70)),
                alt.Y("y:Q", title="y", bin=alt.Bin(maxbins=70)),
                alt.Color("z:Q", scale=alt.Scale(scheme=color_scheme)),
            )
        )

        return chart_contour

    def plot_samples(self, df_samples, color="red"):
        """Plot the samples."""
        chart_samples = (
            alt.Chart(df_samples)
            .mark_circle(size=55, color=color)
            .encode(
                x="x",
                y="y",
            )
        )

        return chart_samples

    def plot_path(self, df_samples, color="red"):
        """Plot the path of the samples."""
        df_samples["index"] = df_samples.index
        chart_path = (
            alt.Chart(df_samples)
            .mark_line(
                color=color,
                point={"filled": False, "fill": "white"},
                opacity=0.8,
                strokeDash=[5, 5],
            )
            .encode(
                x="x",
                y="y",
                order="index",
            )
        )

        return chart_path

    def plot(self, hmc_samples, hmc_momentums, hamiltonians):
        """Plot distributions for the position and momentum."""
        # Plot position results
        df_hmc_samples = pd.DataFrame(hmc_samples, columns=["x", "y"])
        chart_samples = self.plot_samples(df_hmc_samples, color="red")
        chart_contour = self.plot_contour(
            self.mean_target, self.covar_matrix_target, color_scheme="darkgreen"
        )
        total_samples = chart_contour + chart_samples
        # total_samples.save("contour_samples.html")

        chart_path = self.plot_path(df_hmc_samples, color="red")
        total_path = chart_contour + chart_path
        # total_path.save("contour_samples_path.html")

        total = total_samples | total_path
        # total.save("samples_plus_path.html")

        # Plot momentum results
        df_hmc_momentum = pd.DataFrame(hmc_momentums, columns=["x", "y"])
        chart_momentum = self.plot_samples(df_hmc_momentum, color="red")
        chart_contour_momentum = self.plot_contour(
            self.mean_momentum,
            self.covar_matrix_momentum,
            color_scheme="darkgreen",
        )
        total_momentum = chart_contour_momentum + chart_momentum
        # total_momentum.save("contour_momentum.html")

        chart_momentum_path = self.plot_path(df_hmc_momentum, color="red")
        total_momentum_path = chart_contour_momentum + chart_momentum_path
        # total_momentum_path.save("contour_momentum_path.html")

        total_m = total_momentum | total_momentum_path
        # total_m.save("momentum_plus_path.html")

        df_hmc_hamiltonians = pd.DataFrame(hamiltonians, columns=["Hamiltonian"])
        df_hmc_hamiltonians["Iteration"] = df_hmc_hamiltonians.index
        chart_ham = (
            alt.Chart(df_hmc_hamiltonians)
            .mark_line(point=True)
            .encode(
                x="Iteration",
                y="Hamiltonian",
            )
        ).properties(width=1000, height=500)
        chart_m_s = total & total_m & chart_ham
        chart_m_s.properties(width=1000, height=500)
        chart_m_s.save("momentum_samples.html")
