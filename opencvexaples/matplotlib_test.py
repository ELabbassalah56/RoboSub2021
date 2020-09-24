import cv2
from matplotlib import pyplot as plt
img = cv2.imread('lena.jpg', -1)
cv2.imshow('image', img)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# plt.imshow(img)  # to show img

# plt.xticks([]), plt.yticks([])  # to set range of  x_Axis and Y_axis

# plt.show()  # to show img
# simple threshold vs adaptive threshold
import numpy as np
import cv2 as cv

"""
The color frequency image is an image where the pixel 
intensity represents the frequency of pixels in the original image that have
that same pixel color as that pixel location
"""
img = cv.imread('messi5.jpg', 1)
# comparison is between origin img   and  127 and 225   127> pix is 0 else 255
_, Th1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)
# INV is the inverse of binary which comp. between 127 > pix is 255 else 0
_, Th2 = cv.threshold(img, 127, 255, cv.THRESH_BINARY_INV)
# Trunc is compare that which after pixel 127> pix is equal no change else remain 127
_, Th3 = cv.threshold(img, 127, 255, cv.THRESH_TRUNC)
# TOZERO => 127>pix equal to  zero else no change
_, Th4 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO)
# TOZEROINV => 127>pix equal to  nochange else zero
_, Th5 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO_INV)
images = [img, Th1, Th2, Th3, Th4, Th5]
titles = ['Original image', 'th1', 'Th2', 'Th3', 'Th4', 'Th5' ]

for i in range(6):
    plt.subplot(2, 3, i+1), plt.imshow(images[i])
    plt.title(titles[i])

plt.show()

