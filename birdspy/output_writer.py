#
# Generates output .csv files from 
#

import os
import numpy as np
import pandas as pd
import scipy.io
from typing import Dict

from birdspy.image_factory import ImageFactory


class OutputWriter:
    """Factory to generate ground truth images from a given annotation dataset.

    Currently only stores the number of birds per image, but also be possible
    to isolate bird locations from regions of maximal density - needs discussion
    on the thresholds to set here.
    """

    @staticmethod
    def write_csv(input_loc: str, save_loc: str):
        """Writes csv data from output files
        """
        write_dict = {'image_id': [], 'workflow_name': [],
                      'birdnum': [], 'colonyname': [],
                      'datetime': [], 'celsius': []}
        annotation_df = ImageFactory.annotation_data()

        directory = os.fsencode(input_loc)
    
    
        for file in os.listdir(directory):
            filename = os.fsdecode(file)
            if filename.endswith(".mat"):
                OutputWriter.write_line(os.path.join(input_loc, filename), write_dict, annotation_df)

        write_df = pd.DataFrame(write_dict, index = write_dict['image_id'], columns=list(write_dict.keys())[1:])
        write_df.index.name = "image_id"
        write_df.to_csv(save_loc)

    @staticmethod
    def write_line(filename: str, write_dict: Dict, annotation_df: pd.DataFrame):
        print("Line name" + str(filename))
        image_code = os.path.splitext(os.path.basename(filename))[0]
        image_id = (image_code) + '.JPG'

        bird_num = OutputWriter.bird_count(filename)
        write_dict['birdnum'].append(bird_num)
        write_dict['image_id'].append(image_id)
        write_dict['workflow_name'].append("birdspy_tool")

        line = annotation_df.loc[annotation_df["image_id"] == image_id]
        line = line.drop_duplicates(subset='image_id', keep="last")
        for variable in ['colonyname','datetime','celsius']:
            write_dict[variable].append(line[variable].values[0])

    @staticmethod
    def bird_count(input_loc: str):
        mat = scipy.io.loadmat(input_loc)
        return int(np.sum(mat['orgDensityEst']))
