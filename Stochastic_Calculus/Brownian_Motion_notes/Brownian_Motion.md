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
>**(Doob-Meyer Decomposition)** 

For all square integrable martingales $M \in \mathcal{M}_{T}^{2,c}$ there exists a unique adapted, continuous and increasing process $(\langle M \rangle _{t})_{t \leq T}$ such that $M ^{2} - \langle M \rangle$ is a martingale and $\langle M \rangle _{0} = 0$.

> $\blacktriangleright$
---

Let $(\mathcal{F} _{n})_{n \geq 0}$ be a filtration. An $L ^{2}$ martingale $X = (X _{n}, \mathcal{F}_{n})_{n \geq 0}$ is a martingale such that $X _{n} \in L ^{2}(\mathbb{P})$ for all $n \geq 0$. We write $\mathcal{M}^{2}$ for the family of $L ^{2}$ martingales. If $X \in \mathcal{M}^{2}$, then $X ^{2} = (X _{n}^{2}, \mathcal{F}_{n})_{n \geq 0}$ is a submartingale and, by the Doob Decomposition,
$$
\begin{equation}
	X _{n}^{2} = X _{0}^{2} + M _{n} + A _{n} \tag{15.2}
\end{equation}
$$
where $(M _{n},\mathcal{F}_{n})_{n \geq 0}$ is a martingale and $(A _{n})_{n \geq 0}$ is a previsable (i.e. $A _{n}$ is $\mathcal{F}_{n-1}$ measurable, $n \geq 1$) and increasing (i.e.: $A _{n} \leq A _{n+1}, n \geq 0$) process.

---
> **15.2 Lemma** 

Let $(X _{n}, \mathcal{F}_{n})_{n \geq 0}$ be an $L ^{2}$ martingale and let $\langle X \rangle = (\langle X \rangle _{n})_{n \geq 0}$ be its quadratic variation. Then, for all $n > m \geq 0$,
$$
\begin{equation}
	\mathbb{E} \left[ (X _{n} - X _{m})^{2} \right | \mathcal{F} _{m}] = \mathbb{E} \left[ X _{n}^{2} - X _{m}^{2} \right|\mathcal{F} _{m}]= \mathbb{E} \left[ \langle X \rangle _{n} - \langle X \rangle _{m} \right|\mathcal{F} _{m}]. \tag{15.3}
\end{equation}
$$
In particular,
$$
\begin{equation}
	\langle X \rangle _{n} = \sum_{j=1}^{n} \mathbb{E} \left[ (X _{j} - X _{j-1})^{2} \right | \mathcal{F} _{j-1}] = \sum_{j=1}^{n} \mathbb{E} \left[ X _{j}^{2} - X _{j-1}^{2} \right | \mathcal{F} _{j-1}] \tag{15.4}
\end{equation}
$$
> $\blacktriangleright$
---

---
> **15.3 Definition** 

Let $(X _{n}, \mathcal{F}_{n})_{n \geq 0}$ be a martingale and $(C _{n},\mathcal{F}_{n})_{n \geq 0}$ and adapted process. Then 
$$
\begin{equation*}
	C _{n} \cdot X _{n} = \sum_{j=1}^{n} C _{j-1} (X _{j}- X _{j-1}), \qquad C \cdot X _{0}=0, \qquad n \geq 1 \tag{15.5}
\end{equation*}
$$
is called the martingale transform.
> $\blacktriangleright$
---

---
**15.4 Theorem** \
Let $(M _{n}, \mathcal{F} _{n})_{n \geq 0}$ be an $L ^{2}$ martingale and $(C _{n},\mathcal{F}_{n})_{n \geq 0}$ be a bounded adapted process. Then
1. $C \cdot M$ is an $L ^{2}$ martingale, i.e. $C \cdot: \mathcal{M}^{2} \rightarrow \mathcal{M}^{2}$;
2. $C \mapsto C \cdot M$ is linear;
3. $\langle C \cdot M \rangle _{n} = C ^{2} \cdot \langle M \rangle _{n} = \sum_{j=1}^{n} C ^{2}_{j=1}(\langle M \rangle _{j} - \langle M \rangle _{j=1})$ for all $n \geq 1$;
4. $\mathbb{E}[(C \cdot M _{n} - C \cdot M _{m})^{2} | \mathcal{F} _{m}] = \mathbb{E} [C ^{2} \cdot \langle M \rangle _{n}- C ^{2} \cdot \langle M \rangle _{m} | \mathcal{F}_{m}]$, $n >m \geq 0$. In particular 
$$
\begin{align}
		&\mathbb{E} [(C \cdot M _{n})^{2}] = \mathbb{E} [C ^{2} \cdot \langle M \rangle _{n}], \tag{15.6}  \\
		&\mathbb{E} [(C \cdot M _{n})^{2}] = \mathbb{E} \left[ \sum_{j=1}^{n}C _{j=1}^{2}(M _{j} - M _{j-1})^{2} \right] = \mathbb{E} \left[ \sum_{j=1}^{n}C _{j=1}^{2}(M _{j}^{2} - M _{j-1}^{2}) \right] \tag{15.7}
