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

**2. Let $\pi$ be a probability mass function on $\mathbb{X}$. Show that if** 
$$
\begin{equation*}
	\alpha(x,y) = \frac{\gamma (x,y)}{\pi (x)q (x,y)}
\end{equation*}
$$
**where $\gamma (x,y) = \gamma (y,x)$ and $\gamma (x,y)$ is chosen such that $0 \leq \alpha (x,y) \leq 1$ for any $x,y \in \mathbb{X}$, then $T$ is $\pi$-reversible.**   

`Solution`

The transition kernel $T$ is $\pi$-reversible if, for any $x,y \in \mathbb{X}$,
$$
\begin{equation*}
	\pi (x)T(x,y) = \pi (y)T(y,x)
\end{equation*}
$$
Then, let $x,y \in \mathbb{X}$, we have
$$
\begin{align*}
	\pi (x)T(x,y) &= \pi (x)\left(\alpha (x,y)q (x,y) + \left(1 - \sum_{z \in \mathbb{X}} \alpha (x,z)q (x,z)\right)\delta _{x}(y)\right)\\
	&= \pi (x)\alpha (x,y)q (x,y) + \pi (x)\left(1 - \sum_{z \in \mathbb{X}} \alpha (x,z)q (x,z)\right)\delta _{x}(y)\\
	&= \pi (x)\frac{\gamma (x,y)}{\pi (x)q (x,y)}q (x,y) + \pi (x)\left(1 - \sum_{z \in \mathbb{X}} \frac{\gamma (x,z)}{\pi (x)q (x,z)}q (x,z)\right)\delta _{x}(y)\\
	&= \gamma (x,y) + \pi (x)\delta _{x}(y) - \sum_{z \in \mathbb{X}} \gamma (x,z)\delta _{x}(y)\\
\end{align*}
$$
If $x=y$, then the result is true trivially. If $x \neq y$, then $\delta _{x}(y) = 0$ and, therefore, considering that $\gamma (x,y) = \gamma (y,x)$, $T$ is $\pi$-reversible.

**3. Show that the Metropolis-Hastings algorithm corresponds to a particular choice of $\gamma (x,y)$.** 

`Solution`

In the Metropolis-Hastings algorithm, the acceptance probability is given by
$$
\begin{equation*}
	\alpha (x,y) = \min \left\{1,\frac{\pi (y)q (y,x)}{\pi (x)q (x,y)}\right\}
\end{equation*}
$$
Setting $\gamma (x,y) = \min \left\{\pi (x)q (x,y),\pi (y) q (y,x)\right\}$ we get the acceptance probability of the Metropolis-Hastings algorithm.

**4. Let $\pi$ be a probability mass function on the finite space $\mathbb{X}$ such that $\pi (x) > 0$ for any $x \in \mathbb{X}$. To sample from $\pi$, we run a Metropolis-Hastings chain $(X^{(t)})_{t \geq 1}$ with proposal $q (x,y)\geq 0$, such that $\sum_{y \in \mathbb{X}}q (x,y) = 1$ and $q (x,x)=0$, for any $x \in \mathbb{X}$. Consider here the sequence $(Y^{(k)})_{k \geq 1}$ of accepted proposals: $Y^{(1)} = X^{(\tau_{1})}$, where $\tau_{1} = 1$ and, for $k \geq 2$, $Y^{(k)} = X^{(\tau_{k})}$, where $\tau_{k} = \min \left\{t : t > \tau_{k-1}, X^{(t)} \neq Y^{(k-1)} \right\}$.** 

**Let $\phi: \mathbb{X} \to \mathbb{R}$ be a test function. Show that the estimate $\frac{1}{\tau_{k}-1}\sum_{t=1}^{\tau_{k}-1}\phi (X^{(t)})$ can be rewritten as a function of $(Y^{(k)})_{k \geq 1}$ and $(\tau_{k})_{k \geq 1}$ and prove that the sequence $(Y^{(k)})_{k \geq 1}$ is a Markov chain with transition kernel** 
$$
\begin{equation*}
	K (x,y) = \frac{\alpha (x,y)q (x,y)}{\sum_{z \in \mathbb{X}} \alpha (x,z)q (x,z)}.
\end{equation*}
$$

`Solution`


