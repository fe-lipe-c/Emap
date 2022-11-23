# Chapter 10 - Stochastic Differential Equations
$\tiny \text{This doc is a direct reproduction of the course notes.}$

## Introduction

The goal of this chapter is to study the following equation:
$$
\begin{equation*}
	X_{t} = \eta + \int_{0}^{t} \mu_{s}(X_{s})ds + \int_{0}^{t}\sigma_{s}(X_{s})d B_{s} \qquad 0 \leq t \leq T, \qquad \text{a.s.} \tag{10.1}
\end{equation*}
$$
**Example:** Solve $d X_{t} = \mu_{t}X_{t}dt + \sigma_{t}X_{t}d B_{t}$
