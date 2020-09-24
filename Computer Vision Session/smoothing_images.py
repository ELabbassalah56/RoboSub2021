import cv2

img = cv2.imread("images/carpet.jpg")

averaging = cv2.blur(img, (5, 5))
gaussian = cv2.GaussianBlur(img, (5, 5), 0) # the extra value (0) : it's sigmaX (more advanced)
median = cv2.medianBlur(img, 5) # it needs an integer like 5 not (5, 5)
# Median Filter functions well in noisy images
bilateral = cv2.bilateralFilter(img, 5, 75, 75) # used for smoothening images and reducing noise, while preserving edges

cv2.imshow("Original", img)
cv2.imshow("Averaging", averaging)
cv2.imshow("Gaussian", gaussian)
cv2.imshow("Median", median)
cv2.imshow("Bilateral", bilateral)

cv2.waitKey(0)
cv2.destroyAllWindows()