# Lab 5, SciML class

Why do we use both **validation** and **testing** sets?

See the [lab05.ipynb](lab05.ipynb) starter notebook

## Part 1: Hoeffding's inequality

Two-sided [Hoeffding inequality](https://en.wikipedia.org/wiki/Hoeffding%27s_inequality#Special_Case:_Bernoulli_RVs) for Bernoulli r.v.
```math
\mathbb{P}\left[ \left| \frac{1}{n}S_n - \mu  \right| \ge t\right] \le 2 \exp\left( -2nt^2\right)
```
where $S_n=X_1+X_2+\ldots+X_n$ is the sum of $n$ **independent** Bernoulli random variables.  Recall $X$ is a Bernoulli random variable (with some parameter $p$) if it takes on two possible values, $\{0,1\}$, and is equal to $1$ with probability $p$ and equal to $0$ with probability $1-p$.


Let $\mu$ be the true risk of a binary classifier $f$ (using the 0-1 loss $\ell$), and suppose we have $n$ independent samples (that are also independent of $f$), and let $\frac{1}{n}S_n$ be the empirical risk (still using the 0-1 loss) on these samples.  (Think of these as validation or testing samples)

**Q**: If we want to estimate $\mu$ to an accuracy of $\pm t$, with a confidence of $p=1-\alpha$, how many samples $n$ do we need? Do this for $t=0.001, 0.01, 0.02$ and $0.05$, and for $\alpha$ being $10^{-1},10^{-2},10^{-3},10^{-4},10^{-5}$. Make a table of the resulting $n$ values.

Comment on whether $p$ or $t$ has a "bigger effect".

## Part 2: Numerically verify Hoeffding's inequality
Using the [lab05.ipynb](lab05.ipynb) starter notebook, we have a simple neural net that does binary classification on 1D inputs.

Find $\mu$ by using very very large "test" data

Run many experiments (say, 1000), each time drawing a new validation set of size 1000, and look at the results compared with $\mu$.  Is this what you expected via Hoeffding's inequality?  Comment on this.

## Part 3: Picking the best model
Now, fix a single validation set of size 1000

Run 10 different models (for now, just use different initializations, no training), and pick the one that has the highest validation error.

Then compare that to the "true" test error.

Repeat this experiment 10 times. Are the results similar to part 2?

## Part 4: now with training
Repeat part 3 but train the models. Each model should be different -- it could just be the different initialization, or it could be different hyperparameters.

# Deliverables
Make a PDF of the table from part 1, **and** a short written commentary about your efforts for parts 2--4 (you can also include code). You do not need to finish parts 2--4.