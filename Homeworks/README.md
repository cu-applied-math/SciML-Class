# Scientific Machine Learning: Homeworks
Fall 2024

The homework assignments are here, but homework **solutions** are on Canvas

- [HW 1](APPM4720SciML_Fall2024_HW01.pdf) A review of numerical analysis. Due Fri Aug 30 2024.
- [HW 2](APPM4720SciML_Fall2024_HW02.pdf) Getting started with CIFAR10. Due Fri Sep 6 2024.
- [HW 3](APPM4720SciML_Fall2024_HW03.pdf) Nicer workflow: PyTorch Lightning or other ways to log, profile, debug. Due Fri Sep 13 2024.
- [HW 4](APPM4720SciML_Fall2024_HW04.pdf) Automatic Differentiation by hand. Due Fri Sep 20 2024. [Update: due date extended to Mon Sep 23 2024]
- [HW 5](APPM4720SciML_Fall2024_HW05.pdf) ODE solvers and conservation of energy. Due Mon Sep 30 2024.
- [HW 6](APPM4720SciML_Fall2024_HW06.pdf) Constrained optimization. Due Mon Oct 7 2024.
- [HW 7](APPM4720SciML_Fall2024_HW07.pdf) Baby PINNs. Due Mon Oct 14 2024.
- [HW 8](APPM4720SciML_Fall2024_HW08.pdf) PINNs in inverse mode. Due Mon Oct 28 2024.
- No more homeworks, but there is a final project. See [Final Project info](ProjectInformation.md), due on Sunday December 15 2024 at 1:30 PM



