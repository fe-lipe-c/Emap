# Stochastic Calculus

## 8. Itô Integration

### 8.1. Quadratic Variation of the Brownian Motion

### 8.2. The Itô Integral
We will now construct the Ito integral:
$$
\begin{equation*}
	\int_{0}^{T} \phi (\omega ,t) dB_{t}
\end{equation*}
$$
for a class of functions $\phi$. In what follows, we will fix a final time $T > 0$, a filtration $(\mathcal{F}_{t})_{t \geq 0}$ and a Brownian motion $(B_{t})_{t \geq 0}$ with respect to this filtration. 

#### 8.2.1. Simple Functions

We say $\phi: \Omega \times [0,T] \rightarrow \mathbb{R}$ is simple, and write $\phi \in \mathcal{H}_{0}^{2}[0,T]$, if
$$
\begin{equation*}
	\phi (\omega, t) = \sum_{i=0}^{n-1}a_{i}(\omega)\mathbb{I}_{(t_{i},t_{i+1}]}(t),
\end{equation*}
$$
where $0 = t_0 < t_1 < \cdots < t_{n} = T$ and $a_{i} \in \mathcal{F}_{t_{i}}$, with $\mathbb{E}[a_{i}^{2}] < + \infty$.

A choice for the integral of $f \in \mathcal{H}_{0}^{2}[0,T]$:
$$
\begin{equation*}
	\int_{0}^{T}\phi (\omega,t) dB_{t} = \sum_{i=0}^{n-1}a_{i}(\omega)(B_{t_{i+1}}(\omega) - B_{t_{i}}(\omega)).
\end{equation*}
$$
This define the integral operator $I: \mathcal{H}_{0}^{2}[0,T] \rightarrow L^2$.

We would like to extend this operator to a wider class of functions:
$$
\begin{equation*}
	\mathcal{H}^2[0,T] = \left\{\phi \in \mathcal{M} : \mathbb{E}\left[ \int_{0}^{T} \phi^2(\omega , t)dt \right] < + \infty \right\},
\end{equation*}
$$
where $\mathcal{M}$ is the space of function $\phi : \Omega \times [0,T] \rightarrow \mathbb{R}$ such that $\phi$ is measurable with respect to $\mathcal{F} \otimes \mathcal{B}([0,T])$ and adapted with respect to $(\mathcal{F}_{t})_{t \geq 0}$. Define also the norm in $\mathcal{H}^2$:
$$
\begin{equation*}
	||\phi||^2_{\mathcal{H}^2} = \mathbb{E}\left[ \int_{0}^{T} \phi^2(\omega , t)dt \right] = \int_{0}^{T} \mathbb{E}[\phi^2(\omega , t)]dt.
\end{equation*}
$$

---
**Lemma 8.2.1. (Ito Isometry $\mathcal{H}_0^{2}$)** 
$$
\begin{equation*}
	||\phi||_{\mathcal{H}^2} = ||I(\phi)||_{L^2}, \,\,\, \forall \phi \in \mathcal{H}_0^{2}.
\end{equation*}
$$
Then, the mapping $I: \mathcal{H}_0^{2}[0,T] \rightarrow L^2$ is continuous.

---

---
**Lemma 8.2.2.** 
$\mathcal{H}_0^2$ is dense in $\mathcal{H}^2$, i.e. for any $\phi \in \mathcal{H}^2$, there exists $(\phi_{n})_{n \in \mathbb{N}}$ in $\mathcal{H}_0^2$ such that $|| \phi - \phi_{n}||_{\mathcal{H}^2} \rightarrow 0$, as $n \rightarrow + \infty$.

---
#### 8.2.2. The Integral

---
**Definition 8.2.3. (Ito Integral)** 
For any $\phi \in \mathcal{H}^2$, we define $I(\phi)$ as the limit of $I(\phi_{n})$, where $(\phi_{n})_{n \in \mathbb{N}}$ belongs to $\mathcal{H}^2_0$ and $\phi_{n} \rightarrow \phi$ in $\mathcal{H}^2$. We call $I(\phi)$ the Ito integral of $\phi$ with respect to the Brownian motion $(B_{t})_{t \geq 0}$ and write
$$
\begin{equation*}
	I(\phi) = \int_{0}^{T} \phi (\omega ,t) dB_{t}.
\end{equation*}
$$

---

---
**Theorem 8.2.4** 
The Ito integral is well defined and in $\mathcal{H}^2$.

---

--- 
**Theorem 8.2.5 (Ito Isometry)** 
$$
\begin{equation*}
	||\phi||_{\mathcal{H}^2} = ||I(\phi)||_{L^2}, \,\,\, \forall \phi \in \mathcal{H}^2.
\end{equation*}
$$

$\vdots$

$\vdots$

$\vdots$

#### 8.2.4. Localization

The first important generalization is to consider $\phi: \Omega \times [0,T] \rightarrow \mathbb{R}$ measurable, adapted and satisfying the weaker integrability condition
$$
\begin{equation*}
	\mathbb{P} \left[ \int_{0}^{T} \phi^2(\omega , t)dt < + \infty \right] = 1.
\end{equation*}
$$
We write $\phi \in \mathcal{L}_{loc}^2[0,T]$. Clearly, $\mathcal{H}^2[0,T] \subset \mathcal{L}_{loc}^2[0,T]$

One of the main reasons to consider this space is to be able to integrate continuous functions of the Brownian motion.

**Definition 8.2.12.** 
$\mathbb{R} \mathbb{R}_{10} \times \mathbb{R}^{s}$

## 10. Stochastic Differential Equations

### 10.1 Introduction

