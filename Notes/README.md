# Lecture notes for SciML, Fall 2024

## Week 1 (Mon Aug 26 - Fri Aug 30 2024)
- Monday: [course logistics](<01 Course intro.pdf>) and [what is this course about? Intro to SciML](<02 Intro to SciML forward problems.pdf>).  We started (just the first page) of [Intro to ML](<03 Intro to ML.pdf>)
  - [HW 1 and 2](../Homeworks/) have been posted
  - Please read the [syllabus](../syllabus.md) and [course policies](../policies.md)
- Wednesday
  - continue [Intro to ML](<03 Intro to ML.pdf>)
  - start [Training ERM](<04 Training ERM.pdf>)
- Friday: in-class lab, [lab01](../Labs/lab01.md). Please bring your laptop!

## Week 2 (Mon Sep 2 - Fri Sep 6 2024)
- Monday: no school (labor day)
- Wednesday:
  - finish [Training ERM](<04 Training ERM.pdf>)
  - [Preventing Overfitting](<05 Preventing Overfitting.pdf>)
  - Start [Artificial Neural Nets](<06 Artificial Neural Networks.pdf>)
- Friday: in-class lab, [lab02](../Labs/lab02.md). Please bring your laptop!

## Week 3 (Mon Sep 9 - Fri Sep 13 2024)
- Monday: CU Research Computing presentation
- Wednesday:
  - [Misc: catastrophic cancellation](<Misc_Catastrophic Cancellation.pdf>)
  - [Misc: details on MLP and convolutions](<Misc_MLP and Conv Net.pdf>)
  - Continue [Artificial Neural Nets](<06 Artificial Neural Networks.pdf>)
- Friday: in-class lab, [lab03](../Labs/lab03.md). Please bring your laptop!

## Week 4 (Mon Sep 16 - Fri Sep 20 2024)
- Monday
  - [Tricks etc for neural nets](<07 Tricks, and going farther.pdf>)
  - [HPC: computer memory](<08 HPC_ComputerMemory.pdf>)
  - [Automatic Differentiation](<09 Automatic Differentiation.pdf>)
- Wednesday
  - Finish [Automatic Differentiation](<09 Automatic Differentiation.pdf>)
- Friday: in-class lab, [lab04](../Labs/lab04.md) about AutoDiff acting funny. Please bring your laptop!

## Week 5 (Mon Sep 23 - Fri Sep 27 2024)
- Monday
  - Guest lecture from Jacob Spainhour on hand-coding gradients/adjoints
  - HW 4 is due tonight (the deadline was extended from last Friday)
- Wednesday
  - Start ODEs. See [ODE_notes](ODE_notes.md) for a link to a chapters worth of material from an undergraduate numerical analysis class
  - These notes are mainly for anyone who didn't take the prereq class; I have a link to youtube videos on Canvas for these
- Friday: in-class lab, [lab05](../Labs/lab05.md) about why we have both validation and testing data

## Week 6 (Mon Sep 30 - Fri Oct 4 2024)
- Monday
  - Finish ODE notes
  - Start optimization: [Unconstrained optimization](<10 Unconstrained Optimization.pdf>) then [SGD](<11 SGD.pdf>) 
- Wednesday
  - Finish previous optimization notes, and do [Constrained optimization](<12 Constrained Optimization.pdf>)
- Friday: in-class lab, [lab06](../Labs/lab06.md)
  - Nic (TA) gave a short talk about measuring computational complexity, in response to the backprop HW
  - The lab had sections on (a) complexity, (b) choosing the right scipy.optimize method, and (c) doing some scipy.optimize coding yourself.
  - We didn't make it very far...

