import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt


img = cv.imread('colorballs.jpg', cv.IMREAD_GRAYSCALE)
_, mask = cv.threshold(img, 220, 250, cv.THRESH_BINARY_INV)
ker = np.ones((3, 3), np.uint8)

dilation = cv.dilate(mask, ker, iterations=3)
ers = cv.erode(mask, ker, iterations=1)
opening = cv.morphologyEx(mask, cv.MORPH_OPEN, ker, iterations=1)   #  erision => dilation
closing = cv.morphologyEx(mask, cv.MORPH_CLOSE, ker, iterations=1)  #  dilation => erision

## there is more teqnices

images = [img, mask, dilation, ers, opening, closing]
titles = ['Original image', 'mask', 'dilation', 'ersion', 'opening', 'closing']

for i in range(6):
    plt.subplot(3, 2, i+1), plt.imshow(images[i], 'gray'),
    plt.title(titles[i])


plt.show()