# MCMC Using Hamiltonian Dynamics

### Hamilton's Equations

Hamiltonian dynamics operates on a d-dimensional position vector, $q$, and a d-dimensional momentum vector, $p$, so that the full state has 2d dimensions. The system is described by a function of $q$ and $p$ known as the Hamiltonian, $H (q,p)$.

#### Equations of Motion

The partial derivatives of the Hamiltonian determine how $q$ and $p$ change over time, $t$, according to Hamilton's equations:
$$
\begin{align*}
	& \frac{d q_{i}}{dt} = \frac{\partial H}{\partial p_{i}}, \tag{5.1}\\
	& \frac{d p_{i}}{dt} = -\frac{\partial H}{\partial q_{i}}, \tag{5.2}
\end{align*}
$$
for $i = 1, \ldots, d$. For any time interval of duration $s$, these equations define a mapping $T_{s}$, from the state at any time $t$ to the state at time $t + s$.

Alternatively, we can combine the vectors $q$ and $p$ into the vector $z = (q, p)$, with 2d dimensions. The equations of motion can then be written as
$$
\begin{equation*}
	\frac{d z}{dt} = J \nabla H(z),
\end{equation*}
$$
where $\nabla H$ is the gradient of $H$ and 
$$
\begin{equation*}
	J = \begin{bmatrix}
		0_{d\times d} & I_{d\times d} \\
		-I_{d\times d}& 0_{d\times d} \tag{5.3}
	\end{bmatrix},
\end{equation*}
$$

#### Potential and Kinetic Energy

For HMC we usually use Hamiltonian functions that can be written as
$$
\begin{equation*}
	H (q,p) = U (q) + K (p). \tag{5.4}
\end{equation*}
$$
Here $U (q)$ is called the potential energy, and will be defined to be minus the log probability density of the distribution for $q$ that we wish to sample, plus any constant that is convenient.

$K (p)$ is called the kinetic energy, and is usually defined as
$$
\begin{equation*}
	K (p) = \frac{1}{2} \left[p^T M^{-1} p \right]. \tag{5.5}
\end{equation*}
$$
Here $M$ is a symmetric, positive-definite "mass matrix", which is typically diagonal, and is often a scalar multiple of the identity matrix. This form for $K (p)$ corresponds to minus the log probability density (plus a constant) of the zero-mean Gaussian distribution with covariance matrix $M$.

With these forms of $H$ and $K$, Hamilton's equations 5.1 and 5.2 become, for i = 1, ..., d:
$$
\begin{align*}
	& \frac{d q_{i}}{dt} = [M^{-1}p]_{i}, \tag{5.6}\\
	& \frac{d p_{i}}{dt} = -\frac{\partial K}{\partial p_{i}}, \tag{5.7}
\end{align*}
$$

#### Properties of Hamiltonian Dynamics

##### 1. Reversibility 

The reversibility of Hamiltonian dynamics is important for showing that MCMC updates that use the dynamics leave the desired distribution invariant, since this is most easily proved by showing reversibility of the Markov chain transitions, which requires reversibility of the dynamics used to propose a state.
