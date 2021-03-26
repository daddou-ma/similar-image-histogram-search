#!/usr/bin/env python

import os
from image import Image
from csvhandler import CSVFile


# Get Images Histograms as list
data = map(Image.get_image_full_feature_vector, Image.get_all_images_in_folder('images')) 

# Save DataFrame to a csv file
CSVFile.save_to_csv(data, 'histograms.csv')
