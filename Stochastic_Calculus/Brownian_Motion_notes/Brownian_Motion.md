# Brownian Motion - A Guide to Random Processes and Stochastic Calculus

## 1. Robert Brown's New Thing

**1.1 Definition.** Let $(\Omega, \mathcal{A},\mathbb{P})$ be a probability space. A d-dimensional stochastic process indexed by $I \subset [0,\infty)$ is a family of random variables $X_{t}:\Omega \longrightarrow \mathbb{R}^{d}, t \in I$. We write $X = (X_{t})_{t \in I}$. $I$ is called the index set and $\mathbb{R}^{d}$ the state space.

**1.2 Definition** A d-dimensional Brownian motion $B= (B_{t})_{t\geq 0}$ is a stochastic process indexed by $[0,\infty)$ taking values in $\mathbb{R}^{d}$ such that

1. $B_0(\omega) = 0$ for $\mathbb{P}$ almost all $\omega$;
2. $B _{t _{n}} - B _{t _{n-1}} , \dots , B _{t _{1}} - B _{t _{0}}$ are independent for all $n \geq 1, 0 = t _{0} \leq t _{1} < t _{2} \cdots < t _{n} < \infty$;
3. $B _{t} - B _{s} \sim B _{t+h} - B _{s +h}$ for all $0 \leq s < t, h \geq -s$;
4. $B _{t}- B _{s} \sim N(0,t-s)^{\otimes d}$, $N (0,t)(dx) = \frac{1}{\sqrt{2 \pi t}}\exp{\left(-\frac{x ^{2}}{2t}\right)dx}$;
5. $t \mapsto B _{t} (\omega)$ is continuous for all $\omega$.

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

Throughout the rest of this chapter $(B _{t})_{t \geq 0}$ is BM$^{1}$, $(\mathcal{F}_{t})_{t \geq 0}$ is an admissible filtration such that each $\mathcal{F}_{t}$ contains all $\mathbb{P}$-null sets, and $[0,T]$, $T < \infty$, a finite interval.
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

Let $(B _{t})_{t \geq 0}$ be a BM$^{1}$, $(M _{t})_{t \leq T } \in \mathcal{M}_{T}^{2,c}$, $(\mathcal{F}_{t})_{t \geq 0}$ be an admissible filtration and $f \in \mathcal{S}_{T}$. Then
1. $f \mapsto f \cdot M _{T} \in L ^{2}(\mathbb{P})$ is linear;
2. $\langle f \cdot B \rangle _{T} = f ^{2} \cdot \langle B \rangle _{T} = \int_{0}^{T}|f (s)| ^{2}ds$;
3. Ito's isometry - $L ^{2}$-continuity. For all $f \in \mathcal{S}_{T}$
$$
\begin{equation*}
	||f \cdot B _{T} ||_{L ^{2}(\mathbb{P})}^{2} = \mathbb{E} [(f \cdot B)_{T}^{2}] = \mathbb{E} \left[\int_{0}^{T}|f (s)|^{2}ds\right] = ||f||^{2}_{L ^{2}(\lambda _{T}\otimes \mathbb{P})}. \tag{15.16}
\end{equation*}
$$
> $\blacktriangleright$
---

----------
**15.11 Theorem** 
Let $(B _{t})_{t \geq 0}$ be $BM ^{1}$, $(M _{t})_{t \leq T} \in \mathcal{M}_{T}^{2,c}, (\mathcal{F}_{t})_{t \geq 0}$ be an admissible filtration and $f \in \mathcal{S}_{T}$. Then
1. $(f \cdot M _{t})_{t \leq T}$ is a continuous $L ^{2}$ martingale; in particular
$$
\begin{equation*}
	\mathbb{E} [(f \cdot B _{t} - f \cdot B _{s})^{2} | \mathcal{F}_{s}] = \mathbb{E} \left[\int_{s}^{t} |f (r)|^{2} dr \Big| \mathcal{F}_{s}\right], \qquad s < t \leq T.
