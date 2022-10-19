# Extra assignment 0: Who's that (simulated) pokemon?

## Background
In this (hopefully) fun little exercise I will describe a [rejection sampling](rejection_sampling.md) algorithm to sample from a mysterious distribution. Suppose we have the following procedure:

1. Generate $U_{1},U_{2} \sim Uniform(0,1)$, independently;
2. Compute $Y_1 = -\log(U1)$ and $Y_2 = -\log(U2)$. If $Y_2 > \frac{(1-Y_1)^2}{2}$, accept $Y = (Y_1, Y_2)$. Else, reject and return to step 1;
5. Generate $U_3 \sim \operatorname{Uniform}(0, 1)$; if $U_3 < 1/2$, set $X = Y_1$, otherwise set $X = -Y_1$.
    
