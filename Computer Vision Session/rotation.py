import cv2

img = cv2.imread("images/python.png")

img_rotate_90_clockwise = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

img_rotate_90_counterclockwise = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)

img_rotate_180 = cv2.rotate(img, cv2.ROTATE_180)



cv2.imshow('90 Clockwise',img_rotate_90_clockwise)
cv2.imshow('90 CounterClockwise',img_rotate_90_counterclockwise)
cv2.imshow('Rotate 180',img_rotate_180)

cv2.waitKey(0)
cv2.destroyAllWindows()
