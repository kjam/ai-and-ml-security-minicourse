## Mini-Course: AI/ML Security

This repository is for the [Probably Private YouTube mini-course](https://www.youtube.com/playlist?list=PLJkNSeYcYBlC88vkG58yx3fHSobmCmDw_) to introduce curious technical persons to the field of AI/ML security. In this mini-course, you'll learn:

- Red Teaming basics
- Adversarial machine learning
- Interesting attacks from research
- Applicable defenses and controls

Currently, these notebooks are in progress, so feel free to fork but expect changes!

If you have a suggestion for another library or additional topic, feel free to drop me a line. :)

## Repository Information

This project contains the Jupyter Notebooks and the associated requirements file for Katharine Jarmul's AI/ML Security Mini-Course. It contains exercises (/notebooks) and solutions (/solutions), as well as any data or files needed (/data).

To have a look at an earlier version of the course which will work on older versions of Python, check out the [original course repository (2019)](https://resources.oreilly.com/live-training/security-for-machine-learning).

### Local Installation

To install locally, please follow these steps:

These lessons has been tested for Python 3.9-Python 3.12 and primarily use the latest release of each library, except where versions are pinned. You likely can run most of the code with older releases, but if you run into an issue, try upgrading the library in question first.

```pip install -r requirements.txt```

```
$ conda create -n mlsecurity --copy python=3.12
$ conda activate mlsecurity
$ conda install pip
$ pip install -r requirements.txt
```

### Installation tips for getting started with no Python environment

1. Download Anaconda: https://www.anaconda.com/download
2. Download GitHub Desktop: https://desktop.github.com/download/
3. In GitHub Desktop, go to this repository and clone it.
4. Download ollama for desktop: https://ollama.com/download
5. Download a few llamafiles: https://github.com/Mozilla-Ocho/llamafile?tab=readme-ov-file#other-example-llamafiles and make sure to make them executable (If new to this, search: your OS + how to change file permissions to make executable)
6. Open an Anaconda prompt, navigate to where the GitHub repository is, follow the conda install instruction above. 
7. Launch Jupyter Notebook by typing 'jupyter notebook' in that same prompt. More info on Step 6+7 here: https://dev.to/saintniyi/launch-anaconda-jupyter-notebook-environment-from-any-folder-in-any-drive-58mj

If you run into any issues, please let me know!

### Repository structure

This repository will introduce external submodules with modifications (coming soon as I rework for newer Python versions) -- this is primarily due to making things compatible with Py3 or Jupyter. Some repositories you might want to take a look at installing individually or tracking changes are:

- [Cleverhans](https://github.com/tensorflow/cleverhans)
- [Foolbox](https://github.com/bethgelab/foolbox)
- [ModelExtraction](https://github.com/ftramer/Steal-ML)
- [EvadeML-Zoo](https://github.com/mzweilin/EvadeML-Zoo)

To have a look at an earlier version of the course which will work on older versions of Python, check out the [original course repository (2019)](https://resources.oreilly.com/live-training/security-for-machine-learning).

### Corrections?

If you find any issues in these code examples, feel free to submit an Issue or Pull Request. I appreciate your input!

### Questions?

Reach out to @kjam here or [via the Probably Private contact options](https://probablyprivate.com/about/).
