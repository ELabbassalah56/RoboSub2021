import cv2

img = cv2.imread("images/python.png")

res = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)

cv2.imshow("Original", img)
cv2.imshow("res",res)

cv2.waitKey(0)
cv2.destroyAllWindows()