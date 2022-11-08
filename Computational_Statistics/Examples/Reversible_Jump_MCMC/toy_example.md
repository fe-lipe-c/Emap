# Toy Example - Reversible Jump 

Two models, uniform prior on models $p (\mathcal{M}_{1}) = p (\mathcal{M}_{2}) = \frac{1}{2}$. 

In model $\mathcal{M}_{1}, \theta \in \mathbb{R}$ and we can evaluate pointwise
$$
\begin{equation*}
	\pi_{1}(\theta) \propto g (\theta| \mathcal{M}_{1})\mathcal{L}(\theta | \mathcal{M}_{1}) = \exp \left(- \frac{1}{2}(\theta)^{2}\right)
\end{equation*}
$$
In model $\mathcal{M}_{2}, \theta \in \mathbb{R}^{2}$ and we can evaluate pointwise
$$
\begin{equation*}
	\pi_{2}(\theta) \propto g (\theta| \mathcal{M}_{2})\mathcal{L}(\theta | \mathcal{M}_{2}) = \exp \left(- \frac{1}{2}(\theta_{1})^{2}- \frac{1}{2}(\theta_{2})^{2}\right)
\end{equation*}
$$
In terms of model comparison, we should find
$$
\begin{equation*}
	\frac{h (\mathcal{M}_{2}|y)}{h (\mathcal{M}_{1}|y)}
\end{equation*}
$$
