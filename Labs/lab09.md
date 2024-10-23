# Lab 9: data-driven parameter estimation / system-identification via WENDy

See [lab09_WENDy.ipynb](lab09_WENDy.ipynb) starter notebook.

We'll consider the [logistic equation](https://en.wikipedia.org/wiki/Logistic_function#In_ecology:_modeling_population_growth) for describing popluation growth, as we did last week.

$y(t)$ represents the population at time $t$, and satisifies the equation
$$dy/dt = \theta y \left( 1 - \frac{y}{k} \right)$$
where $\theta$ is the **growth rate** (often referred to as "r" but we'll use $\theta$ to match other conventions), and $k$ is a carrying capacity of the population.

This is a very simple first-order ODE, covered in any good undergrad ODE class, and has a closed-form solution,
```math
y(t) = \frac{k}{ 1 + \frac{k-y_0}{y_0}e^{-\theta t}}
```
if $y(0) = y_0$ is the initial condition.

**Motivation for our lab**
We're observing a population of organisms and we know they evolve according to the logistic equation, and we know that they have a given carrying capacity of $k=10$.  We observe 21 data points
and our scientific question is, **what was the growth rate $\theta$**?


**What to turn in for credit?**
- Turn in your estimate of theta from the SINDy method (this is about half-way through the lab)