\end{equation*}
$$
2. *Localization in time.* For every $\mathcal{F}_{t}$ stopping time $\tau$ with finitely many values
$$
\begin{equation*}
	(f \cdot M)_{t}^{\tau} = f \cdot (M ^{\tau})_{t} = (f \mathbb{I}_{[0,\tau]})\cdot M _{t}
\end{equation*}
$$
3. *Localization in space.* If $f,g \in \mathcal{S}_{T}$ are simple processes with $f (s,\omega) = g (s,\omega)$ for all $(s,\omega)\in [0,t] \times F$ for some $t \leq T$ and $F \in \mathcal{F}_{\infty}$, then
$$
\begin{equation*}
	(f \cdot M _{s})\mathbb{I}_{F} = (g \cdot M _{s})\mathbb{I}_{F}, \qquad 0 \leq s \leq t.
\end{equation*}
$$
> $\blacktriangleright$
---

### 15.3 Extension of the stochastic integral to $\mathcal{L}^{2}_{T}$

----------
**15.12 Lemma** 
Let $M \in \mathcal{M}_{T}^{2,c}$. Then $|| M ||_{\mathcal{M}_{T}^{2}} = (\mathbb{E}[\sup _{s \leq T} |M _{s}|^{2}])^{\frac{1}{2}}$ is a norm on $\mathcal{M}_{T}^{2,c}$ and $\mathcal{M}_{T}^{2,c}$ is closed under this norm. Moreover,
$$
\begin{equation*}
	\mathbb{E}\left[\sup _{s \leq T} |M _{s}|^{2}\right] \stackrel{tsc}{=} \mathbb{E}\left[ |M _{T}|^{2}\right] = \sup _{s \leq T} \mathbb{E} \left[ |M _{s}|^{2}\right],
\end{equation*}
$$
where $\stackrel{tsc}{=}$ means a two-sided comparison. (???)
> $\blacktriangleright$
---

Ito's isometry (15.16) allows us to extend the stochastic integral from the simple integrands $\mathcal{S}_{T} \subset L ^{2}(\lambda _{T}\otimes \mathbb{P})$ to the closure $\bar{\mathcal{S}}_{T}$ in $L ^{2}(\lambda _{T} \otimes \mathbb{P})$.

----------
**15.13 Definition** 
By $\mathcal{L}^{2}_{T}$ we denote the closure $\bar{\mathcal{S}}_{T}$ of the simple processes $\mathcal{S}_{T}$ with respect to the norm in $L ^{2}(\lambda _{T}\otimes \mathbb{P})$.
> $\blacktriangleright$
---

Using (15.16) we find for any sequence $(f _{n})_{n \geq 1} \subset \mathcal{S}_{T}$ with limit $f \in \mathcal{L}_{T}^{2}$ that
$$
\begin{equation*}
	||f _{n}\cdot B _{T} - f _{m} \cdot B _{T}||_{L ^{2}(\mathbb{P})}^{2} = \mathbb{E} \left[\int_{0}^{T}|f _{n}(s,\cdot) - f _{m}(s,\cdot)|^{2}ds\right] = ||f _{n} - f _{m}||^{2}_{L ^{2}(\lambda _{T}\otimes \mathbb{P})} \xrightarrow[m,n \to \infty]{} 0
	
\end{equation*}
$$
Therefore, for each $0 \leq t \leq T$, the limit
$$
\begin{equation*}
	L ^{2}(\mathbb{P})- \lim _{n \to \infty} f _{n}\cdot B _{t} \tag{15.19}
\end{equation*}
$$
exists and does not depend on the approximating sequence. Because of Lemma 15.12 the convergence (15.19) is locally uniform in $t$, defining an element in $\mathcal{M}_{T}^{2,c}$.

----------
**15.14 Definition** 
Let $(B _{t})_{t \geq 0}$ be a $BM ^{1}$ and let $f \in \mathcal{L}^{2}_{T}$. Then the stochastic integral (or Ito integral) is defined as 
$$
\begin{equation*}
	f \cdot B _{t} = \int_{0}^{t} f (s)dB _{s} = L ^{2}(\mathbb{P})-\lim _{n \to \infty} f _{n} \cdot B _{t}, \qquad 0 \leq t \leq T,
