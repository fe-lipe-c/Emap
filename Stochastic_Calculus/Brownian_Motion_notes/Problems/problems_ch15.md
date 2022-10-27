# Problems Chapter 15

----------
**`Problem 15.1`**

**Let $(M _{n}, \mathcal{F}_{n})_{n \geq 0}$ and $(N _{n}, \mathcal{F}_{n})_{n \geq 0}$ be $L ^{2}$ martingales; then $(M _{n}N _{n}- \langle M,N \rangle _{n},\mathcal{F}_{n})_{n \geq 0}$ is a martingale.** 
> Solution

$$
\begin{align*}
	&\mathbb{E}[M _{n}N _{n} - \langle M _{n},N _{n} \rangle | \mathcal{F}_{n-1}] = \mathbb{E}[M _{n}N _{n}| \mathcal{F}_{n-1}] - \mathbb{E}[\langle M _{n},N _{n} \rangle | \mathcal{F}_{n-1}] \\
	&= M _{n-1}N _{n-1}- \mathbb{E}[\langle M _{n},N _{n} \rangle | \mathcal{F}_{n-1}] \\
\end{align*}
$$
By the quadratic form $M \mapsto \langle M \rangle$, we can use polarization to get the quadratic covariation, which is a bilinear form
$$
\begin{equation*}
	\langle M _{n},N _{n} \rangle = \frac{1}{4}\left[\langle M _{n} +N _{n} \rangle - \langle M _{n} -N _{n} \rangle\right], \qquad \text{for all } M _{n},N _{n} \in \mathcal{M}^{2}
\end{equation*}
$$
Then,
$$
\begin{align*}
	\mathbb{E}[M _{n}N _{n} - \langle M _{n},N _{n} \rangle | \mathcal{F}_{n-1}] &=
	M _{n-1}N _{n-1}- \frac{1}{4} \mathbb{E}[\langle M _{n} + N _{n} \rangle - \langle M _{n} - N _{n} \rangle | \mathcal{F}_{n-1}] \\
	&=M _{n-1}N _{n-1}- \frac{1}{4} \mathbb{E}[\langle M _{n} + N _{n} \rangle| \mathcal{F}_{n-1}] +\frac{1}{4}\mathbb{E}[\langle M _{n} - N _{n} \rangle | \mathcal{F}_{n-1}] \\
\end{align*}
$$
Since, for all $M _{n},N _{n} \in \mathcal{M}^{2}$, $(M _{n} + N _{n}), (M _{n} - N _{n}) \in \mathcal{M}^{2}$, then, by the Doob-Meyer decomposition, we have that $(M _{n} + N _{n})^{2} - \langle M _{n} + N _{n} \rangle$ and $(M _{n} - N _{n})^{2} - \langle M _{n} - N _{n} \rangle$ are also maringales. Therefore
$$
\begin{align*}
\small
	&\tiny\mathbb{E}[M _{n}N _{n} - \langle M _{n},N _{n} \rangle | \mathcal{F}_{n-1}] =\\
	&\tiny M _{n-1}N _{n-1}+ \frac{1}{4} \mathbb{E}[((M _{n} + N _{n})^{2}-\langle M _{n} + N _{n} \rangle) - (M _{n}+ N _{n})^{2} | \mathcal{F}_{n-1}] - \tiny\frac{1}{4} \mathbb{E}[((M _{n} - N _{n})^{2}-\langle M _{n} - N _{n} \rangle) - (M _{n}- N _{n})^{2}| \mathcal{F}_{n-1}] =\\
	&\tiny M _{n-1}N _{n-1}+\frac{1}{4}((M _{n-1} + N _{n-1})^{2}-\langle M _{n-1} + N _{n-1} \rangle)- \frac{1}{4} ((M _{n-1} - N _{n-1})^{2}-\langle M _{n-1} - N _{n-1} \rangle) + \frac{1}{4} \mathbb{E}[(M _{n}- N _{n})^{2} - (M _{n}+N _{n})^{2}| \mathcal{F}_{n-1}] =\\
	&\tiny 2M _{n-1}N _{n-1}+\frac{1}{4}(\langle M _{n-1} - N _{n-1} \rangle-\langle M _{n-1} + N _{n-1} \rangle)+ \frac{1}{4} \mathbb{E}[(M _{n}- N _{n})^{2} - (M _{n}+ N _{n})^{2}| \mathcal{F}_{n-1}] =\\
	&\tiny M _{n-1}N _{n-1}+\frac{1}{4}(\langle M _{n-1} - N _{n-1} \rangle-\langle M _{n-1} + N _{n-1} \rangle)=\\
	&\tiny M _{n-1}N _{n-1}-\langle M _{n-1}, N _{n-1} \rangle
\end{align*}
$$

