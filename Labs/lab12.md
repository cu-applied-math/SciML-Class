# Lab 12: diffusion models
See [lab12_diffusion_models.ipynb](lab12_diffusion_models.ipynb) starter notebook.

We're going to look at diffusion models, using the new hugging face [`diffusion` package](https://pypi.org/project/diffusers/)
- The [documentation for "Diffusers"](https://huggingface.co/docs/diffusers/main/en/index) is good, with many examples. It includes most state-of-the-art variants, and discusses different tasks (e.g., generating an image from a text prompt, and other variants of sampling $x\sim p(x\mid y)$ for some prompt $y$)
- We'll look at the simplest, "unconditional" use case, where we just want a sample $x\sim p(x)$

This wraps many variants of diffusion models, such as the `DDPM` pipline (after the influential [Denoising Diffusion Probabilistic Models](https://proceedings.neurips.cc/paper_files/paper/2020/file/4c5bcfec8584af0d967f1ab10179ca4b-Paper.pdf) Ho et al. NeurIPS 2020 paper), as well as `DDIM`, `PNDM` and `PNDM`

Your task for this lab is to generate a sequence of images that start with a random normal 256 x 256 image and ends up with a celebrity face.

I **highly** suggest you follow the tutorial at https://colab.research.google.com/github/huggingface/notebooks/blob/main/diffusers/diffusers_intro.ipynb

**Deliverable** for Canvas:
- turn in a PDF of your notebook, showing some images, starting with random noise and ending up with a celebrity
- if you are not in class and did not discuss arrangements with the instructor (i.e., if you are not missing class for a valid reason), then your notebook should contain work on at least one more task, such as a conditional generation. See the examples of ["generative tasks"](https://huggingface.co/docs/diffusers/main/en/using-diffusers/img2img) like image-to-image or text-to-image on the Hugging Face "Diffusers" documentation site.
