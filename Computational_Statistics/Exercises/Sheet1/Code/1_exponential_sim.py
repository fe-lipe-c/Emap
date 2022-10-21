"""Simulation of truncated exponential distribution."""

import numpy as np
import pandas as pd
import altair as alt

from general_tools import plot_histogram, plot_histogram_nparams
from exp_truncated import exp_truncated, exp_truncated_alt

# Exercise 1
# Item 1
# Generate 10000 truncated exponential random numbers for a = [1, 10, 100] and lambda = 1

lambda_ = 1
a = [1, 10, 100]
exp_truncated_list = []

size = 10000
u = np.random.uniform(size=size)

for param in a:

    exp_trunc_rv = exp_truncated(lambda_, param, u)
    exp_truncated_list.append(exp_trunc_rv)

plot_histogram(u, "uniform_rv", "uniform")
plot_histogram(exp_truncated_list[1], "exp_truncated_rv (a = 10)", "exp_truncated")
plot_histogram_nparams(exp_truncated_list, zip(a), "exp_truncated_rv")

# Exercise 1
# Item 2
# Use the formula:
# x = - 1\lambda * ln(e^(-lambda * a) - u(e^(-lambda * a)- e^(- lambda b)))

lambda_ = 1
a = [1, 10, 100]
b = [2, 15, 1000]
exp_truncated_alt_list = []

size = 10000
u = np.random.uniform(size=size)

for param in range(len(a)):

    exp_trunc_rv = exp_truncated_alt(lambda_, a[param], b[param], u)
    exp_truncated_alt_list.append(exp_trunc_rv)

# plot_histogram(u, "uniform_rv", "uniform")
plot_histogram_nparams(exp_truncated_alt_list, zip(a, b), "exp_truncated_alt_rv")


# Test

exp_trunc_rv_1 = exp_truncated(lambda_, 1, u)

exp_trunc_rv + exp_trunc_rv_1
exp_trunc_rv_1

# array([5.96734726, 2.53192025, 3.43790101, ..., 5.2262491 , 2.07617501,
#        2.09963789])

# array([2.98367363, 1.26596013, 1.71895051, ..., 2.61312455, 1.0380875 ,
#        1.04981894])

# array([2.98367363, 1.26596013, 1.71895051, ..., 2.61312455, 1.0380875 ,
#        1.04981894])