\end{align}
$$
> $\blacktriangleright$
---

---
> **15.5 Lemma**

Let $(M _{n}, \mathcal{F} _{n})_{n \geq 0}, (N _{n}, \mathcal{F} _{n})_{n \geq 0}$ be an $L ^{2}$ martingales and let $(C _{n},\mathcal{F}_{n})_{n \geq 0}$ be a bounded adapted process. Then
$$
\begin{align}
	&\langle C \cdot M, N \rangle _{n} =  C \cdot \langle M, N \rangle _{n} = \sum_{j=1}^{n} C _{j-1}( \langle M, N \rangle _{j} - \langle M, N \rangle _{j-1} ) \tag{15.9} \\
 \end{align}
$$
> $\blacktriangleright$
---

---
> **15.6 Corollary** 

Let $(M _{n}, \mathcal{F} _{n})_{n \geq 0}, (N _{n}, \mathcal{F} _{n})_{n \geq 0}$ be an $L ^{2}$ martingales and let $(C _{n},\mathcal{F}_{n})_{n \geq 0}$ be a bounded adapted process. Then
$$
\begin{align*}
	&|\langle C \cdot M, N \rangle _{n}| \leq \sum_{j=1}^{n} |C _{j-1} | \left| \langle M, N \rangle _{j} - \langle M, N \rangle _{j-1} \right| \leq C \cdot \langle M, N \rangle _{n} \leq \sqrt{\langle C \cdot M \rangle _{n}} \sqrt{\langle N \rangle _{n}} \\
\end{align*}
$$

> $\blacktriangleright$
---

### 15.2. Simple Integrands

Throuhghout the rest of this chapter $(B _{t})_{t \geq 0}$ is BM ^{1}, $(\mathcal{F}_{t})_{t \geq 0}$ is an admissible filstration such that each $\mathcal{letter}_{t}$ contains all $\mathbb{P}$-null sets, and $[0,T]$, $T < \infty$, a finite interval.
1. $X ^{\tau}$ and $X _{s}^{\tau} = X _{\tau \wedge t}$ for the stopped process $(X _{t})_{t \geq 0}$;
2. $\mathcal{M}^{2}_{T}$ for the family of $\mathcal{F}^{t}$ martingales $(M _{t})_{0 \leq t \leq T} \subset L ^{2}(\mathbb{P})$;
3. $\mathcal{M}^{2,c}_{T}$ for the $L ^{2}$ martingales with (almost surely) continuous sample paths;
4. $L ^{2}(\lambda _{T} \otimes \mathbb{P}) = L ^{2}([0,T] \times \Omega, \lambda _{T} \otimes \mathbb{P})$ for the family of (equivalence classes of) all $\mathcal{B}[0,T] \otimes \mathcal{A}$ measurable random functions $f: [0,T] \times \Omega \rightarrow \mathbb{R}$ equipped with the norm $|| f ||_{L ^{2}(\lambda _{T}\otimes \mathbb{P})}^{2} = \int_{0}^{T} \mathbb{E} (|f (s)|^{2})ds < \infty$.

----------
**15.8 Definition** 

A real-valued stochastic process $(f(t,\cdot))_{t \in [0,T]}$ of the form 
$$
\begin{equation*}
	f (t, \omega) = \sum_{j=1}^{n} \phi _{j-1}(\omega)\mathbb{I}_{[s _{j-1},s _{j})}(t) \tag{15.12}
\end{equation*}
$$
where $n \geq 1, 0 = s _{0} \leq s _{1} \leq \dots \leq s _{n} \leq T$ and $\phi _{j} \in L ^{\infty}(\mathcal{F}_{s _{j}})$ measurable random variables, $j = 0, \dots, n-1$, is called a (right continuous) simple process. We write $\mathcal{S}_{t}$ for the family of all simple processes on $[0,T]$.

> $\blacktriangleright$
---

We can write (15.12) in the following form
$$
\begin{equation*}
	f (t, \omega) = \sum_{j=1}^{n} f(s _{j-1},\omega)\mathbb{I}_{[s _{j-1},s _{j})}(t) \tag{15.13}
\end{equation*}
$$

----------

----------
**15.9. Definition** 

Let $M \in \mathcal{M}_{T}^{2,c}$ be a continuous $L ^{2}$ martingale and $f \in \mathcal{S}_{T}$. Then
$$
\begin{equation*}
	f \cdot M _{T} = \sum_{j=1}^{n} f (s _{j-1})(M (s _{j}) - M (s _{j-1})) \tag{15.14}
\end{equation*}
$$
is called the stochastic integral of $f \in \mathcal{S}_{T}$. Instead of $f \cdot M _{T}$ we also write $\int_{0}^{T} f (s) dM _{s}$.

> $\blacktriangleright$
---

----------
**15.10 Theorem** 

Let


> $\blacktriangleright$
---













































