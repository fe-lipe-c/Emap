"""Notebook of the Euler's method implementation.

We have the following Hamiltonian:
H(q,p) = U(q) + K(p)
U(q) = (q^2)/2
K(p) = (p^2)/2

The resulting dynamics is:
dq/dt = p and dp/dt = -q

Thus, the solution is:
q(t) = r*cos(t + a) and p(t) = -r*sin(t + a)
"""

import numpy as np
import pandas as pd
import altair as alt

iterations = 20
current_q = 0
current_p = 1
step_size = 0.3


def dynamics(q, p):
    """Dynamics of the system."""
    new_q = q + step_size * p
    new_p = p - step_size * q
    return new_q, new_p


q_path = [current_q]
p_path = [current_p]

for t in range(iterations):
    new_q, new_p = dynamics(q_path[-1], p_path[-1])
    q_path.append(new_q)
    p_path.append(new_p)

df_path = pd.DataFrame({"q": q_path, "p": p_path})
df_path["t"] = df_path.index

chart_path = (
    alt.Chart(df_path)
    .mark_line(point=True)
    .encode(
        alt.X(
            "q",
        ),
        alt.Y("p"),
        order="t",
    )
    .properties(width=800, height=800)
)
chart_path.save("path.html")
