"""Exercise 2.

For each of the following cases, generate random variables Xi Yi and
compute the average and variance of the "vanilla"
Monte Carlo and Rao-Blackwellised estimators:
"""

import numpy as np
from gamma import gamma_dist
from general_tools import plot_density_nparams

# (a)
# Y follows a Gamma(a,b)
# X follows a Negative-Binomial(a,1/(b+1))
# 	&= \binom{x+a-1}{x} \left(\frac{1}{b+1}\right)^{x}\left(\frac{b}{b+1}\right)^{a}\
# 	\end{split}
# \end{equation}
# $$
# where in (*) we use constant equal to one to obtain a distribution Gamma(x+a,b+1) and integrate it to the unit and in (**) the fact that $\Gamma(x)= (x-1)!$. Then $\pi$ is Negative-Binomial$\left(a,\frac{1}{b+1}\right)$.

a = [1, 2, 3, 5, 9, 15, 25, 50, 100]
b = [1, 2, 2, 1, 1, 3, 5, 9, 15]
size = 100000

gamma_rv_list = []

for param in zip(a, b):

    gamma_rv = gamma_dist(param[0], param[1], size)
    gamma_rv_list.append(gamma_rv)

# plot_density(exp_truncated_list[1], "exp_truncated_rv (a = 10)", "exp_truncated")
plot_density_nparams(gamma_rv_list, zip(a, b), "gamma_rv")
