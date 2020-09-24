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
while True:
    cv.imshow('image', img)
    cv.imshow('Th1', Th1)
    cv.imshow('Th2', Th2)
    cv.imshow('Th3', Th3)
    cv.imshow('Th4', Th4)
    cv.imshow('Th5', Th5)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break


cv.waitKey(0)
cv.destroyAllWindows()
