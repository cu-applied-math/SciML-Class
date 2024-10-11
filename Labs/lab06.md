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