\end{equation*}
$$
where $(f _{n})_{n \geq 1} \subset \mathcal{S}_{T}$ is any sequence approximating $f \in \mathcal{L}_{T}^{2}$ in $L ^{2}(\lambda _{T} \otimes \mathbb{P})$.
> $\blacktriangleright$
---

----------
**15.15 Theorem** 
Let $(B _{t})_{t \geq 0}$ be a $BM ^{1}$, $(\mathcal{F}_{t})_{t \geq 0}$ be an admissible filtration and $f \in \mathcal{L}^{2}_{T}$. Then we have for all $t \leq T$
1. $f \mapsto f \cdot B$ is a linear map from $\mathcal{L}_{T}^{2}$ into $\mathcal{M}_{T}^{2,c}$, i.e. $(f \cdot B _{t})_{t \leq T}$ is continuous $L ^{2}$ martingale;
2. $(f \cdot B)^{2} - \langle f \cdot B \rangle$ is a martingale where $\langle f \cdot B \rangle _{t} = f ^{2}\cdot \langle B \rangle _{t} = \int_{0}^{t}|f (s)|^{2}ds$; in particular,
$$
\begin{equation*}
	\mathbb{E} [(f \cdot B _{t} - f \cdot B _{s})^{2}| \mathcal{F}_{s}] = \mathbb{E} \left[\int_{s}^{t}|f (r)|^{2}dr \Big| \mathcal{F}_{s}\right], \qquad s < t\leq T. \tag{15.21}
\end{equation*}
$$
3. Ito's Isometry - $L ^{2}$-continuity.
$$
\begin{equation*}
	||f \cdot B _{T}||^{2}_{L ^{2} (\mathbb{P})} = \mathbb{E}[(f \cdot B)_{T}^{2}] = \mathbb{E}\left[\int_{0}^{T}|f (s)|^{2}ds\right] = ||f||^{2}_{L ^{2}(\lambda _{T}\otimes \mathbb{P})} \tag{15.22}
\end{equation*}
$$
4. Maximal Inequalities.
$$
\begin{equation*}
	\mathbb{E}\left[\int_{0}^{T}|f (s)|^{2}ds\right] \leq \left[\sup _{t \leq T} \left(\int_{0}^{t}f \left(s\right)dB _{s}\right)^{2}\right] \leq 4 \mathbb{E}\left[\int_{0}^{T}|f (s)|^{2}ds \right]. \tag{15.23}
\end{equation*}
$$
5. *Localization in time.* Let $\tau$ be an $\mathcal{F}_{t}$ stopping time. Then
$$
\begin{equation*}
	(f \cdot B)_{t}^{\tau} = f \cdot (B ^{\tau})_{t} = (f \mathbb{I}_{[0,\tau)}) \cdot B _{t} \qquad \text{for all $t \leq T$.}
\end{equation*}
$$
6. *Localization in space.* If $f,g \in \mathcal{L}_{T}^{2}$ are integrands such that $f (s,\omega) = g (s,\omega)$ for all $(s,\omega)\in [0,t]\times F$ where $t \leq T$ and $F \in \mathcal{F}_{\infty}$, then 
$$
\begin{equation*}
	(f \cdot B _{s})\mathbb{I}_{F} = (g \cdot B _{s})\mathbb{I}_{F}, \qquad 0 \leq s \leq t.
\end{equation*}
$$
> $\blacktriangleright$
---

### 15.4 Evaluating Ito Integrals

Using integrands from $\mathcal{S}_{T}$ allows us to calculate only very few Ito integrals. For example, up to now we have the natural formula $\int_{0}^{T}\xi \cdot \mathbb{I}_{[a,b)}(s) dB _{s} = \xi \cdot (B _{b} - B _{a})$ just for bounded $\mathbb{F}_{a}$ measurable random variables $\xi$.

----------
**15.16 Lemma** 
Let $(B _{t})_{t \geq 0}$ be a $BM ^{1}$, $0 \leq a < b \leq T$ and $\xi \in L ^{2} (\mathbb{P})$ be $\mathcal{F}_{a}$ measurable. Then $\xi \cdot \mathbb{I}_{[a,b)} \in \mathcal{L}^{2}_{T}$ and
$$
\begin{equation*}
	\int_{0}^{T} \xi \cdot \mathbb{I}_{[a,b)} (s) dB _{s} = \xi \cdot (B _{b}- B _{a}).
