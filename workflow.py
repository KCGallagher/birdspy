#
# Example workflows for both models
#
import os

import birdspy as bs

# Model 1

# Save MATLAB ground-truth image files
# bs.ImageFactory.ground_truth_factory("counting_birds/data/")


# Model 2

# Generate training and testing datasets
for sub_folder in ["HVITa2016a_renamed", "HVITa2016b_renamed"]:
    bs.DatasetFactory.generate_datasets(
        train_path=os.path.join("Counting_MATLAB_package_birds", "bird_data", "train"),
        test_path=os.path.join("Counting_MATLAB_package_birds", "bird_data", "test"),
        image_path=os.path.join("images", "HVITa_renamed", sub_folder),
        test_frac=8,
    )

