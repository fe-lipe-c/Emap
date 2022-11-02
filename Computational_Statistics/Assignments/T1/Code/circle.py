"""Script to make a circle."""
# https://stackoverflow.com/questions/56719988/altair-plot-circle-ellipse-annotations-in-faceted-chart

import pandas as pd
import numpy as np
import altair as alt

# make some data to test

N = 1000
df = pd.DataFrame(
    {
        "x1": np.random.normal(0, 1, N),
        "x2": np.random.normal(0, 1, N),
        "facet": np.random.choice(["a", "b", "c"], N),
    }
)

# derived variables
df["y1"] = np.where(np.sqrt(df["x1"] ** 2 + df["x2"] ** 2) > 2, "f", "p")
df["y2"] = 0.5 * df["x2"] + 2 + np.random.normal(0.5, N)
df["color"] = np.where(df["y1"].eq("f"), "red", "green")

# custom color map
domain = ["f", "p"]
range_ = ["red", "green"]

# create and render chart
base_chart = (
    alt.Chart(df)
    .mark_circle(opacity=1, size=15)
    .encode(
        alt.X("x1", scale=alt.Scale(domain=(-4, 4))),
        alt.Y("x2", scale=alt.Scale(domain=(-4, 4))),
        color=alt.Color("y1", scale=alt.Scale(domain=domain, range=range_)),
        facet=alt.Facet("facet", columns=3),
    )
    .properties(width=200, height=200)
    .resolve_scale(color="independent")
)

base_chart.save("circle.html")
