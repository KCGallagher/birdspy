#
# Functions to interface with the matlab code
#

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
from typing import List

class MatlabInterface:
    """Class to interface python methods with matlab
    """

    @staticmethod
    def ground_truth_conversion(save_loc: str):
        """Generates ground truth .mat lists per image from input csv. 
        """
        return