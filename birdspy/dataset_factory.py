#
# Generates training and test datasets from image data and annotations
#

import os
import shutil
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
from typing import List

import birdspy as bs


class DatasetFactory:
    """Factory to generate ground truth images from a given annotation dataset
    """

    @staticmethod
    def generate_datasets(
        train_path: str, test_path: str, image_path: str, test_frac: int
    ):
        """Generates training and testing datasets at the specified locations, from a given 
        directory of images. Places 1 in n images into the testing dataset randomly.

        Also runs the following checks:
        * All images with invalid data are removed
        * All images with no annotations are optionally removed
        """
        annotation_df = bs.ImageFactory.annotation_data(use_citizens=True)
        images_ids = np.unique(annotation_df["image_id"])

        for image in images_ids:
            if not os.path.exists(os.path.join(image_path, image)):
                continue  # Skip to the nexct image

            if not DatasetFactory.check_image(image, annotation_df):
                continue

            copy_loc = test_path if (np.random.rand() < (1 / test_frac)) else train_path
            # Test (and save) ground truth if not empty
            if bs.MatlabInterface.save_truth_mat(
                image, annotation_df, copy_loc, save_empty_file=False
            ):
                # This will have saved ground druth .mat file if there are annotations
                # We will also save image data
                shutil.copy(os.path.join(image_path, image), copy_loc)

    @staticmethod
    def check_image(image_id, annotation_df):
        """Checks whether image is valid, and has annotations,returning validity boolean"""
        image_df = annotation_df.loc[annotation_df["image_id"] == image_id]
        if (
            len(image_df) <= 0
        ):  # Set minimum threshold for number of annotations required in image
            return False
        return True
