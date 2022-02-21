#
# Functions used for image analysis
# 

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

class BirdImage:
    """Image class for visualisation
    """
    def __init__(self, file_loc: str):
        """Creates an image object from a given file path (including the
        file name itself.
        """

        self.file_loc = file_loc
        self.image = Image.open(file_loc)
        self.data = np.array(self.image)

    def print(self):
        plt.imshow(self.data, interpolation='nearest')
        plt.show()

im = BirdImage("images/HVITa_zooniverse/HVITa2016a_zooniverse/HVITa2016a_000006.JPG")
print(im.file_loc)
print(im.data.shape)
im.print()