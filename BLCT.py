# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 14:23:49 2021

Balanced Contrast enhancement technique (blct function)

l => Minimum value of the input image
h => Maximum value of the input image
e => Mean value of the input image
L => Minimum value of the output image
H => Maximum value of the output image
E => Mean value of the output image assume to be 110 or any number
s => Mean square sum of the output image

Linear Contrast enhancement Algorithm (LCE)
F => Output Image
a => Contrast
b => Brightness
H => Histogram output

@author: AbhinavNarayan

"""

import cv2
import numpy as np

def blct(img):
    img = np.double(img)
    l = np.min(img)
    h = np.max(img)
    e = np.mean(img)
    s = np.mean(img**2)
    L = 0
    H = 255
    E = 145
    bnum = ((h**2) * (E-L)) + (s * (H-L)) + ((l**2) * (H-E))
    bden = 2 * ((h * (E - L)) - (e * (H - L)) + (l * (H - E)))
    b = bnum/bden
    anum = H - L
    aden = (h - l) * (h + l - (2*b))
    a = anum/aden
    
    c = L - (a * ((l - b)**2))
    y = (a * ((img[:,:] -b)**2)) + c
    y = np.uint8(y)
    return y


# def LCE(img):
#     a = 1
#     b = 5
#     F = (a * np.double(img[:,:])) + b
#     F = np.uint8(F)
#     H = cv2.equalizeHist(F)
#     return H

#Test BLCT and LCE

input_image = cv2.imread('C:/Users/Abhi/Downloads/1.jpg')
img_hsv = cv2.cvtColor(input_image,cv2.COLOR_BGR2HSV)

H,S,V = cv2.split(img_hsv)

o = blct(V)

m = cv2.merge([H,S,o])

img_bgr = cv2.cvtColor(m,cv2.COLOR_HSV2BGR)

cv2.imwrite('BLCT_output.png',img_bgr)
