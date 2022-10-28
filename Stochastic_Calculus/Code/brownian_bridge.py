"""Brownian Bridge."""

import numpy as np
import altair as alt
import pandas as pd


def brownian_motion(delta_t=100):
    """Brownian motion with a simple random walk"""
    Bt = [0]

    for t in range(delta_t):
        et = np.random.choice([1, -1], 1, p=[0.5, 0.5])
        if et == 0:
            et = 1

        Bt.append((Bt[-1] + et))

    return Bt


def brownian_bridge(delta_t=1000):
    """Brownian bridge."""
    Bt = brownian_motion(delta_t)
    Xt = []

    for t in range(delta_t):
        Xt.append(Bt[t] - (t / delta_t) * Bt[-1])

    return Xt


# Brownian Motion

bmotion = brownian_motion(delta_t=10000)

df_bm = pd.DataFrame(bmotion, columns=["Bt"])
df_bm["index"] = df_bm.index

df_chart = alt.Chart(df_bm).mark_line().encode(alt.X("index:Q"), alt.Y("Bt:Q"))
df_chart.save("b_motion.html")

## Brownian Bridge

bbridge = brownian_bridge(delta_t=10000)

df_bb = pd.DataFrame(bbridge, columns=["Bt"])
df_bb["index"] = df_bb.index

df_chart = (
    alt.Chart(df_bb)
    .mark_line()
    .encode(alt.X("index:Q"), alt.Y("Bt:Q"))
    .properties(width=800, height=400)
)
df_chart.save("bbridge_motion.html")
