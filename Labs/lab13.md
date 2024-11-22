# Lab 13: Metropolis MCMC
See [lab13_MCMC.ipynb](lab13_MCMC.ipynb) starter notebook.

This is the end of the semester, so the lab has less "hand-holding" than before!

Lab created by Stephen Becker, Nov 2024 for SciML class at University of Colorado Boulder

## Part 1: Metropolis algorithm
You're given the function `unnormalized_p` below which is proportional to a probability `p` that we'd like to sample from.  
- Code a **Metropolis** sampling algorithm
- Pick a jump function (to propose new samples)
- Run the code using your jump function and the provided `unnormalized_p` sampling function, and generate a lot of samples
- Plot a histogram of these samples and make some comments

## Part 2: nicer results
- We plotted the histogram before, but this has a resolution problem -- if we have a lot of bins, each bin has poor statistics; but if we have a few bins, we don't have much resolution.
- To supplement the histogram, plot a kernel density estimate of the MCMC samples. This also has a bias-accuracy tradeoff (due to the bandwidth selection), but it still gives some nice information that you don't get just from a histogram

## Part 3: independence
- Are the samples from our MCMC sampler independent? Do some computation to support your answer
  - I suggest looking at the autocorrelation function (ACF)
  - It's generally not possible to prove that samples **are** independent, but we can be quite certain sometimes that various samples are **not** independent.  In particular, independent samples are uncorrelated (though not necessarily vice-versa), so if you find correlations that you believe are not spurious, then the samples cannot be independent


## Part 4: if you have time...
- Numerically integrate `unnormalized_p` using `scipy.integrate.cumulative_simpson` to get the CDF and then do [inverse CDF sampling](https://en.wikipedia.org/wiki/Inverse_transform_sampling). This is only really practical in 1D.
  - [`np.interp`](https://numpy.org/doc/stable/reference/generated/numpy.interp.html) may be helpful
  - Plot a histogram of your samples using the inverse CDF sampling

- you could record how many failed steps are in the Metropolis algorithm, since that affects how efficient it is
- you could also explore the effect of different jump functions on the quality of your Metropolis algorithm

## Deliverable for Canvas:
- turn in a plot of your KDE estimate (with the reference measure `unnormalized_p` plotted as well)

## Helpful references
- on [MCMC](https://en.wikipedia.org/wiki/Markov_chain_Monte_Carlo)
  - Ch. 14 of Christopher Bishop's [Deep Learning](https://link.springer.com/book/10.1007/978-3-031-45468-4) (free PDF via SpringerLink)
  - Lecture notes on [ch 15 Sampling Methds](https://www.ece.virginia.edu/~ffh8x/docs/teaching/esl/15-Sampling-Methods.pdf) by Farzad Farnoud (U. of Virginia), part of [Statistical Learning and Graphical Models](https://www.ece.virginia.edu/~ffh8x/esl.html) class taught 2021 (see ch 5 [Linear Regression](https://www.ece.virginia.edu/~ffh8x/docs/teaching/esl/05-Linear-Regression.pdf) for "Bayesian Linear Regression" and an example of a non-informative prior that sets up a case where one has an unnormalized pdf).
  - Another set of lectures notes, these by Eric Xing at CMU, scribed 2014, [Approximate Inference: Markov Chain Monte Carlo](https://www.cs.cmu.edu/~epxing/Class/10708-14/scribe_notes/scribe_note_lecture17.pdf)
  - We're doing the "Metropolis" algorithm which uses a symmetric jump function, and can be seen as a special case of (the better-known) [Metropolis-Hastings](https://en.wikipedia.org/wiki/Metropolis%E2%80%93Hastings_algorithm) algorithm
  - For efficient, state-of-the-art MCMC with all the bells-and-whistles, in an interface that prevents you from making silly mistakes, try [PyMC](https://www.pymc.io/welcome.html). However, that's overkill for this lab, as we want to explore the very basics and get our hands dirty.
