><sub><sub><sub>The following text is adapted from the book 'Monte Carlo Statistical Methods'<sub><sub><sub>
# Rejection Sampling

This is a class of methods that only requires to know the functional form of the density $f$ of interest up to a multiplicative constant.

The key to this method is to use a simpler (simulationwise) density $g$ from which the simulation is actually done. For a given density $g$ - called the instrumental density - there are thus many densities $f$ - called the target densities - which can be simulated this way.

If $f$ is the density of interest, on an arbitrary space, we can write

$$
\begin{equation}
	f(x) = \int_{0}^{f(x)}du.\tag{2.7}
\end{equation}
$$

Thus, $f$ appears as the marginal density (in $X$) of the joint distribution,

$$
\begin{equation}
	(X,U) \sim \mathcal{U}\left\{(x,u ) : 0 < u < f(x) \right\}.\tag{2.8}
\end{equation}
$$

[Fundamental Theorem of Simulation](fundamental_theorem_simulation.md)
