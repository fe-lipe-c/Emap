# Background

Suppose we are interested in an integrable function $\varphi(\cdot)$ and its expectation under a probability distribution with law $\pi$, $I = \int_{\mathbb{X}} \varphi(x)\pi(x)dx$. Monte Carlo is a large class of sampling algorithms to approximate integrals. It depends on constructing an estimator
$$
\begin{equation}
	\hat{I} = \frac{1}{n}\sum_{i=1}^n \varphi(X_i),
\end{equation}
$$
where $X_i \sim \pi$. The estimator in (1) can be improved in a number of ways. In particular, the procedure known as *Rao-Blackwellisation* allows one to obtain estimators that have lower variance with the same bias, i.e., are more efficient. 

# Questions
*Hint: I suggest you employ $\varphi(x) = x^2$* 

**1.**  Show that, if $\pi(x) = \int_{\mathbb{X}} g(x|y) h(y)dy$, then both
$$
\begin{equation}
\begin{split}
	\hat{I}_{n}^{MC} = \frac{1}{n}\sum_{i=1}^n \varphi(X_i), X_{i} \sim \pi,
	\text{ and }\\
	\hat{I}_{n}^{RB} = \frac{1}{n}\sum_{i=1}^n \mathbb{E}[\varphi(X)| Y_{i}], Y_{i} \sim h,
\end{split}
\end{equation}
$$
converge to $\mathbb{E}_{\pi}[\varphi(X)]$.

> Solution

We have that $\hat{I}_{n}^{MC} = \frac{1}{n}\sum_{i=1}^n \varphi(X_i), X_{i} \sim \pi$ converges almost surely to $\mathbb{E}_{\pi}[\varphi(X)]$ by the Strong Law of Large Numbers.

Also we have the fact that
$$
\begin{equation*}
\begin{split}
	\mathbb{E}_{\pi}[\varphi(X)] &= \int_{\mathbb{X}} \varphi(x)\pi(x)dx = \int_{\mathbb{X}} \varphi(x)\left(\int_{\mathbb{X}} g(x|y) h(y)dy\right)dx\\
&\stackrel{*}{=}\int_{\mathbb{X}}\left(\int_{\mathbb{X}} \varphi(x)g(x|y)dx\right)h(y)dy\\
&= \int_{\mathbb{X}} \mathbb{E}[\varphi(X)|Y]h(y)dy = \mathbb{E}_{h}\left[ \mathbb{E}[\varphi(X)|Y]\right],
\end{split}
\end{equation*}
$$
where in * we use Fubini's Theorem. Again by the SLLN we have that $\hat{I}_{n}^{RB} = \frac{1}{n}\sum_{i=1}^n \mathbb{E}[\varphi(X)| Y_{i}], Y_{i} \sim h$ converges almost surely to $\mathbb{E}_{h}\left[ \mathbb{E}[\varphi(X)|Y]\right]$. Then, both estimators in (2) vonverge to $\mathbb{E}_{\pi}[\varphi(X)]$.

**2.**  For each of the following cases, generate random variables $X_{i}$ and $Y_{i}$ and compute the average and variance of the "vanilla" Monte Carlo and Rao-Blackwellised estimators:

**(a)** $X|Y \sim$ Poisson$(Y)$, $Y \sim$ Gamma$(a,b) \implies X \sim$ Negative-Binomial;
> Solution

Let $\pi(x) = \int_{\mathbb{X}}g(x|y)h(y)dy$, where $g(x|y) = \frac{e^{-y}y^x}{x!}$ and $h(y) = \frac{b^a}{\Gamma(a)}y^{a-1}e^{-by}$, then we have that
$$
\begin{equation}
	\begin{split}
		\pi(x) &= \int_{\mathbb{X}}g(x|y)h(y)dy = \int_{\mathbb{X}}\frac{e^{-y}y^x}{x!}\frac{b^a}{\Gamma(a)}y^{a-1}e^{-by}dy\\
	&= \frac{b^a}{x!\Gamma(a)}\int_{\mathbb{X}}e^{-y}y^xy^{a-1}e^{-by}dy = \frac{b^a}{x!\Gamma(a)}\int_{\mathbb{X}}e^{-y(b+1)}y^{x+a-1}dy\\
	&\stackrel{(*)}{=} \frac{b^a}{x!\Gamma(a)}\frac{\Gamma(x+a)}{(b+1)^{x+a}}\int_{\mathbb{X}}\frac{(b+1)^{x+a}}{\Gamma(x+a)}e^{-y(b+1)}y^{x+a-1}dy\\
	&= \frac{b^a}{x!\Gamma(a)}\frac{\Gamma(x+a)}{(b+1)^{x+a}} = \frac{\Gamma(x+a)}{x!\Gamma(a)}b^a(b+1)^{-x-a}\\
	&\stackrel{(**)}{=} \frac{(x+a-1)!}{x!(a-1)!}b^a(b+1)^{-x-a} = \binom{x+a-1}{x} b^a(b+1)^{-x-a}\\
	&= \binom{x+a-1}{x} b^a \left(\frac{1}{b+1}\right)^{x}\left(\frac{1}{b+1}\right)^{a}\\
	&= \binom{x+a-1}{x} \left(\frac{1}{b+1}\right)^{x}\left(\frac{b}{b+1}\right)^{a}\
	\end{split}
\end{equation}
$$
where in (*) we use constant equal to one to obtain a distribution Gamma(x+a,b+1) and integrate it to the unit and in (**) the fact that $\Gamma(x)= (x-1)!$. Then $\pi$ is Negative-Binomial$\left(a,\frac{1}{b+1}\right)$.




Then, we have that $\mathbb{E}_{\pi}[\varphi(X)] = \int_{\mathbb{X}} \varphi(x)\pi(x)dx$

We want to calculate
$$
\begin{equation}
	\hat{\mu}_{n}^{MC} = \frac{1}{n}\sum_{i=1}^n X_i, X_{i} \sim \text{Negative-Binomial},
\end{equation}
$$



**(b)** $X|Y \sim$ Normal$(0,Y)$, $Y \sim$ Gamma$(a,b) \implies X \sim$ Generalised-t;
> Solution

teste

$F _{X}(x) = 1 - e ^{-\lambda x}$

Inverse
$$
\begin{equation*}
\begin{split}
	u = 1 - e ^{-\lambda x} \implies u -1 = - e ^{- \lambda x}\\
	\ln{(1-u)} = - \lambda x \implies x = - \frac{1}{\lambda} \ln{(1-u)}
\end{split}
\end{equation*}
$$


















end code
