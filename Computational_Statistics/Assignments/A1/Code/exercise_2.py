"""Exercise 2.

For each of the following cases, generate random variables Xi Yi and
compute the average and variance of the "vanilla"
Monte Carlo and Rao-Blackwellised estimators:
"""

import numpy as np

# (a)
# Y follows a Gamma(a,b)
# X follows a Negative-Binomial(a,1/(b+1))

X = np.random.negative_binomial(a, 1 / (b + 1), 1000)
Y = np.random.gamma(a, b, 1000)
