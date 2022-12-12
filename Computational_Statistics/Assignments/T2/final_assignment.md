Paper 1: MCMC using Hamiltonian dynamics (Neal et al., 2011)

As discussed in class, as the dimensionality of the space over which integrals need to be taken growns, performance suffers massively - this is the so-called "curse of dimensionality". In our quest to compute expectations efficiently, we might want to draw on all of the available information in order to find pockets of high probability mass.

Clever proposal mechanisms in MCMC use local information, usually in the form of gradients of the (log) target. In this seminal 2011 review, Radford Neal lays out a complete treatment of a technique known as Hybrid or Hamiltonian Monte Carlo (HMC), which works by constructing a Markov chain on an augmented state-space where one considers potentials and momenta.

1. Describe how to apply Hamiltonian dynamics to MCMC;

`solution`

The HMC works by using a phase space, that can be seen as an expansion of the target parameter space. This expansion is made through the addition of a new variable with the same dimensionality as the target parameter. This new variable is called momentum. The phase space is defined as the set of all possible states of the system, that is, the set of all possible values of the target parameters and the momenta. 

In this phase space we set a dynamical system. Let $q$ be a d-dimensional position vector (this is the target parameter), and $p$ be a d-dimensional momentum vector. Then we define $H (q,p)$, a function of $q$ and $p$ that determines a Hamiltonian dynamics. This function is called the Hamiltonian function and its partial derivatives determine how $q_{i}$ and $p_{i}$ change over time $t$:
$$
\begin{align*}
\frac{dq}{dt} &= \frac{\partial H}{\partial p} \\
\frac{dp}{dt} &= -\frac{\partial H}{\partial q}
\end{align*}
$$
for $i = 1, \dots, d$.

In Hamiltonian Monte Carlo the Hamiltonian is written as:
$$
\begin{equation*}
	H(q,p) = U(q) + K(p),
\end{equation*}
$$
where $U (q)$ is called the potential energy an $K (q)$ is called the kinetic energy. Here the potential energy is defined to be minus the log probability density of the target distribution.

