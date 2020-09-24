import cv2
import numpy as np

img = cv2.imread("images/opencv_logo.png")
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgGray, 127, 255, 0) # 0 means no type
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
# Contours is a python list of all the Contours in the image
# hierarchy is an optional output, which is contained info about image topology
print("Number of Contours "+str(len(contours)))

# Drawing Contours
cv2.drawContours(img, contours, -1, (0, 255, 0), 3)
# -1 is Contour index, which will draw all the contours in the image


cv2.imshow("Original", img)
cv2.imshow("GrayScaled", imgGray)
cv2.waitKey(0)
cv2.destroyAllWindows()