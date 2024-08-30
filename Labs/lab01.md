# Lab 1, SciML class

There are three parts to this lab.

### Part 1
We will access a few different computers.

1. To use the [Jetstream2](https://jetstream-cloud.org/index.html) computers, follow [Step 1: Create your NSF "ACCESS" account](https://jetstream-cloud.org/get-started/index.html) of their documentation and create an account.

   You do not need to request an allocation (I already created an allocation, so just send me your user name and I will add you to our allocation)

2. Create a [CU Research Computing (CURC) account](https://www.colorado.edu/rc/). This will be linked to your normal CU identikey after you create it. You'll need to use a 2 factor athentication method (like a smart phone app)

3. Make sure you can use [Google colab](https://colab.research.google.com/), which may require a google account

### Part 2
Run the [`lab01_benchmark.py`](lab01_benchmark.py) script on as many computers as you can (and on colab, you can run it several times for different runtime types, e.g., with and without GPUs). In particular, try to run it on:
1. a jetstream2 computer (see their [getting started](https://docs.jetstream-cloud.org/getting-started/overview/) documentation. Make sure you ["shelve"](https://docs.jetstream-cloud.org/getting-started/instance-management/) your instance when done, otherwise it will continuously use up our allocation)
2. CURC. The simplest way to get started (but probably no GPU access) is via the [ondemand portal](https://ondemand.rc.colorado.edu/) with [open ondemand documentation here](https://curc.readthedocs.io/en/latest/open_ondemand/index.html), since this can give you a jupyterlab environment (similar to colab)
3. Colab.
4. Your personal computer

The benchmark script makes a plot of performance. To receive full-credit for this lab, upload at least **one plot** (i.e., from at least one computer) to Canvas.  Ideally you'll be able to create several plots (one for each computer), but that's not necessary for full credit.

### Part 3
If you've finished part 2 (or done at least enough to get credit and are tired of logistics), let's do some coding.  

*You do not need to turn in anything from this part of the lab in order to get credit, as I do not expect everyone to get this far in one class period!*

Using `pytorch`, solve the linear least squares optimization problem $$\min_x \|Ax-b\|_2^2$$ using gradient descent. You can use [builtin optimizers](https://pytorch.org/docs/stable/optim.html) to PyTorch, and use can use the builtin automatic differentiation. (Of course in this case, the gradient is easy to implement by hand, but for practice you could try it both ways)

*Hint*: if you don't want to play guess-and-check with stepsizes (aka learning rates), use a stepsize $\eta \in (0, 2/L)$ where $L$ is the square of [`numpy.linalg.norm`](https://numpy.org/doc/stable/reference/generated/numpy.linalg.norm.html) (using `ord=2` so that you compute the ["spectral norm"](https://en.wikipedia.org/wiki/Matrix_norm#Spectral_norm_(p_=_2)))

**Bonus**: do this exercise in Julia. I'd suggest using [Zygote](https://fluxml.ai/Zygote.jl/stable/) (part of the [Flux](https://fluxml.ai/) machine learning toolbox for Julia, and also used by Lux, the main alternative to Flux) for automatic differentiation, which is one of the many [AD packages in Julia](https://juliadiff.org/).
