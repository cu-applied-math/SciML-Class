# Debrief after Lab 1

For running the Python script, two points to make:

### GPUs appear faster than CPUs
... and for the large matrix size, they are about 100x faster (according to the results turned in).

However, a few caveats:
1. most CPU comparisons used just a single core (since they were run in the cloud, where you get the minimal resources needed for a task unless you ask or pay for more).  Running on a 12-core nice desktop would give very different results
2. in our case, the memory for the matrix was created directly on the GPU (so no cost for memory transfer), and also probably could fit all inside the GPU memory. If either situation changes, then you'd have to pay for the cost of transfering memory between CPU and GPU

### Timings on Mac's with MPS looked funny
The times seemed to not depend on the size. This is a bug!  We were following [https://pytorch.org/tutorials/recipes/recipes/benchmark.html](https://pytorch.org/tutorials/recipes/recipes/benchmark.html) which recomments PyTorch's timing over Python's standard timing when using the GPU since standard timing only looks at how long the CPU is working and then doesn't record GPU time.  Well, PyTorch's version doesn't work on MPS apparently.
