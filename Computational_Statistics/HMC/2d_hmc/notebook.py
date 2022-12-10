"""Notebook: implentation of HMC on a simple 2D problem.

Sampling from a distribution for two variables that is bivariate Gaussian, with
mean zero, standard deviations of one and correlation 0.95.

The momentum variables have a Gaussian distribution with means of zero,
standard deviations of one and zero correlation.
"""

import numpy as np
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
steps = 25
samples = 800

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
