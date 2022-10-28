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
Item 3 is a direct consequence of the fact that $X _{t+h} - X _{t} \sim N(0,h)$, for every $t,h >0$.

Finally, for the fifth item, $B _{t}$ is continuous for all $\omega$, so $\frac{1}{c}B _{tc ^{2}}$ is continuous for all $\omega$.

----------
**2. Let $(W _{t})_{t \geq 0}$ be another Brownian motion independent of $B$. Prove that for any $\rho \in [-1,1]$, the process $\rho B _{t} + \sqrt{1 - \rho ^{2}}W _{t}$ is also a Brownian motion.**
> Solution


----------
**3. Let $X _{t} = B _{t} - t B _{1}$, for $0 \leq t \leq 1$. This process is called *Brownian Bridge*. Compute the mean and covariance functions of $X$. What is the distribution of $X _{t}$?** 																									
> Solution

Let's compute the mean and covariance of $X$:

`mean`
$$
\begin{align*}
	&\mathbb{E}[X _{t}] = \mathbb{E}[B _{t}- t B _{1}] = \mathbb{E}[B _{t}] - t\mathbb{E}[B _{1}] = 0
\end{align*}
$$
`variance`
$$
\begin{align*}
	\mathbb{V}[X _{t}] &= \mathbb{E}[(B _{t} - t B _{1})^{2}] = \mathbb{E}[B _{t}^{2} + t ^{2}B _{1}^{2} - 2 tB _{t}B _{1}] \\
	&= t + t ^{2} - 2t \mathbb{E}[B _{t}B _{1}] = t + t ^{2} - 2t \mathbb{E}[(B _{1} - B _{t} + B _{t})B _{t}]\\
	&= t + t ^{2} - 2t \mathbb{E}[(B _{1}- B _{t})B _{t} + B _{t}^{2}] = t + t ^{2} - 2t \mathbb{E}[(B _{1}- B _{t})B _{t}] - 2t ^{2}\\
	&= t - t ^{2} = t (1-t)
	
\end{align*}
$$
`covariance`

For any $0 \leq s < t \leq 1$
$$
\begin{align*}
	\scriptsize Cov (X _{s}, X _{t})
	&\scriptsize= \mathbb{E}[X _{s}X _{t}]
	= \mathbb{E}[(B _{s}- s B _{1})(B _{t}- t B _{1})]\\
	& \scriptsize=  \mathbb{E}[B _{s}B _{t} -t B _{s}B _{1} - sB _{t} B _{1} + stB _{1}^{2}]\\
	& \scriptsize= s -t s - s t + st = s (1 -t)
\end{align*}
$$

The distribution of $X _{t} = B _{t} - t B _{1}$
$$
\begin{align*}
	\mathbb{P}_{X _{t}}(x) = \mathbb{P}(X _{t}\leq x) = \mathbb{P}(B _{t} - t B _{1} \leq x)
\end{align*}
$$







