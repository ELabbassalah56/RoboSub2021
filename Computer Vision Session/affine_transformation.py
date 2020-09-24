import cv2
import numpy as np

img = cv2.imread('images/grid.jpg')
rows, cols, ch = img.shape # ch = channels

cv2.circle(img, (83, 90), 5, (0, 0, 255), -1)
cv2.circle(img, (447, 90), 5, (0, 0, 255), -1)
cv2.circle(img, (83, 472), 5, (0, 0, 255), -1)

pts1 = np.float32([[83, 90], [447, 90], [83, 472]])
pts2 = np.float32([[83, 90], [447, 90], [150, 472]]) # (150) for turning the image to right, but parallel with my points (declared before)

M = cv2.getAffineTransform(pts1, pts2)
output = cv2.warpAffine(img, M, (cols, rows))


cv2.imshow("Image", img)
cv2.imshow("WarpAffine", output)

cv2.waitKey(0)
cv2.destroyAllWindows()