#!/usr/bin/env python
#imports
import sys
import os
import cv2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from image import Image
from csvhandler import CSVFile
from distance import Distance
from tkinter import filedialog

database = CSVFile.load_from_csv('histograms.csv')

if len(sys.argv) >=2:
    filename = sys.argv[1]
else:
    filename = filedialog.askopenfilename() # sys.argv[0]

request_image = cv2.resize(Image.load_image(filename),(480, 360))
request_histogram = Image.get_image_histogram(filename)

def add_histogram_to_image(image, isMain, distance):
    fig, ax = plt.subplots(figsize=(5, 3))
    ax.plot(range(0, 8), Image.get_image_blue_histogram(image), color='b')
    ax.plot(range(0, 8), Image.get_image_green_histogram(image), color='g')
    ax.plot(range(0, 8), Image.get_image_red_histogram(image), color='r')

    fig.canvas.draw()

    # convert canvas to image
    hist = np.fromstring(fig.canvas.tostring_rgb(), dtype=np.uint8, sep='')
    hist  = hist.reshape(fig.canvas.get_width_height()[::-1] + (3,))
    hist  = cv2.resize(hist, (192, 144))
    # hist is rgb, convert to opencv's default bgr
    hist = cv2.cvtColor(hist,cv2.COLOR_RGB2BGR)
    image[360-144:360, 480-192:480] = hist
    image = cv2.putText(image, str(distance) if distance != 0 else 'Recherche', (24, 24), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)

    return image

request_image = add_histogram_to_image(request_image, True, 0)

rows = []
for index, row in database.iterrows():
    rows.append(Distance.calc_smith_distance(request_histogram, list(row[1:513])))

database['distance'] = rows
database = database.sort_values(by=['distance'], ascending=False)


similars = database.head(4)[1:4].apply(lambda row: {'img': cv2.resize(Image.load_image(row['0']),(480, 360)), 'distance': round(row['distance'], 2)}, axis=1)

similar1, similar2, similar3 = map(lambda item: add_histogram_to_image(item['img'], False, item['distance']), similars)

top = np.hstack((request_image, similar1))
bottom = np.hstack((similar2, similar3))
result = np.vstack((top, bottom))


cv2.imshow('similars', result)

#numpy_vertical = np.vstack((image, grey_3_channel))

cv2.waitKey()