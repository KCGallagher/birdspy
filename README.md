# BirdSpy

Deep learning tool for automated detection of artic birds from time-lapse camera images. I have used data from the Citizen Science project [SeaBird Watch](https://www.zooniverse.org/projects/penguintom79/seabirdwatch) for which I am very grateful. As I have no ownership over this data, I am unable however to publish it within this repository.

## CNN Framework

The Convolutional Neural Network (CNN) framework used is that of Victor Lempitsky and Andrew Zisserman, as introduced in their paper [Learning To Count Objects in Images](https://www.robots.ox.ac.uk/~vgg/publications/2010/Lempitsky10b/). I have no ownership over this code (in the folder `counting/`) and I am very grateful to them for making it freely accessible.

I include two separate models, based on differing loss functions. The first is based on a MESA-Distance, while the second (which is significantly faster to run) is a simple Ridge Regression. More information is avaliable [here](https://www.robots.ox.ac.uk/~vgg/research/counting/index.html).

## Installation

This repository will require python and matlab to run, both of which have extensive installation instructions online. The `birdspy` python package is not yet pip-installable, but you can install a local version by running the following command from the top level directory:

```bash
pip install -e .
```

The `-e` flag installs the package in editable mode, so any changes you make to the code will be reflected in the distribution you then run (so re-installation is not necessary).

## MESA-Distance

Based on code from V. Lempitsky, A. Zisserman, from [Learning To Count Objects in Images](http://www.robots.ox.ac.uk/~vgg/research/counting/index.html).

First install [VLFeat](https://www.vlfeat.org/), and then run the setup tool `vl_setup` through the MATLAB command:

```matlab
run('VLFEATROOT/toolbox/vl_setup')
```

where VLFEATROOT is the directory you installed vlfeat to, to get MATLAB to recognise VLFeat. To check that VLFeat is sucessfully installed,run `vl_version verbose`.

Generate your dataset using:

```python
import birdspy as bs
bs.ImageFactory.ground_truth_factory("mesa_distance/data/")
```

specifying the location you want to read in your data from (this is the default). You can then run the MATLAB script `mesa_distance/BirdCounting.m`. It may be necessaary to change the iteration limits and file paths there - the default option trains on the first 16 images and tests on the second 16.

This script generates the dense SIFT descriptors from a random weighted matrix, but it is preferred to pass a precomputed SIFT codebook for this dataset using VLFeat.

N.B The learning procedure calls methods from MATLAB's optimization toolbox which are very slow. These can be overloaded by faster solver through installlation of [MOSEK](www.mosek.com)- they are providing free academic licenses at the moment. Since MOSEK supercedes `linprog` and `quadprog` methods, no change in the code is required.

## Ridge Regression

Based on code from C. Arteta, V. Lempitsky, J. A. Noble, A. Zisserman , from [Interactive Object Counting](https://www.robots.ox.ac.uk/~vgg/publications/2014/Arteta14/).

Again VLFeat will need to be installed, following the options above. The pylon inference code will also require you to run `ridge_regression/PylonCode/pylonSetup.m` from the `PylonCode` directory before use.

You will then need to populate the `test` and `train` folders with your datasets, and annotations. These can be imported/generated automatically using the `birdspy` workflow, with the following command (replacing directory names with those on your local system):

```python
for sub_folder in ["HVITa2016a_renamed", "HVITa2016b_renamed"]:
    bs.DatasetFactory.generate_datasets(
        train_path=os.path.join("ridge_regression", "bird_data", "train"),
        test_path=os.path.join("ridge_regression", "bird_data", "test"),
        image_path=os.path.join("images", "HVITa_renamed", sub_folder),
        test_frac=8,
    )
```

where you can iterate over all directories you want to search for images in. Importing the data in this was will also allow automatic generation of the image database (IMDB).

The configuration of the learning algorithm is done in `getDataInfo.m`, and it consists of setting the relevant paths (e.g. paths to raw data, annotations, models, etc.), and the different training and testing parameters.

After a session of training is complete, the trained model is stored in the `output` (set in `getDataInfo.m`), and consists of two '.mat' files.
