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
        self.pixel_size = (self.data.shape[1], self.data.shape[0])

    def print(self, save_loc = "", my_dpi = 96):
        """Plots image object, with optional argument to save image"""
        fig = plt.figure(figsize=(self.pixel_size[0] / my_dpi, 
                                  self.pixel_size[1] / my_dpi),
                         dpi=my_dpi)
        axs = fig.add_subplot()

        axs.imshow(self.data, interpolation='nearest')
        axs.axes.xaxis.set_visible(False), axs.yaxis.set_visible(False)
        plt.axis('off')

        if save_loc != "":
            plt.savefig(save_loc, dpi=my_dpi)
        plt.show()
