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

    def print(self, save_loc = ""):
        """Plots image object, with optional argument to save image"""
        plt.imshow(self.data, interpolation='nearest')
        axs = plt.gca()
        axs.axes.xaxis.set_visible(False), axs.yaxis.set_visible(False)
        plt.axis('off')
        if save_loc != "":
            plt.savefig(save_loc)
        plt.show()

