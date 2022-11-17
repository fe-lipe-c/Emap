import numpy as np
import pandas as pd
import altair as alt
import time

from uniform_disc import uniform_disc_dist, mc_mean_distance, true_expected_distance
from MH_uniform_disc import (
    rw_acceptance_probability,
    rw_proposal,
    local_opt_acceptance_probability,
    local_opt_proposal,
)

# Simulate using the inverse method

seed = 1
radius = 10000

mc_dist = mc_mean_distance(
    uniform_disc_dist(4000, radius, seed=seed),
    uniform_disc_dist(4000, radius, seed=seed + 1),
)

mc_dist

true_mean = true_expected_distance(radius)
true_mean

# chart_circle = (
#     alt.Chart(rand_points)
#     .mark_circle(size=10)
#     .encode(
#         alt.X("x:Q"),
#         alt.Y("y:Q"),
#     )
# )
# chart_circle.save("uniform_disc.html")


# Simulate through Metropolis-Hastings: random walk proposal

R = 10000
sigma_proposal = [0.1 * R, 0.5]
p_current = np.array([R / 2, 1])
size = 10000

start_time = time.time()
MH_sample = [p_current]  # Initialize the chain with the initial state
for step in range(size):

    p_proposed = rw_proposal(MH_sample[-1], sigma_proposal)
    a_prob = rw_acceptance_probability(R, MH_sample[-1], p_proposed)
    points_vector = [MH_sample[-1], p_proposed]
    next_index = np.random.choice([0, 1], p=[1 - a_prob, a_prob])
    x_next = points_vector[next_index]
    MH_sample.append(x_next)

end_time = time.time()
total_time = end_time - start_time

total_time

MH_sample = np.array(MH_sample)
x_axis = MH_sample[:, 0] * np.cos(MH_sample[:, 1])
y_axis = MH_sample[:, 0] * np.sin(MH_sample[:, 1])

df = pd.DataFrame({"x": x_axis, "y": y_axis})

mh_chart = (
    alt.Chart(df)
    .mark_circle(size=10)
    .encode(
        alt.X("x"),
        alt.Y("y"),
    )
)
mh_chart.save("MH_uniform_disc.html")

# Simultating through Metropolis-Hastings: local optimization proposal

R = 10000
sigma_proposal = 0.1 * R
p_current = np.array([R / 2, 1])
size = 1000000

start_time = time.time()
MH_sample = [p_current]  # Initialize the chain with the initial state
for step in range(size):

    p_proposed = local_opt_proposal(MH_sample[-1], sigma_proposal)
    a_prob = local_opt_acceptance_probability(
        R, MH_sample[-1], p_proposed, sigma_proposal
    )
    points_vector = [MH_sample[-1], p_proposed]
    next_index = np.random.choice([0, 1], p=[1 - a_prob, a_prob])
    x_next = points_vector[next_index]
    MH_sample.append(x_next)

end_time = time.time()
total_time = end_time - start_time

total_time

MH_sample = np.array(MH_sample)
x_axis = MH_sample[:, 0] * np.cos(MH_sample[:, 1])
y_axis = MH_sample[:, 0] * np.sin(MH_sample[:, 1])

df = pd.DataFrame({"x": x_axis, "y": y_axis})

mh_chart = (
    alt.Chart(df)
    .mark_circle(size=10)
    .encode(
        alt.X("x"),
        alt.Y("y"),
    )
)
mh_chart.save("MH_uniform_disc_local_opt.html")

MH_sample[-1]
sigma_proposal
teste = np.random.randn(2)
teste
np.multiply(sigma, teste)

sigma = np.array([2, 2])
npkk
