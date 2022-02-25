# 
# Root of birdspy module
# 

"""birdspy is a python module for visualising and handling wildlife images
"""

from .image_analysis import BirdImage, DensityPlot
from .image_factory import ImageFactory
from .matlab_interface import MatlabInterface
from .dataset_factory import DatasetFactory
from .output_writer import OutputWriter