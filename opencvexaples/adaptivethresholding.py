# simple threshold vs adaptive threshold
import numpy as np
import cv2 as cv

"""
The color frequency image is an image where the pixel 
intensity represents the frequency of pixels in the original image that have
that same pixel color as that pixel location
"""
img = cv.imread('sudoku.png', 0)
# comparison is between origin img   and  127 and 225   127> pix is 0 else 255
# _, Th1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)
# adaptive threshold
Th2 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 2)
while True:
    cv.imshow('image', img)
    # cv.imshow('Th1', Th1)
    cv.imshow('Th2', Th2)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break


cv.waitKey(0)
cv.destroyAllWindows()
