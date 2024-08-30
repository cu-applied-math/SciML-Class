# -*- coding: utf-8 -*-
"""lab01-benchmark.ipynb
For SciML class
Don't forget, you may need to setup your environment
e.g.,
  on a cluster, this is often done with the 'module' command
  on your computer, this is often done with `conda activate [yourenvironment]`
  on colab, you can copy-and-paste this into a jupyter notebook
"""

# Lab 1 benchmarking script for SciML class
import torch
import torch.utils.benchmark as benchmark
import numpy as np
from matplotlib import pyplot as plt

import platform, subprocess, sys
if platform.system() == 'Windows':
  print('Windows')
else:
  print( platform.system())  # "Darwin" = Mac
  print(platform.processor())
 # print(subprocess.run(['cat', '/proc/cpuinfo'], stdout=subprocess.PIPE).stdout.decode('utf-8')) # lengthy output
hostname = platform.node()
print('hostname of the computer is:', hostname)

print("Torch version is", torch.__version__)
print("Numpy version is", np.__version__)
print("Python version is", sys.version)
# np.show_config() # not always accurate, and very lengthy output

device = (
    "cuda"
    if torch.cuda.is_available()
    else "mps"
    if torch.backends.mps.is_available()
    else "cpu"
)
print(f"Using {device} device")
# If you have more than one thread, you can try benchmarking with all your threads,
# and then try with just one thread (to do so, uncomment this line:)
#torch.set_num_threads(1)

num_threads = torch.get_num_threads()
print(f"Number of threads: {num_threads}")

nReps = 10

nList = np.logspace(2, 3.8, 15, dtype=int)
times = np.zeros(len(nList))

for i,n in enumerate(nList):

  A = torch.randn(n, n, device=device)
  B = torch.randn(n, n, device=device)

  # Following tutorial at https://pytorch.org/tutorials/recipes/recipes/benchmark.html
  t = benchmark.Timer(
      stmt="torch.matmul(A, B)",
      setup="import torch",
      num_threads=num_threads,
      globals={"A": A, "B": B},
  )
  results = t.timeit(nReps)
  #print(results)
  times[i] = results.mean
  print(f"i is {i+1:2d} of {len(nList)}, n = {n:5d}, time = {times[i]:.3e}")

plt.loglog(nList,times,'o-')
plt.xlabel('Size n')
plt.ylabel('Time (s) for matrix multiply')
str = f'device = {device}, num_threads = {num_threads}, OS is {platform.system()}'
plt.title(str)
plt.grid()
plt.ylim( [1e-5, 10] ) # make it consistent
plt.savefig(f'lab01_matmul_time_{hostname}.pdf') # PDFs preferred over PNG since they embod fonts rather than rasterize them
# plt.show()

