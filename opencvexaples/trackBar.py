import numpy as np
import cv2 as cv

# track bars are that useful for change value dynamically in run time
# creat a black image , a Window


def nothing(x):
        print(x)


img = np.zeros((512,512,3),np.uint8)
cv.namedWindow('image')
cv.createTrackbar('blue', 'image', 0, 255, nothing)
cv.createTrackbar('red', 'image', 0, 255, nothing)
cv.createTrackbar('green', 'image', 0, 255, nothing)

switch = '1:OFF\n0:ON'
cv.createTrackbar('Switch', 'image', 0, 1,nothing)


while True:
    cv.imshow('image', img)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
    b = cv.getTrackbarPos('blue', 'image')
    g = cv.getTrackbarPos('green', 'image')
    r = cv.getTrackbarPos('red', 'image')
    s = cv.getTrackbarPos('Switch', 'image')

    if s == 0:
       img[:] = [(b, g, r)]

    elif s == 1:
       img[:] = 0

cv.destroyAllWindows()

