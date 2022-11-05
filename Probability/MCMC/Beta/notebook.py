"""Beta Simulation."""

from beta_unif import beta_dist
from general_tools import plot_density_nparams

a = [5, 1, 2]
b = [1, 3, 2]
size = 1000
seed = 1

beta_rv_list = []

for param in zip(a, b):

    beta_rvs = beta_dist(a=param[0], b=param[1], size=size, seed=seed)
    beta_rv_list.append(beta_rvs)

plot_density_nparams(beta_rv_list, zip(a, b), "beta_unif_rv", step=0.01)
