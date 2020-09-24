import cv2
import numpy as np

img = cv2.imread("images/simpsons.jpg")
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
template = cv2.imread("images/barts_face.jpg", cv2.IMREAD_GRAYSCALE)
w, h = template.shape[::-1]

result = cv2.matchTemplate(gray_img, template, cv2.TM_CCOEFF_NORMED) # the algorithm will find this image in the main one
loc = np.where(result >= 0.4) # find the location of the white point

for pt in zip(*loc[::-1]): #using zip to unpack the points in the location variable
    cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 3)

cv2.imshow("img", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
