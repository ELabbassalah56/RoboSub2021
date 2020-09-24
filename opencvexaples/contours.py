import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('opencv.png', 1)
img = cv.resize(img, (512, 512))
imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
ret, TH = cv.threshold(imgGray, 127, 255, cv.THRESH_BINARY)
contours, hierarchy = cv.findContours(TH, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
# contours  is the python list of all contours in image.Each individual contour is a numpy array of (x, y)
# coordinates of boundary points  of the object
print("number of contours "+str(len(contours)))
print(contours[0])
cv.drawContours(img, contours, -1, (0, 255, 255), 5)
cv.imshow('Image', img)
cv.imshow('Image Gray', imgGray)
cv.waitKey(0)
cv.destroyAllWindows()
