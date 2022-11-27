# Hamiltonian Monte Carlo

### Phase Space and Hamilton's Equations

Having expanded the target parameter space to phase space, we can now lift the target distribution onto a joint probability distribution on phase space called the canonical distribution. We do this with the choice of a conditional probability distribution over the auxiliary momentum:
$$
\begin{equation*}
	\pi (q,p) = \pi (p|q)\pi (q)
\end{equation*}
$$

The canonical density $\pi (q,p)$ dos not depend on particular choice of parametrization, and we can write it in terms of an invariant Hamiltonian function, $H (q,p)$:
$$
\begin{equation*}
	\pi (q,p) = e^{-H (q,p)}.
\end{equation*}
$$
The value of the Hamiltonian at any point in phase space is called the energy at that point. Because of the decomposition of the joint density, the Hamiltonian,
$$
\begin{equation*}
	H (q,p) = -\log \pi (q,p)
\end{equation*}
$$
itself decomposes into two terms, 
$$
\begin{equation*}
	H (q,p) = -\log \pi (p|q) - \log \pi (q) = K (p,q) + V (q)
\end{equation*}
$$
The desired vector field can be generated from a given Hamiltonian with Hamilton's equations:
$$
\begin{align*}
	&\frac{dq}{dt} = \frac{\partial H}{\partial p} = \frac{\partial K}{\partial p} \\
	&\frac{dp}{dt} = -\frac{\partial H}{\partial q} = - \frac{\partial K}{\partial q}-\frac{\partial V}{\partial q}
\end{align*}
$$

### The Idealized Hamiltonian Markov Transition

To lift an initial point in parameter space into one on phase space we simply sample from the conditional distribution over the momentum:
$$
\begin{equation*}
	p \sim (p|q).
\end{equation*}
$$
Once on phase space we can explore the joint typical set by integrating Hamilton's equations for some time, $(q,p) \to \phi_{t}(q,p)$. After integrating Hamilton's equations we can return to the target parameter space by simply projecting away the momentum, $(q,p) \to q$.

Composing these three steps together yields a Hamiltonian Markov transition composed of random trajectories that rapidly explore the target distribution.

### Efficient Hamiltonian Monte Carlo

An immediate complication with this foundational construction is that it does not define a unique Markov transition but rather a infinity of them.

### The Natural Geometry of Phase Space

One of the characteristic properties of Hamilton's equations is that they converse the value of the Hamiltonian. In other words, every Hamiltonian trajectory is confined to an energy level set,
$$
\begin{equation*}
	H^{-1}(E) = \{(q,p) : H(q,p) = E\}
\end{equation*}
$$
Instead of specifying a point in phase space with its position and momentum, we can specify it with an energy $E$ and its position on the corresponding level set $\theta_{E} \in H^{-1}(E)$

The canonical distribution on phase space admits a microcanonical decomposition
$$
\begin{equation*}
	\pi (q,p) = \pi (\theta_{E}|E)\pi (E).
\end{equation*}
$$
across this foliation. The conditional distribution over each level set, $\pi (\theta_{E}|E)$, is called the microcanonical distribution, while the distribution across the level sets, $\pi (E)$, is called the marginal energy distribution.

### Optimizing the Choice of Kinetic Energy