\end{equation*}
$$
> $\blacktriangleright$
---

----------
**15.18 Proposition** 
Let $f \in \mathcal{L}_{T}^{2}$ be a process which is, as a function of $t$, mean-square continuous, i.e.
$$
\begin{equation*}
	\lim _{s \to t \in [0,T]}  \mathbb{E}[|f(s,\cdot) - f(t,\cdot)|^{2}] = 0, \qquad \text{for all $t \in [0,T]$.}
\end{equation*}
$$
Then
$$
\begin{equation*}
	\int_{0}^{T} f (t)d B _{t} = L ^{2}(\mathbb{P})- \lim _{| \Pi | \to 0} \sum_{j=1}^{n}f (s _{j-1})(B _{s _{j}} - B _{s _{j-1}})
\end{equation*}
$$
holds for any sequence of partitions $\Pi = \left\{s _{0} < s _{1} < \cdots < s _{n} = T \right\}$ with mesh $|\Pi| \to 0$.
> $\blacktriangleright$
---

### 15.5 What is the closure of $\mathcal{S}_{T}$

----------
**15.20 Definition** 
Let $(B _{t})_{t \geq 0}$ be a $BM ^{1}$ and $(\mathcal{F}_{t})_{t \geq 0}$ an admissible filtration. The progressive $\sigma$-algebra $\mathcal{P}$ is the family of all sets $\Gamma \subset [0,T]\times \Omega$ such that
$$
\begin{equation*}
	\Gamma \cap ([0,t] \times \Omega) \in \mathcal{B}[0,t]\otimes \mathcal{F}_{t}, \qquad \text{for all $t \leq T$.} \tag{15.25}
\end{equation*}
$$
> $\blacktriangleright$
---
By $L ^{2}_{\mathcal{P}}(\lambda _{T} \otimes \mathbb{P})$ we denote those equivalence classes in $L ^{2}([0,T]\times \Omega, \lambda _{T} \otimes \mathbb{P})$ which have a $\mathcal{P}$ measurable representative.

----------
**15.21 Lemma** 
Let $T >0$. Then $(L ^{2}_{\mathcal{P}}(\lambda \otimes \mathbb{P}),|| \cdot||_{L ^{2}(\lambda _{T}\otimes \mathbb{P})})$ is a Hilbert space.
> $\blacktriangleright$
---

Our aim is to show that $\mathcal{L}_{T}^{2} = L ^{2}_{\mathcal{P}(\lambda _{T} \otimes \mathbb{P})}$. For this we need a simple deterministic lemma. As before we write $L ^{2}(\lambda _{T}) = L ^{2}([0,T], \mathcal{B}[0,T],\lambda)$

----------
**15.22 Lemma** 
Let $\phi \in L ^{2}(\lambda _{T})$ and $T > 0$. Then
$$
\begin{equation*}
	\Theta _{n}[\phi](t) = \sum_{j=1}^{n-1}\xi _{j-1}\mathbb{I}_{[t _{j-1}, t _{j})}(t) \tag{15.26}
\end{equation*}
$$
where 
$$
\begin{equation*}
	t _{j} = \frac{jT}{n}, \qquad j=0,\dots, n, \qquad \xi _{0}= 0 \qquad \text{and} \qquad \xi _{j-1}= \frac{n}{T}\int_{t _{j-2}}^{t _{j-1}} \phi (s)ds, \qquad j \geq 2,
\end{equation*}
$$
is a sequence of step functions with $L ^{2}(\lambda _{T})-\lim _{n\to \infty} \Theta _{n}[\phi] = \phi$.
> $\blacktriangleright$
---

----------
**15.23 Theorem** 
Let $L ^{2}(\lambda _{T}\otimes \mathbb{P})$ closure of $\mathcal{S}_{T}$ is $L ^{2}_{\mathcal{P}}(\lambda _{T} \otimes \mathbb{P})$.
> $\blacktriangleright$
---

### 15.6 White noise integrals


