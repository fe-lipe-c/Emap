"""Notebook."""

import altair as alt
import pandas as pd

from brownian_motion import brownian_motion
from brownian_bridge import brownian_bridge
from brownian_exp_time import bm_exp_time


# Brownian Motion

bmotion = brownian_motion(delta_t=10000)

df_bm = pd.DataFrame(bmotion, columns=["Bt"])
df_bm["index"] = df_bm.index

df_chart = alt.Chart(df_bm).mark_line().encode(alt.X("index:Q"), alt.Y("Bt:Q"))
df_chart.save("b_motion.html")

# Brownian Bridge

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

# Yx = Bx, where x ~ exp(lambda), x independent of Bt

Et = bm_exp_time(delta_t=1000)

df_exp = pd.DataFrame(Et, columns=["Bt"])
df_exp["index"] = df_exp.index

df_chart = (
    alt.Chart(df_exp)
    .mark_line()
    .encode(alt.X("index:Q"), alt.Y("Bt:Q"))
    .properties(width=800, height=400)
)
df_chart.save("bmexp_motion.html")
