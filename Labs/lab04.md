# Lab 4, SciML class

Playing around with automatic differentiation

### Warmup: What happens if you do AD on a function that isn't differentiable?
We'll explore via experimentation.  We first define the $r$ to be the usual ReLU,
$$r(x) = \begin{cases} 0 & x \le 0 \\ x & x > 0\end{cases}
$$
(though note that if we change the $x\le 0$ vs $x>0$ to be $x < 0$ vs $x \ge 0$, that would potentially change things!)

Then define two variant **implementations**,
$$ r_2(x) = r(-x) + x, \quad r_3(x) = \frac12\Big( r(x) + r_2(x) \Big).$$
These should be the same mathematical function as the original ReLU, just via different implmentations.

For each of the three implementations, plot the value of the derivative that PyTorch's autodiff gives you for the x values $\{-1,-.75,-.5,-.25,0,.25,.5,.75,1\}$

### Task for the lab
Your task is to define a function $f$ in Python that is mathematically equivalent to $\sin(x)$, but such that when you do AD on your implementation, the returned derivative is
$$f'(x) = \begin{cases} \cos(x) & x \neq \frac12 \\ 3.8 & x = \frac12\end{cases}$$

For credit for the lab, turn in a PDF (upload to Canvas) showing your Python code and a plot of the derivative.  

*When you plot your derivative, if you use `torch.linspace` or similar to make the $x$ values, be sure to include the point $x=\frac12$*

### Notes
This lab is inspired by the paper [A mathematical model for automatic differentiation
in machine learning](https://hal.science/hal-02734446/file/finalVersion.pdf) by Jérôme Bolte and Edouard Pauwels, NeurIPS 2020

PyTorch has info on [Autograd mechanics](https://pytorch.org/docs/stable/notes/autograd.html), including:
- [Gradients for non-differentiable functions](https://pytorch.org/docs/stable/notes/autograd.html#gradients-for-non-differentiable-functions)