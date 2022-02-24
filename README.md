# BirdSpy

Deep learning tool for automated detection of artic birds from time-lapse camera images. Uses data from the Citizen Science project [SeaBird Watch](https://www.zooniverse.org/projects/penguintom79/seabirdwatch).

## CNN Framework

The Convolutional Neural Network (CNN) framework used is that of Victor Lempitsky and Andrew Zisserman, as introduced in their paper [Learning To Count Objects in Images](http://www.robots.ox.ac.uk/~vgg/research/counting/index.html). I have no ownership over this code (in the folder `counting/`) and I am very grateful to them for making it freely accessible.

## Installation

This repository will require python and matlab to run, both of which have extensive installation instructions online. The `birdspy` python package is not yet pip-installable, but you can install a local version by running the following command from the top level directory:

```bash
pip install -e .
```

The `-e` flag installs the package in editable mode, so any changes you make to the code will be reflected in the distribution you then run (so re-installation is not necessary).

## Model 1

Based on code from V. Lempitsky, A. Zisserman, from [Learning To Count Objects in Images](http://www.robots.ox.ac.uk/~vgg/research/counting/index.html).

First install [VLFeat](https://www.vlfeat.org/), and then run the setup tool `vl_setup` through the MATLAB command:

```matlab
run('VLFEATROOT/toolbox/vl_setup')
```

where VLFEATROOT is the directory you installed vlfeat to, to get MATLAB to recognise VLFeat. To check that VLFeat is sucessfully installed,run `vl_version verbose`.

Generate your dataset using:

```python
import birdspy as bs
bs.ImageFactory.ground_truth_factory("counting_birds/data/")
```

specifying the location you want to read in your data from (this is the default). You can then run the MATLAB script `counting_birds/BirdCounting.m`. It may be necessaary to change the iteration limits and file paths there - the default option trains on the first 16 images and tests on the second 16.

This script generates the dense SIFT descriptors from a random weighted matrix, but it is preferred to pass a precomputed SIFT codebook for this dataset using VLFeat.

N.B The learning procedure calls methods from MATLAB's optimization toolbox which are very slow. These can be overloaded by faster solver through installlation of [MOSEK](www.mosek.com)- they are providing free academic licenses at the moment. Since MOSEK supercedes `linprog` and `quadprog` methods, no change in the code is required.

## Model 2

