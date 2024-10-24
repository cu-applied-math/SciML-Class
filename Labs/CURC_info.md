Information for our class and our usage of [Research Computing](https://www.colorado.edu/rc/)

As part of lab 1, you made an account with research computing, which gives you access to `ucb-general`

Once you send the instructor your identikey, they will add you to our classes special allocation, `ucb549_peak1`.  This gives us slightly higher priority (and in fact, if we use it consistently, that helps us keep the higher priority).

To see which [allocations](https://curc.readthedocs.io/en/latest/clusters/alpine/allocations.html) you belong to, use the [sacctmgr](https://slurm.schedmd.com/sacctmgr.html) command, part of the "SLURM" software that the cluster uses for scheduling. SLURM calls these "associations". The exact command is:
```bash
sacctmgr -p show associations user=$USER
```

You also can request what type of computers (which involves choosing which **cluster** (Alpine or Blanca), and within the cluster, which ["**partition**"](https://curc.readthedocs.io/en/latest/running-jobs/job-resources.html#partitions) e.g. `ahub` which controls the type of node, e.g., CPU vs GPU vs high-memory). There's also the Quality of Service (**QoS**) which is where you ask for very long running jobs, or request an interactive node, or on Blanca, assert your "condominium ownership" rights (e.g., `blanca-<group identifier>` vs the generic low-priority `preemptable`).

Note that selecting the type of computer involves two separate stages, (1) getting to the right cluster and partition where the computers are available, and then later (2) actually telling SLURM what you want.

## PyTorch on CURC
RC has created a conda environment for us, installed at `/curc/sw/conda_env/pytorch-cuda-12.4/`.  To do any copies or installs, either do this on an interactive session (e.g., via the ondemand portal) or a compile node (first login to a login node, then run `acompile` to get access to a compile node)

Here are three ways to use the environment:
1. Use it directly, as in
```bash
conda activate /curc/sw/conda_env/pytorch-cuda-12.4
```
This is fast, but the downside is that you cannot write to that directory, so you cannot install more packages.

2. Create your own, using the same packages: run
```bash
conda env create -f /curc/sw/conda_env/yaml/pytorch-cuda-12.4.yaml
```

3. Copy the environment to your own location (this takes a while, as it is about 10 GB):
```bash
cp -R /curc/sw/conda_env/pytorch-cuda-12.4 /projects/$USER/software/anaconda/envs
```

To see how to use it, look at the demo in `/curc/sw/conda_env/examples/pytorch-cuda-12.4`. Specifically,
```bash
$ cd /scratch/alpine/$USER
$ cp -Rf /curc/sw/conda_env/examples/pytorch-cuda-12.4 .
$ cd pytorch-cuda-12.4
$ sbatch job.slurm
```
This will run a quick (< 5 minute) 3 epoch training job w/ the MNIST dataset. The output is logged in `slurm-<jobid>.out`

#### Going further
First, it's a good idea to update your `.condarc` file [following these CURC instructions](https://curc.readthedocs.io/en/latest/software/python.html#configuring-conda-with-condarc) since your "home" disk is small, so you should use the "projects" disk

If you want to use via Jupyter, you need to make a kernel. Follow https://curc.readthedocs.io/en/latest/gateways/jupyterhub.html:
1. Activate the environment, e.g., your local copy of the `pytorch-cuda-12.4` environment

2. If `ipykernel` is not already installed (it should be pre-installed for the `pytorch-cuda-12.4` environment), then install it:
```bash
conda install -y ipykernel # also installs ipython and jupyter-core
```
3. Create the jupyter kernel as:
```bash
python -m ipykernel install --user --name myenv --display-name MyVirtualEnv
```
where "myenv" and "MyVirtualEnv" are any names you want (they can be the same or different).  It's now saved somewhere like `/home/$USER/.local/share/jupyter/kernels`

4. Now, login to https://ondemand.rc.colorado.edu/ and when you have an .ipynb file, you should be able to select the kernel to be MyVirtualEnv (as opposed to Python3 or something).
