# Stochastic Calculus
## Stochastic Differential Equations
### List 5

**1. Solve the SDE** 
$$
\begin{equation*}
	dX_{t} = (- \alpha X_{t} + \beta)dt + \sigma dB_{t}
\end{equation*}
$$
where $X_{0} = x_{0}$ and $\alpha > 0$, and verify that the solution can be written as
$$
\begin{equation*}
	X_{t} = e^{-\alpha t}\left(x_{0} + \frac{\beta}{\alpha} (e^{\alpha t}-1) + \sigma \int_{0}^{t} e^{\alpha s} dB_{s}\right)
\end{equation*}
$$
Use the representation to show that $X_{t}$ converges in distribution as $t \to \infty$, and find the limiting distribution. Finally, find the covariance $\text{Cov} (X_{s},X_{t})$.
