"""Computational Statistics: Assignment Simulation.

For each R in {0.01, 0.1, 1, 10, 100, 1000 ,10000 }, perform M =500 runs from
your simulation method and compute:

(i) variance
(ii) bias
(iii) standard deviation of the mean (MCSE): sqrt(1/N * [S**4(kurtosis-1)+4*S**3*skewness(mean-I)+4 * S**2(mean-I)**2])
"""

import numpy as np
import pandas as pd
import altair as alt
from scipy.stats import kurtosis, skew
import time

from MH_uniform_disc import rw_proposal, rw_acceptance_probability

R = [0.01, 0.1, 1, 10, 100, 1000, 10000]
M = 500
size = 10000

sample_bias = []
sample_variance = []
sample_mse_mcse = []

start_time = time.time()
for radius in R:

    print(radius)

    R_sample_bias = []
    R_sample_variance = []
    R_sample_mse = []

    sigma_proposal = [0.1 * radius, 0.5]
    true_value = (128 / (45 * np.pi)) * radius

    for i in range(M):

        p_current = np.array(
            [np.random.uniform(0, radius), np.random.uniform(0, 2 * np.pi)]
        )
        MH_sample = [p_current]  # Initialize the chain with the initial state

        for step in range(size):

            p_proposed = rw_proposal(MH_sample[-1], sigma_proposal)
            a_prob = rw_acceptance_probability(radius, MH_sample[-1], p_proposed)
            points_vector = [MH_sample[-1], p_proposed]
            next_index = np.random.choice([0, 1], p=[1 - a_prob, a_prob])
            x_next = points_vector[next_index]
            MH_sample.append(x_next)

        MH_sample = np.array(MH_sample)
        x_axis = MH_sample[:, 0] * np.cos(MH_sample[:, 1])
        y_axis = MH_sample[:, 0] * np.sin(MH_sample[:, 1])
        MH_points = np.array([x_axis, y_axis]).T

        points_distances = np.linalg.norm(
            MH_points[1 : int(size / 2) + 1] - MH_points[int(size / 2) + 1 :], axis=1
        )

        # R_sample_bias.append(np.sqrt(np.var(points_distances) / size))
        R_sample_bias.append(np.mean(points_distances) - true_value)
        R_sample_variance.append(np.var(points_distances))
        # standard deviation of the mean
        R_sample_mse.append(np.mean((points_distances - true_value) ** 2))
        # R_sample_mse_mcse.append(
        #     np.sqrt(
        #         1
        #         / size
        #         * (
        #             np.std(points_distances) ** 4 * (kurtosis(points_distances) - 1)
        #             + 4
        #             * np.std(points_distances) ** 3
        #             * skew(points_distances)
        #             * (np.mean(points_distances) - true_value)
        #             + 4
        #             * np.std(points_distances) ** 2
        #             * (np.mean(points_distances) - true_value) ** 2
        #         )
        #     )
        # )
    sample_bias.append(R_sample_bias)
    sample_variance.append(R_sample_variance)
    sample_mse_mcse.append(R_sample_mse)

end_time = time.time()
total_time = end_time - start_time

total_time
sample_bias[2]
sample_mse_mcse[3]
sample_variance[3]

# for eache radius R, make a column for each: bias, variance, mse_mcse
for i in range(len(R)):
    df = pd.DataFrame(
        {
            "bias": sample_bias[i],
            "variance": sample_variance[i],
            "mse": sample_mse_mcse[i],
        }
    )
    df.to_csv("R_{}_results_final.csv".format(R[i]), index=False)

df_bias_100 = pd.read_csv("R_100_results.csv")

# create a data frame with the mean result for each R of the bias, variance, mse_mcse
df_mean_performance = pd.DataFrame(columns=["R", "bias", "variance", "mse"])
for i in range(len(R)):
    df = pd.read_csv("R_{}_results_final.csv".format(R[i]))
    df_mean_performance.loc[i] = [
        R[i],
        df["bias"].mean(),
        df["variance"].mean(),
        df["mse"].mean(),
    ]


df_mean_performance

# transform dataframe in latex
df_mean_performance.to_latex(index=False)

mh_chart = (
    alt.Chart(df)
    .mark_circle(size=10)
    .encode(
        alt.X("x"),
        alt.Y("y"),
    )
)
mh_chart.save("MH_uniform_disc.html")

np.random.uniform(0, 2 * np.pi)
np.array([1, 2]) - 2
