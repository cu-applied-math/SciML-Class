# Syllabus for Scientific Machine Learning (SciML)

APPM 4720/5720 "Open Topics in Applied Mathematics: **Scientific Machine Learning** (SciML)"

University of Colorado Boulder, Fall 2024. Instructor Stephen Becker, with assistance from Nic Rummel, and course prep help from Cooper Simpson

For a detailed list of class policies see the [policies document](policies.md).

Machine learning, and in particular deep learning, has been successfully applied across almost any field imaginable. This results in a variety of perspectives one might take in learning and presenting material from this vast subject. This course takes the perspective of an applied mathematician and will cover topics specifically relevant to this background. Many other perspectives exist; see [Related Courses](#related-courses) for a list specific to CU.

We will call our perspective Scientifc Machine Learning, or SciML for short. SciML is a relatively new field and term, so a readily agreed upon definition is lacking. We will define it as follows:
>Scientific Machine Learning, often abbreviated SciML, combines classical aspects of computational science with techniques in machine learning, with a focus on solving problems in the scientific domain.

Often this involves fusing topics considered traditionally in applied math such as partial differential equations (PDEs) with deep learning.

Examples of topics this course **does not cover** include natural language processing (NLP), LLM, robotics and computer vision. We consider these to be in the domain of other departments.

### Learning Goals/Outcomes
[//]: # ( Not testable; high-level )
After the course, students will be ready to perform research in SciML (either in industry or academics), and will understand subtleties and pitfalls in both classical methods, data-driven methods and hybrid methods. They will understand pros and cons of various approaches, and be familiar with at least one recent approach in each of several domains of SciML.

With the learning goals in mind, the course is taught with PhD students in mind. Undergraduates are welcome to take the course but should be aware the course is designed for researchers.

### Learning Objectives
[//]: # ( Learning Objectives, i.e., quantifiable outcomes )
[//]: # ( Something measurable )
[//]: # ( more specific, measurable and observable, steps that help achieve goals )
- Students will understand standard **ML concepts** such as bias, variance, expressiveness, learnability, training, validation, over-fitting and generalization, and will learn best practices such as validation and cross-validation, and will also learn industry-standard packages and libraries (PyTorch or Jax in Python, or Lux in Julia) as well as other coding tools (debugging, profiling, logging and visualization, git). They will understand necessary concepts from **probability**
- Students will have a basic knowledge of **optimization** and training neural networks, being able to train their own neural network
- Students will understand basic **HPC** concepts including the memory hierarchy and how forward and reverse mode **automatic differentiation** work, as well as their limitations
- Students will know basic **linear algebra** and **numerical analysis** for solving differential equations, in particular they will be able to solve differential equations numerically using classical methods (not necessarily "from scratch", but at least understand how to use appropriate libraries), and understand basic **physical modeling**
- Finally, students will be aware of recent SciML approaches, know when SciML can be useful and what are shortcomings, and be able to implement an existing approach
  - To this end, students will produce a final report involving a professional writeup and coding
- A theme for the course is "scientific debugging", which includes all levels of usual code debugging, but also higher-level concepts applicable to the entire scientific workflow. How do we know a piece of code is correct? How do we know a discretization is accurate?

### Programming
We currently plan to focus on Python and the PyTorch library, however we may require graduate students to do some assignments in two separate libraries or languages in order to see the similarities and differences.

In the future, we may switch to either Python with the Jax library, or to Julia with the Lux library.

Some demonstrations may be done in Julia in order to illustrate concepts

## Topics in more detail

The topics below are not listed in the order they will be covered in class

### Part 1: Foundations

#### Software and workflow
- Numpy and basic scientific computing (floating point representations...)
- Frameworks
  - PyTorch, Lightning, etc.
- Remote computing
  - [CURC](https://www.colorado.edu/rc/)
- git and GitHub
- managing libraries and virtual environments
- IDEs
- debuggers, profilers, loggers

#### High performance computing (HPC) principals and computer architecture
- Memory models
- GPU, TPU and SIMD
- Automatic Differentiation (AD)
	- Forward vs backward mode
        - Mathematical formulation
	    - Implementation
        - Pros/cons of each, i.e. memory issues
        - Mixed mode
    - Limitations
    - Complicated scenarios
        - Loops, inverses, and recurrent networks
        - Differentiation of iterative solvers
    - Differentiable code

#### Optimization
- Types of solutions; stationary points; convexity
- Stochastic Gradient Descent (SGD) and variants
#### Numerical Analysis
- Basic linear algebra; solving linear regression efficiently and accurately
- Roundoff error
- Solving ODEs "by hand" and finite differences
- Understand approaches to solve PDEs and integral equations (and calling libraries to solve them)

#### Machine Learning and Prob/Stat
- Learning problem setup
	- Supervised vs Unsupervised vs Reinforcement
	- Goals; generalization; regularization; overfitting
- Simple models
    - Activations
    - Feed forward/Dense layers
    - Convolutions
- Universal approximation theorem
- Going beyond [MLPs](https://en.wikipedia.org/wiki/Multilayer_perceptron)
    - Recurrent layers
    - Residual connections
    - Autoencoders / U-Nets
    - Transformers
- Normalization
	- Data
	- Layers
- Misc
    - Parameter initialization
    - Train/Test/Validation
    - Cross-validation
    - Tricks (dropout, gradient clipping)
    - Ablation studies
    - Feature selection/engineering. Positional encodings
    - Vanishing gradients, mode collapse
- Gaussian Processes

## Part 2: SciML Techniques and Applications
There are countless applications of deep learning, but we will foucs on those that are most relevant to practitioners in applied math.

#### Special considerations for Scientific applications
- Infinite dimensional mappings
- Unstructured and Multi-Resolution Data
    - Graph convolution
    - Fourier convolution
    - Quadrature convolution
    - Implicit neural representation
- Invariance, equivariance, and enforcing physical laws

#### Generic Applications
- Forward problems
   - Closure modeling
   - Surrogate and reduced-order modeling (ROM)
- Inverse problems
- Uncertainty Quantification

#### Specific approaches and/or applications
These will typically follow specific papers. These are just examples of what we might follow
- Neural DE
    - Implicit neural representation (ex: SIRENs)
    - Neural DEs
    - Physics informed neural nets (PINNs)
        - relation to FOSLS; drawbacks, [comparisons to FEM](https://arxiv.org/abs/2302.04107), [limitations](https://www.dl.begellhouse.com/journals/558048804a15188a,583c4e56625ba94e,415f83b5707fde65.html)
- Neural Operators
    - Deep-operator networks ([Deep-O nets](https://www.nature.com/articles/s42256-021-00302-5))
    - [Fourier neural operator](https://arxiv.org/abs/2010.08895)
        - Wavelet and Laplace operator
    - Solving forward problems
- (Deterministic and Stochastic) Generative Models for ROM and UQ
    - Diffusion models
    - Autoencoders (AE), Variational AE (VAE) and Generative Adversarial Networks (GAN)
    - Examples: [Machine learning techniques to construct patched analog ensembles for data assimilation](https://www.sciencedirect.com/science/article/abs/pii/S0021999121004277) (by CU authors Yang and Grooms), [Bi-fidelity Variational Auto-encoder for Uncertainty Quantification](https://arxiv.org/abs/2305.1653) (by CU authors Cheng et al.)
- Other applications
    - Inverse problems and exploiting a known forward operator, such as unrolling approaches like this [MRI neural net](https://onlinelibrary.wiley.com/doi/full/10.1002/mrm.28827)
    - Closure modeling, [Invariant data-driven subgrid stress modeling in the strain-rate eigenframe for large eddy simulation](https://www.sciencedirect.com/science/article/abs/pii/S0045782522004923) (by CU authors Prakash et al.)
    - Time series and RNN, [Density Estimation for Entry Guidance Problems using Deep Learning](https://arxiv.org/pdf/2310.19684.pdf) (by CU authors Rataczak et al.)
    - Compression of scientific data
    - Bayesian Neural Networks
    - Reinforcement learning (RL) for protein folding (AlphaFold)
    - RL for matrix multiplication ([AlphaZero](https://www.nature.com/articles/s41586-022-05172-4))
    - [Universal instability theorem](https://sinews.siam.org/Details-Page/deep-learning-in-scientific-computing-understanding-the-instability-mystery) and implications

## Textbooks
As this is a recent field, there's not a standard textbook to follow. We'll use supplementary material (often from the web) as needed, such as the MIT and NVIDIA courses mentioned below.


## Related Courses
This list is not exhaustive and mostly focuses on CSCI. Departments such as ASEN, LING, INFO, and others also run classes covering relevant topics.

- CSCI 5922: Neural Networks and Deep Learning
- CSCI (4/5)622: Machine Learning
- CSCI 3832/5832: Natural Language Processing
- CSCI (4/5)722: Computer Vision
- CSCI (4/5)576: High-Performance Scientific Computing
- CSCI 5822: Probabilistic Modeling of Human and Machine Intelligence

A few courses from outside CU:

- MIT [Parallel Computing and Scientific Machine Learning (SciML): Methods and Applications](https://book.sciml.ai/), which uses Julia
- NVIDIA [Deep Learning for Science and Engineering](https://www.nvidia.com/en-us/on-demand/deep-learning-for-science-and-engineering/) , co-developed by Karniadakis (PINNs and DeepOnets) and uses PyTorch
- Brittany Erickson’s [MATH 607 Seminar on Physics-Informed Deep Learning](https://ix.cs.uoregon.edu/~bae/teaching/) at U Oregon which did a lot of PINNs

## Reference Material
- [Dive into Deep Learning](https://d2l.ai/index.html)
- [Julia SciML](https://sciml.ai/)
