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
        self.cit_annotations = []
        self.gold_annotations = []

    def print(self, citizen_annotations: bool = False, gold_annotations: bool = False, 
              save_loc: str = "", my_dpi: int = 96):
        """Plots image object, with optional argument to save image. However,
        the separate save() methiod should be used for high quality images."""
        fig = plt.figure(figsize=(self.pixel_size[0] / my_dpi, 
                                  self.pixel_size[1] / my_dpi),
                         dpi=my_dpi)
        axs = fig.add_subplot()

        axs.imshow(self.data, interpolation='nearest')
        if citizen_annotations:
            self.plot_annotations(axs, self.cit_annotations, label = "Citizen Annotation")

        if gold_annotations:
            self.plot_annotations(axs, self.gold_annotations, 
            rgb_value = np.array([0, 0, 0.6]), marker = 'P',
            label = "Expert Annotation")

        axs.axes.xaxis.set_visible(False), axs.yaxis.set_visible(False)
        plt.axis('off')
        plt.legend(bbox_to_anchor=(0.15, 0.95))

        if save_loc != "":  # Not recommended - use save directly for better results
            plt.savefig(save_loc, dpi=my_dpi)
        plt.show()

    def save(self, save_loc: str = ""):
        """Alternative to printing the image that saves it directly, and
        retains resolution better on some computers"""
        im = Image.fromarray(self.data)
        im.save(save_loc)

    def get_annotations(self):
        """Obtains pixel wise annotations from citizen science database,
        for a specified image. If use_citizens = False, will use gold standard 
        annotations from researcher instead (N.B these are not always avaliable)."""

        image = os.path.basename(self.file_loc)

        df_cit = pd.read_csv("annotations/HVITa_citsciConsensus_kadult.csv")
        df_img_cit = df_cit.loc[df_cit["image_id"] == image]
        self.cit_annotations += df_img_cit[["cluster_x", "cluster_y"]].values.tolist()
        
        df_gold = pd.read_csv("annotations/HVITa_goldstandard_kadult.csv")
        df_img_gold = df_gold.loc[df_gold["image_id"] == image]
        self.gold_annotations += df_img_gold[["cluster_x", "cluster_y"]].values.tolist()


    def plot_annotations(self, ax, annotations, rgb_value = np.array([0.8, 0, 0]),
                         size = 6, marker = "o", label = "_nolegend_"):
        for i, point in enumerate(annotations):
            ax.plot(int(point[0]), int(point[1]), marker,
                    markersize = size, color = rgb_value, lw=60,
                    label = label if i == 0 else "_nolegend_")

class DensityPlot(BirdImage):
    """ Specifically returns contrasted density plots from MATLAB outputs"""

    def save(self, save_loc: str = ""):
        """Saves a higher contrast version of the image"""
        scaled_data = self.data * int(np.floor((255 / np.amax(self.data))))
        im = Image.fromarray(scaled_data)
        im.save(save_loc)

