# Lab 10: curse of dimensionality and integration

See [lab10_curse_of_dimensionality.ipynb](lab10_curse_of_dimensionality.ipynb) starter notebook.



The "curse of dimensionality" is a term thrown around a lot these days, and it means different things to different people and in different contexts.  One context in which it is used is when the work required to reach a fixed accuracy grows exponentially in the dimension.

We'll explore this phenomenon in the context of integration, and compare two methods (quadrature vs Monte Carlo) which have very different pros and cons.

- Bonus: if you're interested in a method that mixes the pros and cons of each approach, look into **quasi Monte Carlo** methods. I have a [demo on quasi-Monte Carlo](https://github.com/stephenbeckr/randomized-algorithm-class/blob/master/Demos/demo14_MonteCarlo_and_improvements.ipynb) that I made for a different class

## Part 1: quadrature 

"Quadrature" refers to numerical integration where we sample points from the domain and use specific weights associated with those points to form our estimate of the integral (in contrast, Monte Carlo and Quasi-Monte Carlo are sometimes defined to be estimates in which the weights never change from point to point, though that definition is too vague to be illuminating at this point).

For example, the midpoint rule, [trapezoidal rule](https://en.wikipedia.org/wiki/Trapezoidal_rule), and [Simpson's rule](https://en.wikipedia.org/wiki/Simpson%27s_rule) (and their composite version) are quadrature methods, as are things like [Gauss-Legendre](https://en.wikipedia.org/wiki/Gaussian_quadrature) and [Clenshaw-Curtis](https://en.wikipedia.org/wiki/Clenshaw%E2%80%93Curtis_quadrature). 

We won't investigate these in detail, as we'll use `scipy.integrate.quad` to do the work for us (and it adaptively chooses the number of nodes in order to reach a target accuracy), but it helps to think of these as just Riemann sums.

Throughout this lab, we'll work with the function $f(x)=\sin(x)$, or in higher dimensions with $\vec{x}\in\mathbb{R}^d$, then
```math
f(\vec{x}) = \prod_{i=1}^d \sin(x_i)
```
and our goal is to estimate its integral
```math
\widetilde{I} = \int_{a}^{b} f(x)dx
```
or more generally if $d\ge 1$
```math
\widetilde{I} = \int_{a}^{b}\int_{a}^{b} \ldots \int_{a}^{b} f(\vec{x})dx_1 dx_2 \ldots dx_d.
```
We chose $f$ to be a simple function so that you can workout the answer by hand.

When $d>1$, let's actually look at 
```math
I = \widetilde{I}^{1/d}
```
since the value of this will not depend on the dimension.

## Part 2: Monte Carlo

We think of $\int_{a}^b f(x)dx$ as an expected value, like 
```math
E[\tilde{f}] := \int_{a}^b \tilde{f}(x) p(x) dx
```
for a probability distribution $p$ (i.e., $\int_a^b p(x)dx = 1$ and $p(x)\ge 0$), with $\tilde{f}(x) := f(x)/p(x)$.

The simplest choice is the uniform distribution for $p$, so 
```math
p(x) = \frac{1}{b-a}.
```

Then to estimate the value of the integral, we draw random samples $x$ from this uniform distribution $p$, and then evaluate $\tilde{f}(x)$. We do this many times, to get a **sample mean**, and use that to approximate the true mean.

That's it!

## Part 3: what to turn in for credit
To get credit for the lab,
- write a sentence or two about your observations, and...
- from part 1b, using about 100 function evalutions, what was your accuracy?
- from part 1c, in dimension 4, how many function evaluations did you use?
- from part 2, in dimension 1, with 1000 function evaluations, what was the accuracy?'

Turn this into Canvas
