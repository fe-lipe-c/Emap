# Stochastic Processes 

## Brownian Motion

**Definition** A d-dimensional Brownian motion $B= (B_{t})_{t\geq 0}$ is a stochastic process indexed by $[0,\infty)$ taking values in $\mathbb{R}^{d}$ such that

1. $B_0(\omega) = 0$ for $\mathbb{P}$ almost all $\omega$;
2. $B _{t _{n}} - B _{t _{n-1}} , \dots , B _{t _{1}} - B _{t _{0}}$ are independent for all $n \geq 1, 0 = t _{0} \leq t _{1} < t _{2} \cdots < t _{n} < \infty$;
3. $B _{t} - B _{s} \sim B _{t+h} - B _{s +h}$ for all $0 \leq s < t, h \geq -s$;
4. $B _{t}- B _{s} \sim N(0,t-s)^{\otimes d}$, $N (0,t)(dx) = \frac{1}{\sqrt{2 \pi t}}\exp{\left(-\frac{x ^{2}}{2t}\right)dx}$;
5. $t \mapsto B _{t} (\omega)$ is continuous for all $\omega$.

In what follows, $(B_{t})_{t \geq 0}$ is a Brownian motion.

----------
**1. Show that $X_{t} = \frac{1}{c}B_{c^2t}$ is also a Brownian motion, for any constant $c$.** 
> Solution

The first item of the definition of a Brownian motion is satisfied directly. Now, for the item two we have that, for all $n \geq 1, 0 = t _{0} \leq t _{1} < t _{2} \cdots < t _{n} < \infty \implies 0 = c ^{2}t _{0} \leq c ^{2}t _{1} < c ^{2}t _{2} \cdots < c ^{2}t _{n} < \infty$. Then $B _{c ^{2}t _{n}} - B _{c ^{2}t _{n-1}} , \dots , B _{c ^{2}t _{1}} - B _{c ^{2}t _{0}}$ are independent, as well as $\frac{1}{c}B _{c ^{2}t _{n}} - \frac{1}{c}B _{c ^{2}t _{n-1}} , \dots , \frac{1}{c}B _{c ^{2}t _{1}} - \frac{1}{c}B _{c ^{2}t _{0}}$.

For the forth item, note that, for h >0
$$
\begin{equation*}
	(B _{c ^{2}(t + h)} - B _{c ^{2}t}) \sim N (0, c ^{2}h)
\end{equation*}
$$
Then $X _{t+h} - X _{t}$ is normally distributed. Furthermore, 
$$
\begin{align*}
	\mathbb{E}[X _{t +h} - X _{t}] = \mathbb{E} \left[\frac{1}{c}B _{(t+h)c ^{2}} - \frac{1}{c}B _{t c ^{2}}\right] = \frac{1}{c} \mathbb{E}[B _{(t+h)c ^{2}} - B _{t c ^{2}}] = 0
\end{align*}
$$
and
$$
\begin{align*}
	\mathbb{V}[X _{t +h} - X _{t}] = \mathbb{V} \left[\frac{1}{c}B _{(t+h)c ^{2}} - \frac{1}{c}B _{t c ^{2}}\right] = \frac{1}{c^2} \mathbb{V}[B _{(t+h)c ^{2}} - B _{t c ^{2}}] = \frac{1}{c^2}[ (t+h)c ^{2} - tc ^{2}] = h
\end{align*}
$$
Item 3 is a direct consequence of the fact that $X _{t+h} - X _{t} \sim N(0,h)$.

Finally, for the fifth item, $B _{t}$ is continuous for all $\omega$, so $\frac{1}{c}B _{tc ^{2}}$ is continuous for all $\omega$.

----------
**2. Let $(W _{t})_{t \geq 0}$ be another Brownian motion independent of $B$. Prove that for any $\rho \in [-1,1]$, the process $\rho B _{t} + \sqrt{1 - \rho ^{2}}W _{t}$ is also a Brownian motion.**
> Solution
