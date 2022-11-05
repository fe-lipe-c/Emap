"""Beta Simulation."""

import numpy as np

from beta_unif import beta_dist
from mcmc_beta import acceptance_probability, proposal
from general_tools import plot_density_nparams

# Beta distribution using uniform rvs.

a = [5, 1, 2]
b = [1, 3, 2]
size = 1000
seed = 1

beta_rv_list = []

for param in zip(a, b):

    beta_rvs = beta_dist(a=param[0], b=param[1], size=size, seed=seed)
    beta_rv_list.append(beta_rvs)

plot_density_nparams(beta_rv_list, zip(a, b), "beta_unif_rv", step=0.01)

# Generate Beta random variables using the Metropolis-Hastings algorithm

a = [5, 1, 2]
b = [1, 3, 2]
size = 1000
seed = 1

beta_MH_list = []

for param in zip(a, b):
    x_init = 0.5  # Initial state
    MH_sample = [x_init]  # Initialize the chain with the initial state
    for step in range(size):

        x_proposed = proposal()  # Propose a new state
        a_prob = acceptance_probability(param[0], param[1], MH_sample[-1], x_proposed)
        x_next = np.random.choice([MH_sample[-1], x_proposed], p=[1 - a_prob, a_prob])
        MH_sample.append(x_next)

    beta_MH_list.append(np.array(MH_sample))

plot_density_nparams(beta_MH_list, zip(a, b), "beta_MH", step=0.01)
a
