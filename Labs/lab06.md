# Lab 6

## Part a: complexity analysis
- We'll discuss complexity analysis in class, e.g., how to do it properly by hand
- For the lab, we'll give you a black-box funciton, and your job is to determine what you think the complexity is

See [lab06a_complexity.ipynb](lab06a_complexity.ipynb) starter notebook


## Part b: optimization quiz
Take the [optimization method use case](https://canvas.colorado.edu/courses/110094/quizzes/425844) quiz on Canvas 
which asks you about which methods from [`scipy.optimize`](https://docs.scipy.org/doc/scipy/reference/optimize.html) to use in which cases

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

#### Explore what's in `scipy.optimzie`
For the classic 2D [Rosenbrock function](https://en.wikipedia.org/wiki/Rosenbrock_function), solve it with the different solvers available in scipy. Which ones work best?

#### More Rosenbrock
Repeat the previous part for the multdimensional generalization of Rosenbrock, in dimension 1000
