"""Notebook: implentation of 100-Dimensional Distribution.

Sampling from a distribution for 100-dimensional multivariate independent
Gaussian, with mean zero, standard deviations going from 0.01 up to 1.00,
in 0.01 increments.

The momentum variables have a Gaussian distribution with means of zero,
standard deviations of one and zero correlation.
"""

import numpy as np
import pandas as pd
from utils import HMC, MHRW  # , plot_contour, plot_samples, plot_path
import altair as alt

# HAMILTONIAN MONTE CARLO

# Define the target distribution
mean_target = np.zeros(100)
covar_matrix_target = np.diag(np.linspace(0.01, 1.00, 100))

# Define the momentum distribution
mean_momentum = np.zeros(100)
covar_matrix_momentum = np.diag(np.ones(100))

# Algorithm hyperparameters
# epsilon = np.random.uniform(0.0104, 0.0156, 1)
steps = 150
samples = 1000

# Run the algorithm

hmc = HMC(
    mean_target,
    covar_matrix_target,
    mean_momentum,
    covar_matrix_momentum,
    steps,
)

s, m, h, a = hmc.sample(samples)
# hmc.plot(s, m, h)


# Dataframe with the last coordinate for each sample
df_s_last = pd.DataFrame(s[:, -1], columns=["last_coordinate"])
df_s_last["index"] = df_s_last.index

chart_samples = (
    alt.Chart(df_s_last)
    .mark_circle(color="red", size=50)
    .encode(alt.X("index"), alt.Y("last_coordinate"))
    .properties(width=800, height=600)
)
chart_samples.save("chart_samples.html")

# METROPOLIS-HASTINGS RANDOM WALK

mhrw = MHRW(mean_target, covar_matrix_target, samples)

mhrw_samples = mhrw.run(samples)

# Dataframe with the last coordinate for each sample
df_s_last = pd.DataFrame(mhrw_samples[:, -1], columns=["last_coordinate"])
df_s_last["index"] = df_s_last.index

chart_samples = (
    alt.Chart(df_s_last)
    .mark_circle(color="red", size=50)
    .encode(alt.X("index"), alt.Y("last_coordinate"))
    .properties(width=800, height=600)
)
chart_samples.save("chart_samples_mhrw.html")
