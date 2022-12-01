# HMC Examples

#### One-Dimensional Example

The Hamiltonian is defined as follows:
$$
\begin{align*}
&H (q,p) = U (q) + K (p), \tag{5.8}\\ 
& U (q) = \frac{q^{2}}{2},\\
& K (p) = \frac{p^{2}}{2}.
\end{align*}
$$
This corresponds to a Gaussian distribution for $q$ with mean zero and variance one. Indeed, the potential energy is defined to be minus the log probability density of the distribution for $q$ that we wish to sample, plus any constant that is convenient. The probability density for $N (0,1)$ is
$$
\begin{equation*}
	\frac{1}{\sqrt{2\pi}}\exp\left(-\frac{q^{2}}{2}\right),
\end{equation*}
$$
and the log probability density is
$$
\begin{equation*}
	-\frac{1}{2}\log(2\pi) - \frac{q^{2}}{2}.
\end{equation*}
$$
Also, for $K$ we have that $M = 1$. The resulting dynamics for (5.8) is
$$
\begin{equation*}
	\frac{dq}{dt} = p \quad \text{and} \quad \frac{dp}{dt} = -q.
\end{equation*}
$$
Solutions have the following form, for some constants $r$ and $a$:
$$
\begin{align*}
	& q(t) = r\cos(a + t),\\
	& p(t) = -r\sin(a + t).
\end{align*}
$$
Hence, the mapping $T_{s}$ is a rotation by $s$ radians clockwise around the origin in the $(q,p)$ plane.