<!--
[//]: # [HW 5/6](APPM5630Spring21Homework05-06.pdf) HW 5 and 6 on logistic regression; checking if strongly convex, strongly smooth; derive gradient/Hessian; implement gradient check; implement gradient descent with backtracking linesearch
[//]: # - [HW 7/8](APPM5630Spring21Homework07-08.pdf) HW 7 and 8 on logistic regression and 2D total-variation, and proximal methods. You have 3 weeks to do this HW
[//]: # - [HW 9/10](APPM5630Spring21Homework09-10.pdf) HW 9 and 10 on compressed sensing and perturbation analysis, applied to the Handel audio clip (using a matrix-free linear operator). See the [HW10](HW10/) subfolder for helper files.
-->

# Homework "debriefs"
Solutions are not posted on the web (they are on Canvas, available to other instructors upon reasonable request), but here are some "take-away" messages from each homework.

- HW 1, review of numerical analysis
  - **take-away**: Setup students for future discussions; basic understanding of interplay between algorithms and implementation. Numerical differentiation is unstable.
- HW 2, PyTorch and CIFAR10
  - **take-away**: Basic classification in PyTorch is fairly starightforward to setup; become familiar with PyTorch
- HW 3, workflow with PyTorch / Lightning
  - **take-away**: Learn to profile, organize code, look at validation vs training error. Setup students for future experimentation with code.
- HW 4, automatic differentiation
  - **take-away**: How autodiff works at a high-level, and the difference in memory and computation between forward- and reverse- style autodiff
- HW 5, ODE solvers
  - **take-away**: Familiarity with ODEs, considerations on solvers besides just local accuracy (e.g., conservation of energy)
- HW 6, constrained optimization
  - **take-away**: The difficulty constraints add; the penalty method isn't a great method though it's easy to implement. Thinking about how this will relate to future constraints for ML (e.g., PINNs constraints)
- HW 7, baby PINNS
  - **take-away**: Understand the PINNs idea in forward mode, and some practical experience to help with the next HW and projects
- HW 8, PINNs in inverse mode
  - **take-away**: PINNs show their true potential when used in inverse mode. Understand the idea of PINNs in inverse mode. See the sensitivity of training them (it's difficult, and not always reproducible!) even on easy problems


# Submission FAQ

### General

**Gradescope** has a [submission guide](https://gradescope-static-assets.s3.amazonaws.com/help/submitting_hw_guide.pdf) that recommends software for your phone to take pictures of written homework and convert it to a PDF (your final submission to Gradescope must be a PDF).

Note: the links in the PDFs will not work if you view the PDF on github, but if you open the PDF in its own tab, or download it, all the links should work.

**Collaboration**: Collaboration with your fellow students is OK and in fact recommended, although direct copying is not allowed.

**Internet**: The internet is allowed for basic tasks (e.g., looking up definitions on wikipedia, or documentation, or following basic tutorials) but it is
not permissible to search for answers to exact problems or to post requests for help on forums such as [math.stackexchange.com](http://math.stackexchange.com/)
or to look at solution manuals.

#### Merging multiple PDF files

**Mac** You can use the Preview software that comes with Mac, and drag-and-drop in the Thumbnail view, or follow these [instructions](https://support.apple.com/en-us/HT202945).

**Linux** install `pdftk` (e.g., `apt-get install pdftk`), and the on the command line, it's just `pdftk inputFile1.pdf inputFile2.pdf cat output outputFileName.pdf`.  This works on Mac and Windows too (on Mac, the exact command line works; on Windows, I'm not sure).

**Windows** there are [lists of free web- and desktop-based software](https://superuser.com/a/34294), including [i-love-pdf](https://www.ilovepdf.com/merge_pdf), but [PDFtk](https://www.pdflabs.com/tools/pdftk-the-pdf-toolkit/) is one of the most classic and respected (no viruses). I haven't used PDFtk on Windows, but the website claims they have a GUI; or if you don't like their GUI, try a [3rd party GUI that uses PDFtk](https://www.pdflabs.com/tools/pdftk-the-pdf-toolkit/).

### Python
For overall Python, and numpy in particular, Matlab users might like [NumPy for Matlab users](https://numpy.org/doc/stable/user/numpy-for-matlab-users.html).

For **plotting** in Python using Matplotlib, try these [plotting cheatsheets](https://github.com/matplotlib/cheatsheets) and [controlling figure aesthetics](https://seaborn.pydata.org/tutorial/aesthetics.html) with seaborn.


#### Jupyter

Tips for exporting jupyter notebook code to a PDF:

- You can try this [Notebook to PDF conversion website](https://htmtopdf.herokuapp.com/ipynbviewer/) that some of our students have had good luck with

- Or try `nbconvert` which requires [`pandoc`](https://pandoc.org/installing.html). You can do this on [Colab](https://colab.research.google.com/), following the [instructions here](https://stackoverflow.com/a/54191922) (but note that you may need to add a backslash before any white space when you run commands, e.g., change a command like

`!cp drive/My Drive/Colab Notebooks/Untitled.ipynb ./`
to
``!cp drive/My\ Drive/Colab\ Notebooks/Untitled.ipynb ./``
)

Note that if you include latex in the jupyter notebook, when you run `nbconvert`, you cannot have any whitespace near the `\$` symbols for math due to a requirement of `pandoc` (see [here](https://pandoc.org/MANUAL.html#extension-tex_math_dollars)).  So, ``$ f(x) = 3x^2 $`` will not work, but `$f(x) = 3x^2$` will be OK.

The downside of `nbconvert` is that images are saved as png, not pdf, so fonts don't come through, but that's not a big deal for homework.

If you run jupyter locally, you might be able to run `nbconvert` without using the command line; go to "Download" the "PDF via LaTeX".

#### Python source code (not Jupyter)
The *non-preferred* ways are (1) screenshot of your editor (not so nice since it's an image not text, but at least you get syntax color highlighting), and (2) export from a text editor to PDF (not so nice if you don't get syntax color highlighting).

It's not nice to the graders to submit code without syntax color highlighting!

Better ways: it depends on your system and editor, but there are many ways. For example, this [stackoverflow 'printing python code to PDF'](https://stackoverflow.com/q/20412038) offers several suggestions. For example, since I already use `vim` and its setup with syntax highlighting, I can do [this answer](https://stackoverflow.com/a/20412421) and do `vim abc.py -c ":hardcopy > abc.ps" -c ":q"` followed by `ps2pdf abc.ps abc.pdf` -- no extra software needed!


### Matlab

You can use the export notebook features in Matlab (it can handle latex) if you want; see the [Live-Editor](https://www.mathworks.com/products/matlab/live-editor.html); there are also claims on the internet that it's easy to get Jupyter to run with a Matlab kernel, so you could use Jupyter.

To just export a figure, there are builtin methods, but one of the nicer ways is to use [export_fig](https://www.mathworks.com/matlabcentral/fileexchange/23629-export_fig), which works like `export_fig MyFileName -pdf -transparent` and makes a file `MyFileName.pdf` (note that PDF files for figures are preferred, since then the text is saved as a font and not bitmapped)
