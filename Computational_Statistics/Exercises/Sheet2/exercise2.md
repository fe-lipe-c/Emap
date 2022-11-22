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

**1. Explain how you would simulate a Markov chain with transition kernel $T$.**

`Solution`

First we need to prove that $T$ is a Markov transition kernel: $T (x,y) = \mathbb{P}(y|x)$
$$
\begin{align*}
	T(x,y) &= \alpha (x,y)q (x,y) + \left(1 - \sum_{z \in \mathbb{X}} \alpha (x,z)q (x,z)\right)\delta _{x}(y)\\
	&= \sum_{z \in \mathbb{X}} \delta_{z}(y) \alpha (x,z)q (x,z) +  \left(1 - \sum_{z \in \mathbb{X}} \alpha (x,z)q (x,z)\right)  \delta_{x}(y)\\
	&\scriptsize= \mathbb{P}(X^{(t)} = y, \tiny\text{Proposal Accepted}\scriptsize|X^{(t-1)}=x)+ \mathbb{P}(X^{(t)}=y | X^{(t-1)}=x,\tiny\text{Proposal rejected}\scriptsize)\cdot \mathbb{P}(\tiny\text{Proposal rejected}\scriptsize|X^{(t-1)}= x)\\
	&\scriptsize= \mathbb{P}(X^{(t)} = y, \tiny\text{Proposal Accepted}\scriptsize|X^{(t-1)}=x) + \mathbb{P}(X^{(t)} = y, \tiny\text{Proposal Rejected}\scriptsize|X^{(t-1)}=x)\\
	&=\mathbb{P}(X^{(t)} = y | X^{(t-1)}=x)
\end{align*}
$$

To simulate a Markov chain from $T$, we define a initial distribution $\mu_{0}$ for the first sample $X^{0} \sim \mu_{0}$ and for the rest of the chain, given that we are at the iteration $t$, first we sample $X^{t+1} \sim q (\cdot|x^{(t)})$ and then we sample $U^{(t+1)} \sim \mathcal{U}[0,1]$. If $U^{(t+1)} \leq \alpha (x^{(t)},X^{(t+1)})$, we set $x^{(t+1)} = X^{(t+1)}$, otherwise we set $x^{(t+1)} = x^{(t)}$

