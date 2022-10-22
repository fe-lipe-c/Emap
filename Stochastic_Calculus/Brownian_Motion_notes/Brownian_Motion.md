# Brownian Motion - A Guide to Random Processes and Stochastic Calculus

## 1. Robert Brown's New Thing

**1.1 Definition.** Let $(\Omega, \mathcal{A},\mathbb{P})$ be a probability space. A d-dimensional stochastic process indexed by $I \subset [0,\infty)$ is a family of random variables $X_{t}:\Omega \longrightarrow \mathbb{R}^{d}, t \in I$. We write $X = (X_{t})_{t \in I}$. $I$ is called the index set and $\mathbb{R}^{d}$ the state space.

**1.2 Definition** A d-dimensional Brownian motion $B= (B_{t})_{t\geq 0}$ is a stochastic process indexed by $[0,\infty)$ taking values in $\mathbb{R}^{d}$ such that

1. $B_0(\omega) = 0$ for $\mathbb{P}$ almost all $\omega$;
2. timeHMS
3. t

## 15. Stochastic integrals: $L ^{2}$-Theory

### 15.1 Discrete stochastic integrals

---
>**(Doob Decomposition - Measure Book)** 

Let $(X, \mathcal{F}, \mathcal{F _{n}}, \mu)$ be a $\sigma$-finite filtered measure space and let $(U _{n},\mathcal{F} _{n}) _{n \in \mathbb{N}}$ be a submartingale. Define $U _{0} = 0$ and $\mathcal{F _{0}} = \left\{\empty, X \right\}$. Then there exists an a.e. unique martingale $(M _{n}, \mathcal{F} _{n}) _{n \in \mathbb{N}}$ and an increasing sequence of functions $(A _{n}) _{n \in \mathbb{N}}$ such that $A _{n} \in L ^{1}(\mathcal{F}_{n-1})$ for all $n \geq 2$ and
$$
\begin{equation*}
	U _{n} = M _{n} + A _{n}, \qquad n \in \mathbb{N}
\end{equation*}
$$
> --
---

Let $(\mathcal{F} _{n})_{n \geq 0}$ be a filtration. An $L ^{2}$ martingale $X = (X _{n}, \mathcal{F}_{n})_{n \geq 0}$ is a martingale such that $X _{n} \in L ^{2}(\mathbb{P})$ for all $n \geq 0$. We write $\mathcal{M}^{2}$ for the family of $L ^{2}$ martingales. If $X \in \mathcal{M}^{2}$, then $X ^{2} = (X _{n}^{2}, \mathcal{F}_{n})_{n \geq 0}$ is a submartingale and, by the Doob Decomposition,
$$
\begin{equation*}
	X _{n}^{2} = X _{0}^{2} + M _{n} + A _{n}
\end{equation*}
$$
where $(M _{n},\mathcal{F}_{n})_{n \geq 0}$ is a martingale and $(A _{n})_{n \geq 0}$ is a previsable (i.e. $A _{n}$ is $\mathcal{F}_{n-1}$ measurable, $n \geq 1$) and increasing (i.e.: $A _{n} \leq A _{n+1}, n \geq 0$) process.

