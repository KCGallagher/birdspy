#
# Example workflows for both models
#

import birdspy as bs

# Model 1

# Save MATLAB ground-truth image files
#bs.ImageFactory.ground_truth_factory("counting_birds/data/")


# Model 2

# Generate training and testing datasets
bs.DatasetFactory.generate_datasets(train_path="Counting_MATLAB_package_birds/bird_data/train",
                                 test_path="Counting_MATLAB_package_birds/bird_data/test",
                                 image_path="images/HVITa_renamed/HVITa2016a_renamed",
                                 test_frac=8)