# BirdSpy

Deep learning tool for automated detection of artic birds from time-lapse camera images. Uses data from the Citizen Science project [SeaBird Watch](https://www.zooniverse.org/projects/penguintom79/seabirdwatch).

## CNN Framework

The Convolutional Neural Network (CNN) framework used is that of Victor Lempitsky and Andrew Zisserman, as introduced in their paper [Learning To Count Objects in Images](http://www.robots.ox.ac.uk/~vgg/research/counting/index.html). I have no ownership over this code (in the folder `counting/`) and I am very grateful to them for making it freely accessible.

## Installation

This repository will require python and matlab to run, both of which have extensive installation instructions online. The `birdspy` python package is not yet pip-installable, but you can install a local version by running the following command from the top level directory:

```
pip install -e .
```

The `-e` flag installs the package in editable mode, so any changes you make to the code will be reflected in the distribution you then run (so re-installation is not necessary).
















