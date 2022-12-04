"""Script to make a circle."""

import pandas as pd
import numpy as np
import altair as alt


def ellipse(center, radius, points):
    """Create a circle.

    center: center of the circle
    radius: radius of the circle
    points: number of points to use to create the ellipse
    """
    theta = np.linspace(0, 2 * np.pi, points)
    df_circle = pd.DataFrame(
        {
            "x": center[0] + radius[0] * np.cos(theta),
            "y": center[1] + radius[1] * np.sin(theta),
        }
    )
    df_circle["index"] = df_circle.index
    return df_circle


def plot_ellipse(center, radius, color, points):
    """Plot a circle."""
    c = ellipse(center, radius, points)
    chart_circle = (
        alt.Chart(c)
        .mark_line(color=color, strokeDash=[5, 5])
        .encode(
            alt.X(
                "x",
                scale=alt.Scale(domain=[-max(radius) - 2, max(radius) + 2]),
            ),
            alt.Y(
                "y",
                scale=alt.Scale(domain=[-max(radius) - 2, max(radius) + 2]),
            ),
            order="index",
        )
    )

    return chart_circle
