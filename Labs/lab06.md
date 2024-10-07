# Lab 6

## Part a: complexity analysis
- We'll discuss complexity analysis in class, e.g., how to do it properly by hand
- For the lab, we'll give you a black-box funciton, and your job is to determine what you think the complexity is

See [lab06a_complexity.ipynb](lab06a_complexity.ipynb) starter notebook


## Part b: optimization quiz
Take the [optimization method use case](https://canvas.colorado.edu/courses/110094/quizzes/425844) quiz on Canvas 
which asks you about which methods from [`scipy.optimize`](https://docs.scipy.org/doc/scipy/reference/optimize.html) to use in which cases

The quiz is: for each of the following type of optimization problem below, choose a reasonable solver from the lower list:

- $\min_{ x \in \mathbb{R}^{10000}} \, \|Ax-b\|_2^2 + 3 \|x\|_2^2, \quad A \in \mathbb{R}^{10000 \times 10000}$
- $\min_{x\in\mathbb{R}^n}  f(x), \quad f\in C^\infty(\mathbb{R}^n)\text{ and convex}, \quad  n = 10^2, \quad\text{want very high accuracy}$
- $\min_{x\in\mathbb{R}^n}  f(x), \quad f\in C^\infty(\mathbb{R}^n)\text{ and convex}, \quad  n \ge 10^6$
- $\min_{x\in\mathbb{R}^n}  f(x), \quad f\in C^\infty(\mathbb{R}^n)$ and *not* convex, $n = 10^2$
- $\min_{x\in\mathbb{R}^n} f(x)$, $f$ *not* convex, derivative *not available*, $n\approx 5$
- $\min_{x\in\mathbb{R}^n} \sum_{i=1}^{1000} f_i(x)^2$, each $f_i$ a smooth nonlinear function}

And the choice of solvers:

- Newton's method
- `scipy.optimize.least_squares`  "Solve a nonlinear least-squares problem with bounds on the variables"
- `scipy.optimize.minimize(..., method=’Nelder-Mead’)`
- `scipy.optimize.minimize(..., method=’trust-exact’)`
- `scipy.optimize.minimize(..., method=’BFGS’)`
- `scipy.sparse.linalg.lsqr`  "Find the least-squares solution to a large, sparse, linear system of equations."


## Part c: optimization (programming)

See [lab06b_optimization.ipynb](lab06b_optimization.ipynb) starter notebook.

#### Write your own Newton's method
Let
```math
f:\mathbb{R}^2 \to \mathbb{R},\quad
f(\vec{x}) = \left( x_1^2 - x_2^2 \right)\cdot e^{-(x_1^2 + x_2^2 )/0.2 }
```

Write your own very simple Newton's method to solve this, starting at the point $\vec{x} = (0,0.1)$.  What happens?

(Note: the starter notebook defines the function and its gradient and Hessian for you)

#### Explore what's in `scipy.optimize`
For the classic 2D [Rosenbrock function](https://en.wikipedia.org/wiki/Rosenbrock_function), solve it with the different solvers available in scipy. Which ones work best?

#### More Rosenbrock
Repeat the previous part for the multdimensional generalization of Rosenbrock, in dimension 1000
