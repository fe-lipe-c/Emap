"""Notebook: implentation of HMC on a simple 2D problem.

Sampling from a distribution for two variables that is bivariate Gaussian, with
mean zero, standard deviations of one and correlation 0.95.

The momentum variables have a Gaussian distribution with means of zero,
standard deviations of one and zero correlation.
"""

import numpy as np
import altair as alt
import pandas as pd
from utils import HMC  # , plot_contour, plot_samples, plot_path

# Define the target distribution
mean_target = np.array([0, 0])
covar_matrix_target = np.array([[1, 0.95], [0.95, 1]])

# Define the momentum distribution
mean_momentum = np.array([0, 0])
covar_matrix_momentum = np.array([[1, 0], [0, 1]])

# Algorithm hyperparameters
epsilon = 0.25
steps = 15
samples = 8

# Run the algorithm

hmc = HMC(
    mean_target,
    covar_matrix_target,
    mean_momentum,
    covar_matrix_momentum,
    epsilon,
    steps,
)

s, m, h, a = hmc.sample(samples)
hmc.plot(s, m, h)

hmc_samples = hmc.leapfrog_path[0]

df_hmc_samples = pd.DataFrame(hmc_samples, columns=["x", "y"])
chart_samples = hmc.plot_samples(df_hmc_samples, color="red")
chart_contour = hmc.plot_contour(
    mean_target, covar_matrix_target, color_scheme="darkgreen"
)
total_samples = chart_contour + chart_samples
# total_samples.save("contour_samples.html")

chart_path = plot_path(df_hmc_samples, color="red")
total_path = chart_contour + chart_path
# total_path.save("contour_samples_path.html")

total = total_samples | total_path

total_path.save("leapfrog_path.html")


def plot_path(df_samples, color="red"):
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
        .properties(width=800, height=800)
    )

    return chart_path
