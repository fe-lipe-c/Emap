"""Notebook for Assignment 1."""

import numpy as np
import pandas as pd
import altair as alt

from uniform_disc import uniform_disc_dist, mc_mean_distance, expected_distance
from MH_uniform_disc import acceptance_probability, proposal
from circle import circle, plot_circle

# Part 1, exercise 3

# x = [0, 0.5]
# y = [0, 0.5]
# radius = [1, 1]
# color = ["red", "blue"]
# nr_points = 1000
#
# chart_0 = plot_circle(x[0], y[0], radius[0], color[0], nr_points)
# chart_1 = plot_circle(x[1], y[1], radius[1], color[1], nr_points)
#
# df_center_0 = pd.DataFrame({"x": x[0], "y": y[0]}, index=[0])
# chart_center_0 = (
#     alt.Chart(df_center_0)
#     .mark_circle(size=100, color="red")
#     .encode(alt.X("x"), alt.Y("y"))
# )
# df_center_1 = pd.DataFrame({"x": x[1], "y": y[1]}, index=[0])
# chart_center_1 = (
#     alt.Chart(df_center_1)
#     .mark_circle(size=100, color="blue")
#     .encode(alt.X("x"), alt.Y("y"))
# )

# chart_t = chart_0 + chart_1 + chart_center_0 + chart_center_1
# chart_t.save("circle_int.html")

# Simulate using the inverse method

seed = 1
radius = 1000

mc_dist = mc_mean_distance(
    uniform_disc_dist(4000, radius, seed=seed),
    uniform_disc_dist(4000, radius, seed=seed + 1),
)

mc_dist

true_mean = expected_distance(radius)
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


# Simulate through Metropolis-Hastings

R = 10
sigma_proposal = R / 10
p_current = np.array([R / 2, 1])
size = 40000

MH_sample = [p_current]  # Initialize the chain with the initial state
for step in range(size):

    p_proposed = proposal(MH_sample[-1], sigma_proposal)
    a_prob = acceptance_probability(R, MH_sample[-1], p_proposed)
    points_vector = [MH_sample[-1], p_proposed]
    next_index = np.random.choice([0, 1], p=[1 - a_prob, a_prob])
    x_next = points_vector[next_index]
    MH_sample.append(x_next)

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
