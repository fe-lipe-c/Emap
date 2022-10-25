
# Advanced Simulation
## Problem Sheet 2

### Exercise 2 (Metropolis-Hastings)

Let $\mathbb{X}$ be a finite state-space. Consider the following Markov transition kernel
$$
\begin{equation*}
	T(x,y) = \alpha (x,y)q (x,y) + \left(1 - \sum_{z \in \mathbb{X}} \alpha (x,z)q (x,z)\right)\delta _{x}(y)
\end{equation*}
$$
where $q (x,y) \geq 0$, $\sum_{y \in \mathbb{X}}q (x,y) = 1$ and $0 \leq \alpha (x,y) \leq 1$ for any $x,y \in \mathbb{X}$. $\delta _{x}(y)$ is the Kronecker symbol; i.e. $\delta _{x}(y) = 1$ if $y = x$ and zero otherwise.

1. Explain how you would simulate a Markov chain with transitiion kernel $T$.
