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

## Week 8 (Mon Oct 14 - Fri Oct 18 2024)
- Monday
  - Finish up PINNs
  - [Case-study of PINNS for gravity modeling](<Misc PINN Case study gravity modeling.pdf>) based on the paper [Physics-informed neural networks for gravity field modeling
of small bodies](https://hanspeterschaub.info/PapersPrivate/Martin2022d.pdf) by John Martin and Hanspeter Schaub (CU Aerospace dept), 2022
- Wednesday
  - Start on Operator learning

# Future weeks (tentative)

## Week 9 (Mon Oct 12 - Fri Oct 25 2024)
- Generative models, Bayesian Inverse Problems
## Week 10-13
- (finish / expand on previous topics)
## Thanksgiving week, no class
## Week 14-15
- guest lectures
