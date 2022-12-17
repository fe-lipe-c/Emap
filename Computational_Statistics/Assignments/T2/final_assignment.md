Paper 1: MCMC using Hamiltonian dynamics (Neal et al., 2011)

As discussed in class, as the dimensionality of the space over which integrals need to be taken growns, performance suffers massively - this is the so-called "curse of dimensionality". In our quest to compute expectations efficiently, we might want to draw on all of the available information in order to find pockets of high probability mass.

Clever proposal mechanisms in MCMC use local information, usually in the form of gradients of the (log) target. In this seminal 2011 review, Radford Neal lays out a complete treatment of a technique known as Hybrid or Hamiltonian Monte Carlo (HMC), which works by constructing a Markov chain on an augmented state-space where one considers potentials and momenta.

**1. Describe how to apply Hamiltonian dynamics to MCMC;**

`solution`

The HMC work by using a phase space, that can be seen as an expansion of the target parameter space. This expansion is made through the addition of a new variable with the same dimensionality as the target parameter. This new variable is called momentum. The phase space is defined as the set of all possible states of the system, that is, the set of all possible values of the target parameters and the momenta. 

In this phase space we set a dynamical system. Let $q$ be a d-dimensional position vector (this is the target parameter), and $p$ be a d-dimensional momentum vector. Then we define $H (q,p)$, a function of $q$ and $p$ that determines a Hamiltonian dynamics. This function is called the Hamiltonian function and its partial derivatives determine how $q_{i}$ and $p_{i}$ change over time $t$:
$$
\begin{align*}
\frac{dq_{i}}{dt} &= \frac{\partial H}{\partial p_{i}} \\
\frac{dp_{i}}{dt} &= -\frac{\partial H}{\partial q_{i}}
\end{align*}
$$
for $i = 1, \dots, d$.

In Hamiltonian Monte Carlo the Hamiltonian is written as:
$$
\begin{equation*}
	H(q,p) = U(q) + K(p),
\end{equation*}
$$
where $U (q)$ is called the potential energy an $K (q)$ is called the kinetic energy. The potential energy is defined to be minus the log probability density of the target distribution and $K (p)$ usually is defined as $K (p) = p^{T} M^{-1}p/2$, where $M$ is a symmetric, positive-definite (usually diagonal).

#### Leapfrog method

To implement this method we use the Leapfrog method, that discretaize the Hamiltonian dynamics. This method can be seen as an extension of the Euller's method. While the Euller's method have the following steps,
$$
\begin{align*}
	&p_{i}(t+\epsilon) = p_{i} (t) + \epsilon \frac{dp_{i}}{dt}(t) = p_{i}(t) - \epsilon \frac{\partial U}{\partial q_{i}}(q (t)) \\
	&q_{i}(t+\epsilon) = q_{i} (t) + \epsilon \frac{dq_{i}}{dt}(t) = q_{i}(t) + \epsilon \frac{p_{i}(t)}{m_{i}},
\end{align*}
$$
the leapfrog method have the following steps:
$$
\begin{align*}
	&p_{i}(t+\epsilon/2) = p_{i}(t) - \epsilon/2 \frac{\partial U}{\partial q_{i}}(q (t)) \\
	&q_{i}(t+\epsilon) = q_{i}(t) + \epsilon \frac{p_{i}(t+\epsilon/2)}{m_{i}} \\
	&p_{i}(t+\epsilon)  = p_{i}(t+\epsilon/2) - \epsilon/2 \frac{\partial U}{\partial q_{i}}(q (t+\epsilon)),
\end{align*}
$$
With this method we calculate an approximate trajectory of the position and momentum variables.

#### The two steps of the HMC Algorithm
There is two steps to sample from the target distribution using HMC. Let $q_{0}$ be the initial value for the target parameter. Then the first step is to sample a momentum from the Gaussian distribution. With it we start the dynamics of the system, approximated by the leapfrog method, and sample a path in the phase space. At the end of the path, the last pair of momentum and position is set as the proposal, where the value of this momentum is negated. 

The proposed state $(q^{*},p ^{*})$ is accepted with probability:
$$
\begin{align*}
	&\min \left(1, \exp \left(-H(q^{*},p^{*}) + H(q,p) \right) \right) =\\
	&\min \left(1, \exp \left(-U(q^{*}) + U(q) - K (p^{*})+K (p) \right) \right) ,
\end{align*}
$$
If the proposed state is not accepted, the next state is the same as the current state.


**Trajectories for a Two-Dimensional Problem** 

As an example I used a simple simulation shown in the paper, where the target distribution is bivariate Gaussian with means of zero, standard deviations of one, and correlation 0.95. For the momentum is used a bivariate Gaussian with means zero, standard deviations of one, and zero correlation. 

The figure below shows the trajectory, after the momentum sampling, of the position variable is the phase space, going from one point in the distribution to another. 
integral

**2. Implementation: reproduce Figure 6 of Neal et al. (2011)** 

The author implements a Hamiltonian Monte Carlo and a random-walk Metropolis in a 100-dimensional multivariate Gaussian distribution in which the variables are independent, with means of zero, and standard deviations of $0.01, 0.02, \dots, 0.99, 1.00$.

For the random-walk Metropolis is used the following proposal
$$
\begin{equation*}
	q^{*} = q^{t-1} + W
\end{equation*}
$$
where $W \sim N(0, \Sigma)$, $\Sigma$ is diagonal matrix with diagonal drawn uniformly from $(0.0176, 0.0264)$. Since the kernel of the proposal is symmetrical, we get the following acceptance ratio:
$$
\begin{equation*}
	\frac{\pi (q^{*})}{\pi (q^{t-1})}
\end{equation*}
$$
where $\pi (q)$ is the target distribution:
$$
\begin{equation*}
	\pi (q) = \frac{1}{(2 \pi)^{\frac{k}{2}} (\text{det}\Sigma)^{\frac{1}{2}}} \exp \left( -\frac{1}{2} q^T \Sigma^{-1} q \right)
\end{equation*}
$$

