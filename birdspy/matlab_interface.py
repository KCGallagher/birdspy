#
# Functions to interface with the matlab code
#

import os
import numpy as np
import pandas as pd
import scipy.io
from typing import List

import birdspy as bs


class MatlabInterface:
    """Class to interface python methods with matlab
    """

    @staticmethod
    def ground_truth_conversion(save_loc: str):
        """Generates ground truth .mat lists per image from input csv. 

        The training of the method is based on dot-annotations provided manually, 
        which are stored in '.mat' files, one per image, and with the same name 
        as its correspondent image. This '.mat' file should be a Nx2 matrix, with 
        (:,1) being the X coordinates and (:,2) the Y coordinates of the annotation dots.
        """
        annotation_df = bs.ImageFactory.annotation_data(use_citizens=True)
        images_ids = np.unique(annotation_df["image_id"])

        for image in images_ids:
            MatlabInterface.save_truth_mat(image, annotation_df, save_loc)

    @staticmethod
    def save_truth_mat(
        image_id: str, annotation_df: pd.DataFrame, save_loc: str, save_empty_file=True
    ):
        """Save truth matrix from image_id, and dataframe of all annotations
        
        In the form of a Nx2 matrix, with (:,1) being the X coordinates 
        and (:,2) the Y coordinates of the annotation dots.

        Option to save empty file if no annotations are present, or return nothing.
        """
        df_img = annotation_df.loc[annotation_df["image_id"] == image_id]
        annotations = df_img[["cluster_x", "cluster_y"]].values
        if np.isnan(annotations).any():
            if save_empty_file:
                print(f"Nan value in image {image_id}, saving empty matrix")
                annotations = []
            else:
                return False

        save_name = str(image_id.split(".")[0]) + ".mat"
        save_path = os.path.join(save_loc, save_name)
        scipy.io.savemat(save_path, {"values": annotations})
        return True
