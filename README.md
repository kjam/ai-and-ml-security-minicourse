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

Shield: [![CC BY-SA 4.0][cc-by-sa-shield]][cc-by-sa]

This work is licensed under a
[Creative Commons Attribution-ShareAlike 4.0 International License][cc-by-sa].

[![CC BY-SA 4.0][cc-by-sa-image]][cc-by-sa]

[cc-by-sa]: http://creativecommons.org/licenses/by-sa/4.0/
[cc-by-sa-image]: https://licensebuttons.net/l/by-sa/4.0/88x31.png
[cc-by-sa-shield]: https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg

### Local Installation

To install locally, please follow these steps:

#### (Recommended) Using pixi

[pixi](https://pixi.prefix.dev/latest/) is a package management tool useful for installing Python
and project dependencies. It has nice support for CPU and GPU environments.

After cloning the repo:

1. [Install pixi](https://pixi.prefix.dev/latest/installation/).
2. Install and activate the pixi environment: `pixi install`
3. Check the dependencies installed: `pixi list`
4. Run a command: `pixi run jupyter lab`

Helpful commands in [Getting Started](https://pixi.prefix.dev/latest/getting_started/):
- `pixi -h` - help
- `pixi self-update` - update pixi itself

#### Using uv

If you are using [uv](https://docs.astral.sh/uv/), you can also use the pyproject.toml file to install the necessary requirements.

```
$ uv venv
$ source .venv/bin/activate
$ uv sync
$ uv run jupyter lab
```

#### Using conda+pip

If using [conda](https://www.anaconda.com/docs/getting-started/miniconda/install/overview), you can create an environment using Python3.12 and use the requirements file with pip. 

```
$ conda create -n mlsecurity --copy python=3.12
$ conda activate mlsecurity
$ conda install pip
$ pip install -r requirements.txt
```

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
