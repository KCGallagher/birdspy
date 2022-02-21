#
# Functions used for image analysis
# 

from __future__ import annotations
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

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
        self.annotations = []

    def print(self, use_annotations: bool = False, save_loc: str = "", my_dpi: int = 96):
        """Plots image object, with optional argument to save image. However,
        the separate save() methiod should be used for high quality images."""
        fig = plt.figure(figsize=(self.pixel_size[0] / my_dpi, 
                                  self.pixel_size[1] / my_dpi),
                         dpi=my_dpi)
        axs = fig.add_subplot()

        axs.imshow(self.data, interpolation='nearest')
        if use_annotations:
            self.plot_annotations(axs)

        axs.axes.xaxis.set_visible(False), axs.yaxis.set_visible(False)
        plt.axis('off')

        if save_loc != "":  # Not recommended - use save directly for better results
            plt.savefig(save_loc, dpi=my_dpi)
        plt.show()

    def save(self, save_loc: str = ""):
        """Alternative to printing the image that saves it directly, and
        retains resolution better on some computers"""
        im = Image.fromarray(self.data)
        im.save(save_loc)

    def get_annotations(self, use_citizens: bool = True):
        """Obtains pixel wise annotations from citizen science database,
        for a specified image. If use_citizens = False, will use gold standard 
        annotations from researcher instead (N.B these are not always avaliable)."""

        image = os.path.basename(self.file_loc)

        if use_citizens:
            file_path = "annotations/HVITa_citsciConsensus_kadult.csv"
        else:
            file_path = "annotations/HVITa_goldstandard_kadult.csv"

        df = pd.read_csv(file_path)
        df_img = df.loc[df["image_id"] == image]
        self.annotations += df_img[["cluster_x", "cluster_y"]].values.tolist()

    def plot_annotations(self, ax, rgb_value = np.array([1, 0, 0]), size = 6):
        for point in self.annotations:
            ax.plot(int(point[0]), int(point[1]), "o",
                    markersize  = size, color = rgb_value, )
