import os
import numpy as np
import pandas as pd

class Distance:
    # Get All jpg files in images folder
    @staticmethod
    def calc_swim_distance(hist1, hist2):
        result = np.sum(np.minimum(hist1, hist2)) / np.sum(hist1)
        return result

    @staticmethod
    def calc_smith_distance(hist1, hist2):
        result = np.sum(np.minimum(hist1, hist2)) / np.minimum(np.sum(hist1), np.sum(hist2))
        return result

    # Open an Image
    @staticmethod
    def calc_jeffrey_distance(hist1, hist2):
        nh1 = np.array(hist1)
        nh2 = np.array(hist2)
        p1 = nh1 * np.log((2 * nh1) / (nh1 + nh2))
        p2 = nh2 * np.log((2 * nh2) / (nh1 + nh2))
        result = np.sum(p1 + p2)
        return result