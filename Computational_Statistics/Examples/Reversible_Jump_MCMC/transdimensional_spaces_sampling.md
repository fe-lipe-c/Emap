# Advanced Simulation Methods

## Chapter 7 - Reversible Jump MCMC

### 1. Bayesian Model Selection

Assume you have a countable set $\left\{\mathcal{M}_{1},\mathcal{M}_{2},\dots \right\}$ of Bayesian models to describe some data $y$. To each Bayesian model $\mathcal{M}_{k}$ is associated a random parameter $\theta _{k}$ of prior density $p (\theta _{k}| \mathcal{M}_{k})$ on the parameter space $\Theta _{k}$ and a likelihood function $\mathcal{L}(y;\theta _{k},\mathcal{M}_{k})$. Hence the posterior density on the parameters associated to model $\mathcal{M}_{k}$ is defined on $\Theta_{k}$ and has density
$$
\begin{equation*}
	\pi (\theta_{k}|y,\mathcal{M}_{k}) = \frac{\mathcal{L}(y;\theta_{k},\mathcal{M}_{k})p(\theta_{k}|\mathcal{M}_{k})}{\int_{\Theta_{k}}\mathcal{L}(y;\theta_{k},\mathcal{M}_{k})p(\theta_{k}|\mathcal{M}_{k})d\theta_{k}} = \frac{\mathcal{L}(y;\theta_{k},\mathcal{M}_{k})p(\theta_{k}|\mathcal{M}_{k})}{\mathcal{d}(y|\mathcal{M}_{k})}.
\end{equation*}
$$
where $\mathcal{d}(y|\mathcal{M}_{k})$ is the marginal likelihood or evidence of model $\mathcal{M}_{k}$.

Here we are interested in performing Bayesian inference about the model. To achieve this, we need to specify a prior distribution on $\{\mathcal{M}_{1},\mathcal{M}_{2},\dots\}$; i.e.
$$
\begin{equation*}
	g(\mathcal{M}_{k}) = \mathbb{P}(\mathcal{M}=\mathcal{M}_{k}).
\end{equation*}
$$
Now Bayesian inference on the model and parameter relies on the joint posterior
$$
\begin{equation*}
	\pi (\mathcal{M}_{k},\theta_{k}|y) = \frac{\mathcal{L}(y;\theta_{k},\mathcal{M}_{k})p(\theta_{k}|\mathcal{M}_{k})g(\mathcal{M}_{k})}{\sum_{k}\left(\int_{\Theta_{k}}\mathcal{L}(y;\theta_{k},\mathcal{M}_{k})p(\theta_{k}|\mathcal{M}_{k})d\theta_{k}\right)g(\mathcal{M}_{k})} = \frac{\mathcal{L}(y;\theta_{k},\mathcal{M}_{k})p(\theta_{k}|\mathcal{M}_{k})g(\mathcal{M}_{k})}{\mathcal{d}(y)}
\end{equation*}
$$
which is defined on the space
$$
\begin{equation*}
	\Theta = \Theta_{k} \times \bigcup_{k} \left\{k  \right\}.
\end{equation*}
$$

### 2. Model evidence estimation using standard Monte Carlo techniques

### 3. Reversible Jump Markov Chain Monte Carlo

The reversible jump algorithm will alternatively use 'within model' kernels and 'between-models' kernels. Starting from model index $k^{(0)}$ and parameter $\theta^{(0)} \in \Theta_{k^{(0)}}$, we propose a 'within model' move or we propose a move to another model. For within model moves we can use a standard Metropolis-Hastings algorithm. And how about 'between-models' moves? We are interested in designing a Markov kernel moving $(k, \theta_{k})$ to $k^{\prime,\theta_{k^{\prime}}}$.

#### 3.1. Reversible Markov kernel across dimensions

#### 3.2. Constructing $q$ and $a$ using dimension matching and deterministic mappings

The idea of dimension matching is to extend $\theta$ and $\theta ^{\prime}$ with auxiliary variables $u$ and $u^{\prime}$ such that the extended variables are of common dimension. Hence introduce $u$ drawn from (an arbitrary) $\varphi_{k \to k^{\prime}}$ and $u^{\prime}$ drawn from (an arbitrary) $\varphi_{k^{\prime} \to k}$ such that
$$
\begin{equation*}
	dim (\theta) + dim (u) = dim (\theta^{\prime}) + dim (u^{\prime}).
\end{equation*}
$$
To construct the proposal with density $q_{k \to k^{\prime}}(\theta \to \theta^{\prime})$, we first draw $u \sim \varphi_{k \to k^{\prime}}$. We then introduce a diffeomorphism $G_{k \to k^{\prime}}$ taking a couple $(\theta,u)$ and returning $(\theta^{\prime},u^{\prime})= G_{k \to k^{\prime}}(\theta,u)$. We will also write $\theta^{\prime}$ as $\theta^{\prime}(\theta,u)$ and $u^{\prime}$ as $u^{\prime}(\theta,u)$, to emphasize that it is a deterministic mapping. The we can write for any sets $A,B$:
$$
\begin{align*}
	&\sum_{k,k^{\prime}\in K_{A}\times K_{B}} \int_{(\theta,\theta^{\prime})\in A_{k}\times B_{k^{\prime}}}\pi(k,\theta)q (k \to k^{\prime})q_{k \to k^{\prime}}(\theta \to \theta^{\prime})a (\theta \to \theta^{\prime})d \theta d \theta^{\prime} =\\
	&\sum_{k,k^{\prime}\in K_{A}\times K_{B}} \int_{(\theta,\theta^{\prime}(\theta,u))\in A_{k}\times B_{k^{\prime}}}\pi(k,\theta)q (k \to k^{\prime})\varphi_{k \to k^{\prime}}(u)a (\theta \to \theta^{\prime}(\theta,u))d \theta du =\\
\end{align*}
$$
Consider the following acceptance probability:
$$
\begin{equation*}
	a (\theta \to \theta^{\prime}) = \min \left(\frac{\pi (k^{\prime},\theta^{\prime})\varphi_{k^{\prime}\to k}(u^{\prime})q (k^{\prime}\to k)}{\pi (k,\theta)\varphi_{k \to k^{\prime}}(u)q (k\to k^{\prime})}\left| \frac{\partial G_{k \to k^{\prime}}(\theta,u)}{\partial (\theta,u)}\right|,1\right)
\end{equation*}
$$
To summarize, we have found a proposal mechanism, consisting of sampling $k^{\prime}$, then $u$ from $\phi_{k \to k^{\prime}}$ and then deterministically mapping $(\theta,u)$ to $(\theta^{\prime},u^{\prime}) = G_{k \to k^{\prime}}$, and an acceptance probability $a (\theta,\theta^{\prime})$, such that the resulting Markov kernel $P$ satisfies
$$
\begin{equation*}
	\int_{((k,\theta_{k}),(k^{\prime},\theta_{k^{\prime}}^{\prime}))\in A \times B} = \int_{((k,\theta_{k}),(k^{\prime},\theta_{k^{\prime}}^{\prime}))\in A \times B}
\end{equation*}
$$



