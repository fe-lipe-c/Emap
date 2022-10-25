# Advanced Simulation Methods

## Chapter 6 - The Metropolis-Hastings Algorithm

Assume that we are interested in sampling from a distribution on $\mathbb{X}$ with probability density  function $\pi$. In most applications, we will have $\mathbb{X} = \mathbb{R}^{d}$. We introduce a proposal distribution on the space $\mathbb{X}$, with density written $q (x|x ^{\prime})$; i.e. for any $x ^{\prime} \in \mathbb{X}$ we have $q (x | x ^{\prime}) \geq 0$ and $\int_{\mathbb{X}} q (x |x ^{\prime})dx = 1$.

The Metropolis-Hastings algorithm proceeds as follows to generate a Markov chain $(X ^{(t)})_{t \geq 1}$.

**Algorithm. Metropolis-Hastings** 
Starting from an arbitrary $X ^{(1)}$, iterate for $t = 2,3,\dots$
1. Sample $X \sim q (\cdot | X ^{(t - 1)})$.
2. Compute
$$
\begin{equation*}
	\alpha \left(X | X ^{(t-1)}\right) = \min{\left(1,\frac{\pi (X)q (X ^{(t-1)}|X)}{\pi (X ^{(t-1)}) q (X|X ^{t-1})}\right)}
\end{equation*}
$$
3. With probability $\alpha (X|X ^{t-1})$, set $X ^{(t)} = X$, otherwise set $X ^{(t)} = X ^{(t-1)}$.

Note that the Metropolis-Hastings only requires point-wise evaluations $\pi (x)$ up to a normalizing constant.

This algorithm generates a Markov chain $(X ^{(t)})_{t \geq 1}$. The following expression establishes the expression of the associated Markov chain kernel.

----------
**Proposition 1.1.** 
The transition kernel of the Metropolis-Hastings algorithm is given by
$$
\begin{equation*}
	K (x ^{(t-1)}, x ^{(t)}) = \alpha (x ^{(t)} | x ^{(t-1)})q (x ^{(t)} | x ^{(t-1)}) + (1 - \alpha (x ^{(t-1)})) \delta _{x ^{(t-1)}} (x ^{(t)})
\end{equation*}
$$
where $\delta _{x ^{(t-1)}}$ denotes the Dirac mass at $x ^{(t-1)}$














































