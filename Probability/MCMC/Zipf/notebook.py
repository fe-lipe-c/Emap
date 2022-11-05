"""Notebook with MCMC examples from the book 'Introduction to Probability'."""

import numpy as np
import pandas as pd

from zipf_pmf import zipf_rvs
from mcmc_zipf import proposal, acceptance_probability
from general_tools import plot_density_nparams

# Generate Zipf random variables directly from the PMF

states = 10
parameter_a = [1, 2, 3]
size = 1000
seed = 10

zipf_rv_list = []

for param in zip(parameter_a):

    z_rvs = zipf_rvs(M=states, a=param[0], size=size, seed=seed)
    zipf_rv_list.append(z_rvs)

plot_density_nparams(zipf_rv_list, zip(parameter_a), "zipf_rv")

# Generate Zipf random variables using the Metropolis-Hastings algorithm

states = 10
parameter_a = [1, 2, 3]
size = 10000
probability = 0.5  # Probability of birth
T = proposal(probability, states)  # Transition matrix

zipf_MH_list = []

for param in zip(parameter_a):
    x_init = 10  # Initial state
    MH_sample = [x_init]  # Initialize the chain with the initial state
    for step in range(size):

        x_proposed = np.random.choice(states, p=T[MH_sample[-1] - 1, :]) + 1
        a = acceptance_probability(param[0], MH_sample[-1], x_proposed)
        x_next = np.random.choice([MH_sample[-1], x_proposed], p=[1 - a, a])
        MH_sample.append(x_next)

    zipf_MH_list.append(np.array(MH_sample))

plot_density_nparams(zipf_MH_list, zip(parameter_a), "zipf_MH")
