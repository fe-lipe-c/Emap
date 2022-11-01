# Stochastic Calculus
## Stochastic Processes - Ito Integral

### Exercises List 2

In what follows, $B (t) _{t \geq 0}$ is a Brownian motion.

1. Show that the Ito Integral does not have the monotonicity property, i.e. $X _{t} \leq Y _{t}$ a.s. for all $t \in [0,T]$ does not imply $\int_{0}^{T} X _{t}dB _{t} \leq  \int_{0}^{T} Y _{t} dB _{t}$ 

> Solution

Let $X _{t} \leq Y _{t}$ a.s. for all $t \in [0,T]$

----------
1. Show that if $X _{t}$ is any continuous martingale and $\phi$ is any convex function, then $Y _{t} = \phi (Y _{t})$ is always a local submartingale. Give an example that shows $Y _{t}$ need not be an honest submartingale.

> Solution

Let $X _{t}$ be any continuous martingale and $\phi$ be any convex function. Then $Y _{t} = \phi (X _{t})$ is a local submartingale. To prove that we need to show that $E [Y _{t}|\mathcal{F}_{t-1}] \geq Y _{t+1}$ a.s. for all $t \in [0,T]$.

Since $\phi$ is a convex function, the by Jensen inequality, we have
$$
\begin{align*}
	\mathbb{E} [\phi (X _{t})|\mathcal{F}_{t-1}] \geq \phi (\mathbb{E} [X _{t}| \mathcal{F}_{t-1}]) \\
\end{align*}
$$