## Week 7 (Mon Oct 7 - Fri Oct 11 2024)
- Monday
  - Finish up last bit of [Constrained optimization](<12 Constrained Optimization.pdf>)
  - Discuss **initialization** of neural networks
    - Follow [PyTorch Lightning tutorial](https://lightning.ai/docs/pytorch/stable/notebooks/course_UvA-DL/03-initialization-and-optimization.html)
      - and their [video](https://www.youtube.com/watch?v=X5m7bC4xCLY)
    - Other references: [blog post](https://pouannes.github.io/blog/initialization) and [deeplearning.ai chapter](https://www.deeplearning.ai/ai-notes/initialization/)
    - Interesting work by Jared Tanner's group on initialization: [Information-Bottleneck under Mean Field Initialization](https://people.maths.ox.ac.uk/tanner/papers/AbTa_InfBott_mean_field_ICML.pdf) (2020), [Activation Function design for deep networks: linearity and effective initialisation](https://people.maths.ox.ac.uk/tanner/papers/MAT_activation_design.pdf) (2021), [Mutual Information of Neural Network Initialisations: Mean Field Approximations](https://people.maths.ox.ac.uk/tanner/papers/TaUg_mutual_inf.pdf) (2021)
  - Discuss the "SIREN" paper
    - [their website](https://www.vincentsitzmann.com/siren/) and [paper](https://arxiv.org/abs/2006.09661)
    - 3 main ideas:
      - INR
      - Periodic (sinusoid) activation
      - Initialization
  - Not discussing NeRF (not science-related enough, though ideas like INR build somewhat on NeRF, though NeRF uses positional encoding)
- Wednesday
  - Introduce [PINN paper](https://doi.org/10.1016/j.jcp.2018.10.045) by M Raissi, P. Perdikaris, G Karniadakis (J Comp Phys, 2019)
    - My [handwritten notes on PINNs (7 pg)](<13 PINNs.pdf>)
    - Existing similar ideas, "INR" idea, and
    - Forward solving
      - Vanilla version: what exactly they are proposing
      - RK4 version
    - Inverse solving
    - 5 years later: hindsight, criticism and influence
    - Other resources
      - Perspective on PINNs a few years later;
        - ["Scientific Machine Learning Through Physics–Informed Neural Networks: Where we are and What’s Next"](https://link.springer.com/article/10.1007/s10915-022-01939-z) by S Cuomo, V Schiano Di Cola, F Giampaolo, G Rozza, M Raissi & F Piccialli (J Sci Comp, 2022)
        - ["Physics-informed machine learning"](https://www.nature.com/articles/s42254-021-00314-5) by G Karniadakis, I Kevrekidis, L Lu, P Perdikaris, S Wang & L Yang (Nature Review Physics, 2021)
      - Limitations (note: the original PINN paper did *not* advocate replacing conventional solvers with neural nets)
        - Solving PDEs in a least-squares way has been tried before, e.g., the [First-order system least squares (FOSLS) for coupled
fluid-elastic problems](https://amath.colorado.edu/pub/fosls/coupled1.pdf) approach (Heys, Manteuffel, McCormick, Ruge; JCP 2003) and the least-squares finite element method (LSFEM) of [An alternative least-squares formulation of the Navier–Stokes equations with improved mass conservation](https://www.sciencedirect.com/science/article/abs/pii/S0021999107002185?via%3Dihub) (Heys, Lee, Manteuffel, McCormick; JCP 2007)
        - [Limitations of physics informed machine learning for nonlinear two-phase transport in porous media](https://www.dl.begellhouse.com/journals/558048804a15188a,583c4e56625ba94e,415f83b5707fde65.html) (Fuks and Tchelepi; J of ML for Modeling and Computation, 2020)
        - [Can Physics-Informed Neural Networks beat the Finite Element Method?](https://arxiv.org/abs/2302.04107) (Grossmann, Komorowska, Latz, Schönlieb; 2023)
        - [Weak baselines and reporting biases lead to overoptimism in machine learning for fluid-related partial differential equations](https://www.arxiv.org/abs/2407.07218) (McGreivy, Hakim; 2024)
    - Background on PDEs
      - [Burgers Equation](https://people.maths.ox.ac.uk/trefethen/pdectb/burgers2.pdf) from Nick Trefethen and Kristine Embree's unfinished ["PDE Coffee Table book"](https://people.maths.ox.ac.uk/trefethen/pdectb.html)
      - [KdV Equation](https://people.maths.ox.ac.uk/trefethen/pdectb/kdv2.pdf),
      - [Time-dependent Schrodinger equation](https://people.maths.ox.ac.uk/trefethen/pdectb/schr2.pdf), and then
      - [Allen-Cahn](https://people.maths.ox.ac.uk/trefethen/pdectb/allen2.pdf) equation, all from the same coffee table book
- Friday: in-class lab, [lab07](../Labs/lab07.md), a followup to last week's lab

## Week 8 (Mon Oct 14 - Fri Oct 18 2024)
- Monday
  - Finish up PINNs
  - [Case-study of PINNS for gravity modeling](<Misc PINN Case study gravity modeling.pdf>) based on the paper [Physics-informed neural networks for gravity field modeling
of small bodies](https://hanspeterschaub.info/PapersPrivate/Martin2022d.pdf) by John Martin and Hanspeter Schaub (CU Aerospace dept), 2022
- Wednesday
  - Getting ready for more inverse problems, we're talking about the adjoint state method
  - [Adjoint State Method notes](<14 Adjoint State Method.pdf>), following [Neural Ordinary Differential Equations](https://proceedings.neurips.cc/paper_files/paper/2018/file/69386f6bb1dfed68692a24c8686939b9-Paper.pdf) by Chen, Rubanova, Bettencourt, and Duvenaud (NeurIPS 2018)
- Friday: in-class lab, [lab08](../Labs/lab08.md)
  - on the adjoint-state method for an ODE with a single observation

## Week 9 (Mon Oct 21 - Fri Oct 25 2024)
- Monday
  - Intro to [inverse problems](<15 Inverse Problems.pdf>) and some classical solution methods
    - for classical methods, [Survey of Multifidelity Methods in Uncertainty Propagation, Inference, and Optimization](https://epubs.siam.org/doi/abs/10.1137/16M1082469) (by Peherstorfer, Karen Willcox, and Max Gunzburger, SIAM Review 2018) is a review of surrogate models
    - and [Approximation of high-dimensional parametric PDEs](https://www.cambridge.org/core/journals/acta-numerica/article/abs/approximation-of-highdimensional-parametric-pdes/B2C26BF6F63B7734FEAD1C59738E8730) (by Cohen and DeVore, Acta Numerica 2015) takes an approximation-theoretic viewpoint
- Wednesday
  - Start on Operator learning for inverse problems, starting with [DeepONets](<16 DeepONets.pdf>)
- Friday: in-class lab, [lab09](../Labs/lab09.md)
  - on system identification with WENDy

## Week 10 (Mon Oct 28 -- Fri Nov 1 2024)
- Monday
  - Background on [Fourier transform](<Misc Fourier Transform Background.pdf>)
  - Background on [kernel methods and Random Fourier Features](https://github.com/stephenbeckr/ML-theory-class/blob/main/Notes/Spring2020/ch16_kernels.pdf)
- Wednesday
  - [Fourier Neural Operator (FNO)](<17 FNO.pdf>) notes, based on the [Fourier Neural Operator for Parametric Partial Differential Equations](https://arxiv.org/abs/2010.08895) Li et al. ICLR 2021 paper.
    - That group has a followup paper [Neural Operator: Learning Maps Between Function Spaces With Applications to PDEs](https://www.jmlr.org/papers/volume24/21-1524/21-1524.pdf) (Kovachki et al. JMLR 2023) which puts it in a bit more context
- Friday: in-class lab, [lab10](../Labs/lab10.md)
  - on the curse of dimensionality, exploring quadrature vs Monte Carlo integration

## Week 11 (Mon Nov 4 -- Fri Nov 8 2024)
- Monday
  - [18 Image Processing Background](<18 Image Processing Background.pdf>)
  - [19 Image Denoising Survey](<19 Image Denoising Survey.pdf>), based on [Image Denoising: The Deep Learning Revolution and Beyond : A Survey Paper](https://arxiv.org/abs/2301.03362) by Elad, Kawar and Vaksman (2023) [SIAM J Imaging Science](https://epubs.siam.org/doi/10.1137/23M1545859) )
- Wednesday
  - Finish Image Denoising Survey
- Friday: in-class lab, [lab11](../Labs/lab11.md)
  - on solving inverse problems via denoisers

## Week 12 (Mon Nov 11 -- Fri Nov 15 2024)
- Monday
  - Finish Image Denoising Survey
  - Look at some results from [Diffusion Posterior Sampling for General Noisy Inverse Problems](https://openreview.net/forum?id=OnD9zGAGT0k), by Chung, Kim, Mccann, Klasky and Ye, ICLR 2023
    - See their [code](https://github.com/DPS2022/diffusion-posterior-sampling)
Wednesday
  - Follow Christopher Bishop's [Deep Learning](https://www.bishopbook.com/) book
  - [ch 16 on sampling](<20 Sampling.pdf>)
  - [ch 20 on diffusion models](< 21 Diffusion Models.pdf>)

# Future weeks (tentative)

- Generative models, Bayesian Inverse Problems
## Week 13
- (finish / expand on previous topics)
## Thanksgiving week, no class
## Week 14-15
- guest lectures
