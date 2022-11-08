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
	\int_{((k,\theta_{k}),(k^{\prime},\theta_{k^{\prime}}^{\prime}))\in A \times B}\pi (dk,d \theta_{k})P ((k,\theta_{k}),d (k^{\prime},\theta^{\prime}_{k^{\prime}})) = \int_{((k,\theta_{k}),(k^{\prime},\theta_{k^{\prime}}^{\prime}))\in A \times B}\pi (dk^{\prime},d \theta_{k^{\prime}}^{\prime})P ((k^{\prime},\theta_{k^{\prime}}^{\prime}),d(k,\theta_{k}))
\end{equation*}
$$

#### 3.3. Another representation for the random walk Metropolis-Hastings

### 4. Algorithmic description

For each model $\mathcal{M}_{k}$ we introduce a 'within-model' standard Metropolis-Hastings kernel $S_{k}$ leaving $\pi (\theta_{k}|y,\mathcal{M}_{k})$ invariant. We thus have a collection of 'within-model' moves, $S_{k}$ for each $\mathcal{M}_{k}$ for each $\mathcal{M}_{k}$, and a 'between-model' Markov kernel $P$. We introduce the probability $\beta$ of performing a 'within-model' move, which we might take close to 1 so that most moves are performed within models, with the occasional 'between-models' attempt with probability $1 - \beta$.

**Algorithm. (Reversible Jump Markov Chain Monte Carlo)**
Starting with $(k^{(0)},\theta^{(0)})$ iterate for $t = 1,2,3,\dots$
1. With probability $\beta$, set $k^{(t)} = k^{(t-1)}$ and perform one step of $S_{k^{(t)}}$ leaving $\pi (\theta_{k^{(t)}}|y, \mathcal{M}_{k^{(t)}})$ invariant.
2. With probability $1-\beta$, propose another model $k^{\prime}\sim q (k^{\prime}|k^{(t-1)})$. Then draw a random variable $u_{k^{(t-1)}\to k^{\prime}}\sim \varphi_{k^{(t-1)}\to k^{\prime}}$ and apply the deterministic mapping $G_{k^{(t-1)}\to k^{\prime}}$ to obtain a proposal $\theta^{\prime}\in \Theta_{k^{\prime}}$ and $u_{k^{\prime}\to k^{(t-1)}}$. With probability
$$
\begin{equation*}
	a(\theta^{(t-1)}\to \theta^{\prime}) = \min \left(\frac{\pi (\theta^{\prime})\varphi_{k^{\prime}\to k^{(t-1)}}(u_{k^{\prime}\to k^{(t-1)}})q (k^{(t-1)}|k^{\prime})}{\pi (\theta^{(t-1)})\varphi_{k^{(t-1)}\to k^{\prime}}(u_{k^{(t-1)}\to k^{\prime}})q (k^{\prime}|k^{(t-1)})}\left|\frac{\partial G_{k^{(t-1)}\to k^{\prime}}(\theta^{(t-1)},u_{k^{(t-1)}\to k^{\prime}})}{\partial (\theta,u)} \right|,1\right)
\end{equation*}
$$
accept, i.e. set $\theta^{(t)} = \theta^{\prime}$, $k^{(t)} = k^{\prime}$. Otherwise reject, i.e. set $\theta^{(t)} = \theta^{(t-1)}$, $k^{(t)}= k^{(t-1)}$.

**Proposition 1** 
The Markov kernel associated to the reversible jump algorithm admits $\pi (\mathcal{M}_{k}, \theta_{k}|y)$ as invariant density.

### 5. Toy Example

Consider a problem with two possible models $\mathcal{M}_{1}$ and $\mathcal{M}_{2}$. Model $\mathcal{M}_{1}$ has a single parameter $\theta \in \Theta_{1}$. Model $\mathcal{M}_{2}$ has two parameters $(\theta_{1}, \theta_{2})\in \Theta_{2}$. The joint posterior is defined on
$$
\begin{equation*}
	\Theta = \left\{1 \right\} \times \Theta_{1} \cup \left\{2 \right\} \times \Theta_{2}.
\end{equation*}
$$
We need to propose moves $G_{1 \to 2}$ and $G_{2 \to 1}$ such that $G_{2 \to 1} = G^{-1}_{1 \to 2}$. Assume we move from $\mathcal{M}_{1}$ to $\mathcal{M}_{2}$ using
$$
\begin{equation*}
	(\theta_{1},\theta_{2}) = G_{1 \to 2}(\theta,u) = (\theta - u,\theta + u)
\end{equation*}
$$
where $u$ is some auxiliary variable from distribution $\varphi$, so that the associated reverse move from $\mathcal{M}_{2}$ to $\mathcal{M}_{1}$ is simply
$$
\begin{equation*}
	G_{2 \to 1}(\theta_{1},\theta_{2}) = \left(\frac{\theta_{1}+ \theta_{2}}{2},\frac{\theta_{1}- \theta_{2}}{2}\right)
\end{equation*}
$$
We have $G_{2 \to 1} \circ G_{1 \to 2}(\theta,u) = G_{2 \to 1}(\theta -u, \theta +u) = (\theta, u)$. We have $\left|\frac{\partial G_{1 \to 2}(\theta,u)}{\partial (\theta,u)} \right| = 2$ and $\left|\frac{\partial G_{2 \to 1}(\theta,u)}{\partial (\theta,u)} \right| = \frac{1}{2}$. If we propose a move from $\mathcal{M}_{1}$ to $\mathcal{M}_{2}$ with probability $q_{12}$ and a move from $\mathcal{M}_{2}$ to $\mathcal{M}_{1}$ with probability $q_{21}$, then the acceptance rate of a move from $\mathcal{M}_{1}$ to $\mathcal{M}_{2}$ is given by
$$
\begin{equation*}
	\min \left(1,\frac{\pi (2,\theta_{1}, \theta_{2})}{\pi (1, \theta)}\frac{1}{\varphi (u)} \frac{q_{21}}{q_{12}} \times 2\right)
\end{equation*}
$$

