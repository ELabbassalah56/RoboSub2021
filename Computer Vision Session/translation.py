import cv2
import numpy as np
img = cv2.imread("images/python.png")
rows, cols, ch = img.shape

M = np.float32([[1, 0, 50], [0, 1, 10]])
output = cv2.warpAffine(img, M, (cols, rows))

cv2.imshow("Output", output)
cv2.imshow("Original", img)


cv2.waitKey(0)
cv2.destroyAllWindows()

