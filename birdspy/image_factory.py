#
# Generates ground truth images from annotation csv files
#

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
from typing import List


class ImageFactory:
    """Factory to generate ground truth images from a given annotation dataset
    """

    @staticmethod
    def ground_truth_factory(save_loc: str):
        """Generates ground truth images from input csv. Select images from 2016 only as they are a uniform size
        """
        annotation_df = ImageFactory.annotation_data(use_citizens=True)
        annotation_df = annotation_df.loc[
            annotation_df["cam_id"].str.startswith("HVITa2016")
        ]
        images_ids = np.unique(annotation_df["image_id"])

        for image in images_ids:
            ImageFactory.save_truth_image(image, annotation_df, save_loc)

    @staticmethod
    def save_truth_image(image_id: str, annotation_df: pd.DataFrame, save_loc: str):
        """Save truth image from image_id, and dataframe of all annotations"""
        df_img = annotation_df.loc[annotation_df["image_id"] == image_id]
        annotations = df_img[["cluster_x", "cluster_y"]].values.tolist()

        img_array = ImageFactory.write_truth_image(annotations)
        img = Image.fromarray(img_array)
        save_name = str(image_id.split(".")[0]) + "_truth.jpg"
        save_path = os.path.join(save_loc, save_name)
        img.save(save_path)

    @staticmethod
    def write_truth_image(annotations: List):
        """Generate array from truth image from list of annotation points"""
        img_shape = (1080, 1920, 3)  # All images in uncompressed datasize are this size
        img = np.zeros(img_shape, dtype=np.uint8)
        if np.isnan(annotations).any():
            return img  # No birds in image
        for point in annotations:
            img[int(point[1])][int(point[0])] = np.array([255, 0, 0])
        return img

    @staticmethod
    def annotation_data(use_citizens: bool = True):
        """Generate dataframe of annotation data"""
        if use_citizens:
            annotation_path = "annotations/HVITa_citsciConsensus_kadult.csv"
        else:
            annotation_path = "annotations/HVITa_goldstandard_kadult.csv"
        return pd.read_csv(annotation_path)


ImageFactory.ground_truth_factory("counting_birds/data/")
