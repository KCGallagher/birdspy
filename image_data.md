# Image Data

I am very grateful to the [SeabirdWatch](https://ornithology.ucc.ie/current-projects/seabirdwatch/) project, who have ownership of all data used in this project, and have kindly let me use it. As such I have no ownship over this data, nor any right to publish/share it. Instead, I provide a log here of the data used in this project.

## Introduction

All images in the dataset were taken from a single camera, located on Hvitabjarnarey Island in Iceland ([colony code](https://www.zooniverse.org/projects/penguintom79/seabirdwatch/talk/1165/799728) 'HVITa'). The images depict a relatively small colony, with approximately 30 nests per photo.

## Images

The full set of original images was provided, each with an approximate size of 500kb per (1920 x 1080) image. These images were compressed for upload to the citizen science programme [Zooniverse]((https://www.zooniverse.org/projects/penguintom79/seabirdwatch)), to an approximate size of 100kb per (1000 x 562) image. As all annotations have been completed on this dataset, I will train and test on this dataset.

The dataset used is a combination of data collected in 2016 and 2018, randomly separated into testing and training datasets.

## Annotations

I use collated annotation data from the citizen science platform, and obtained following the methods used in [Jones et al. 2018](https://doi.org/10.1038/sdata.2018.124). In summary, at least ten users will classify every image, whose raw clicks are combined to give one ‘consensus’ click per bird, in the form of x and y pixel values in the originial size image. The number of raw clicks that each consensus click is formed from is recorded for each image, but currently I do not weight each data point according to this.
