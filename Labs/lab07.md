# Lab 7: more optimization

See [lab07_optimization.ipynb](lab07_optimization.ipynb) starter notebook.

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


To get credit for this lab, in Canvas, turn in 1 paragraph describing your attemps on high-dimensional Rosenbrock using several SciPy solvers. In particular, try at least one derivative-free solver, one solver that uses derivatives/gradients but not Hessians, and one solver that uses Hessians. Discuss what you saw (which solvers were efficient?)
