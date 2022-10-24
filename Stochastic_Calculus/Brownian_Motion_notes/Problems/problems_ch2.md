# Problems

----------
**`Problem 2.8`**

**Let $(B _{t})_{t \geq 0}$ be a $BM ^{1}$. Decide which of the following processes are Brownian motions:**
$$
\begin{equation*}
	\text{a)} X _{t} = 2 B _{t/4}; \qquad \text{b)} Y _{t} = B _{2t} - B _{t}; \qquad \text{c)} Z _{t} = \sqrt{t} B _{1} \qquad (t \geq 0).
\end{equation*}
$$
> Solution

**Definition** A d-dimensional Brownian motion $B= (B_{t})_{t\geq 0}$ is a stochastic process indexed by $[0,\infty)$ taking values in $\mathbb{R}^{d}$ such that

1. $B_0(\omega) = 0$ for $\mathbb{P}$ almost all $\omega$;
2. $B _{t _{n}} - B _{t _{n-1}} , \dots , B _{t _{1}} - B _{t _{0}}$ are independent for all $n \geq 1, 0 = t _{0} \leq t _{1} < t _{2} \cdots < t _{n} < \infty$;
3. $B _{t} - B _{s} \sim B _{t+h} - B _{s +h}$ for all $0 \leq s < t, h \geq -s$;
4. $B _{t}- B _{s} \sim N(0,t-s)^{\otimes d}$, $N (0,t)(dx) = \frac{1}{\sqrt{2 \pi t}}\exp{\left(-\frac{x ^{2}}{2t}\right)dx}$;
5. $t \mapsto B _{t} (\omega)$ is continuous for all $\omega$.

**a)** $X _{t} = 2 B _{t/4};$
 
