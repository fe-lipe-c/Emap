"""Script to make a circle."""

import pandas as pd
import numpy as np
import altair as alt


def circle(x, y, radius, points):
    """Create a circle.

    x, y: center of the circle
    """
    theta = np.linspace(0, 2 * np.pi, points)
    df_circle = pd.DataFrame(
        {
            "x": x + radius * np.cos(theta),
            "y": y + radius * np.sin(theta),
        }
    )
    df_circle["index"] = df_circle.index
    return df_circle


def plot_circle(x, y, radius, color, points):
    """Plot a circle."""
    c = circle(x, y, radius, points)
    chart_circle = (
        alt.Chart(c)
        .mark_line(color=color)
        .encode(
            alt.X("x", scale=alt.Scale(zero=False)),
            alt.Y("y", scale=alt.Scale(zero=False)),
            order="index",
        )
    )

    # chart_circle.save("circle.html")
    return chart_circle
