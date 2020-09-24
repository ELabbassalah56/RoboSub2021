import cv2
import numpy as np

img = cv2.imread("images/cards.jpg")
w, h = 450, 300 # w = Width, h = Height
# make 4 points of the images in MATRIX using NUMPY
pts1 = np.float32([[326, 116], [214, 335], [479, 196], [369, 413]])
pts2 = np.float32([[0, 0], [w, 0], [0, h], [w, h]]) # for the new card
M = cv2.getPerspectiveTransform(pts1,pts2) # Matrix
output = cv2.warpPerspective(img, M, (w, h))
# for plotting the points on the image (for testing)
for x in range(0, 4):
    cv2.circle(img, (pts1[x][0], pts1[x][1]), 5, (0, 255, 0), cv2.FILLED)  # plotting X and Y values

cv2.imshow("Original", img)
cv2.imshow("Warped", output)
cv2.waitKey(0)
cv2.destroyAllWindows()
