import numpy as np
import cv2 as cv

# track bars are that useful for change value dynamically in run time
# creat a black image , a Window


def nothing(x):
        print(x)

# img = np.zeros((512,512,3),np.uint8)

cv.namedWindow('image')

cv.createTrackbar('cp', 'image', 10, 400, nothing)

switch = 'color/gray'
cv.createTrackbar(switch, 'image', 0, 1, nothing)


while True:
    img = cv.imread('lena.jpg')
    pos = cv.getTrackbarPos('cp', 'image')
    cv.putText(img, str(pos), (50, 150), cv.FONT_HERSHEY_SIMPLEX, 4, (255, 0, 255))

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

    s = cv.getTrackbarPos(switch, 'image')

    if s == 0:
       pass  # meaning that nothing happen

    else:
        img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    img = cv.imshow('image', img)

cv.destroyAllWindows()

