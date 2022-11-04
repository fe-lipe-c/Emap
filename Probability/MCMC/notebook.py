"""Notebook with MCMC examples from the book 'Introduction to Probability'."""

import numpy as np
import pandas as pd

from zipf_pmf import zipf_rvs
from general_tools import plot_density_nparams

states = 20
parameter_a = [1, 2, 3]
size = 1000
seed = 10

# z_rvs = zipf_rvs(M=states, a=parameter_a[0], size=size, seed=seed)
#
# z_rvs

zipf_rv_list = []

for param in zip(parameter_a):

    z_rvs = zipf_rvs(M=states, a=param[0], size=size, seed=seed)
    zipf_rv_list.append(z_rvs)

plot_density_nparams(zipf_rv_list, zip(parameter_a), "zipf_rv")
