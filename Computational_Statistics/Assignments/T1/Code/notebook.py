"""Notebook for Assignment 1."""

import numpy as np
import altair as alt

from uniform_disc import uniform_disc_dist, mc_mean_distance, expected_distance


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
