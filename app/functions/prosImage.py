import cv2
import numpy as np


def cannyImage(img_array):
    img = cv2.Canny(img_array, 100, 200)
    return img

def calcRGB(img_array):
    average_color_per_row = np.average(img_array, axis=0)
    average_color = np.average(average_color_per_row, axis=0)
    return average_color
