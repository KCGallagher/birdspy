#
# Example workflows for both models
#

import os

import birdspy as bs

# MESA Distance

# Save MATLAB ground-truth image files
# bs.ImageFactory.ground_truth_factory("mesa_distance/data/")


# Ridge Regression

# Generate training and testing datasets
for sub_folder in [
    "HVITa2016a_renamed",
    "HVITa2016b_renamed",
    "HVITa2016c_renamed",
    "HVITa2016d_renamed",
]:
    bs.DatasetFactory.generate_datasets(
        train_path=os.path.join("ridge_regression", "bird_data", "train"),
        test_path=os.path.join("ridge_regression", "bird_data", "test"),
        image_path=os.path.join("images", "HVITa_renamed", sub_folder),
        test_frac=8,
    )
