# Lab 8: adjoint state method

See [lab08.ipynb](lab08.ipynb) starter notebook.

# Lab 8

We'll consider the [logistic equation](https://en.wikipedia.org/wiki/Logistic_function#In_ecology:_modeling_population_growth) for describing popluation growth. 
$y(t)$ represents the population at time $t$, and satisifies the equation
$$dy/dt = \theta y \left( 1 - \frac{y}{k} \right)$$
where $\theta$ is the **growth rate** (often referred to as "r" but we'll use $\theta$ to match other conventions), and $k$ is a carrying capacity of the population.

This is a very simple first-order ODE, covered in any good undergrad ODE class, and has a closed-form solution,
$$y(t) = \frac{k}{ 1 + \frac{k-y_0}{y_0}e^{-\theta t}}$$
if $y(0) = y_0$ is the initial condition.

**Motivation for our lab**
We're observing a population of organisms and we know they evolve according to the logistic equation, and we know that they have a given carrying capacity of $k=10$.  We observe two data points:

| time | population |
| -- | -- |
| $t_0=0$ | $y_0=1$ |
| $t_1=2$ | $y_1 = 7$ |

and our scientific question is, **what was the growth rate $\theta$**?

Our lab is divided into several parts:
- Part 1: familiarity with scipy's ODE solver
  - This should be quick
- Part 2 and 3a: work things out by hand
  - This should be pen-and-paper, and should also be fairly quick
- Part 3b: adjoint state method
  - This may take longer. This is the heart of the lab
- Part 4: root-finding
  - This is "extra". Only do this if you finish part 3b


To get credit for this lab, in Canvas, turn in a plot from parts 1a and 1b.


### Helpful links
- [`scipy.integrate.solve_ivp`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.solve_ivp.html)
- Info on the adjoint-state method in the appendix of [Neural Ordinary Differential Equations](https://arxiv.org/abs/1806.07366) by Chen, Rubanova, Bettencourt and Duvenaud (NeurIPS 2018)