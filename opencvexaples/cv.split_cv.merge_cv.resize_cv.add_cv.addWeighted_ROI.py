import numpy as np
import cv2


def click_event(event, x_coord, y_coord, event_flag, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x_coord, ' , ', y_coord)
        cv2.putText(img, str(x_coord)+' , '+str(y_coord), (x_coord, y_coord), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 250, 250), 2,
                    cv2.LINE_AA)
        cv2.imshow('image', img)
    if event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img, (x_coord, y_coord), 5, (250, 0, 250), -1, cv2.LINE_AA)
        points.append((x_coord, y_coord))
        if len(points) >= 2:
            cv2.line(img, points[-1], points[-2], (0, 250, 250), 2, cv2.LINE_8)
            cv2.imshow('image', img)


img = cv2.imread('messi5.jpg', 1)
img2 = cv2.imread('transparent.png', 1)
# shape return cluster of rows columns  and channels
print(img.shape)
print(img2.shape)
# size Total number of pixels is accessed
print(img.size)
print(img2.size)
# dtype return Image  dataType
print(img.dtype)
print(img2.dtype)

"""
The co-ordinates used in the array follow the format of 
img [y1: y2, x1: x2]
Therefore, when copying to another part of the image, you need to ensure that (y2-y1) value remains the same, as well as (x2-x1)

Here's another example to copy messi's head, where Top left coordinates is (200, 60) and bottom right is (270, 140) in x,y format

messi_head = img[60:140, 200:270]
img[260:340,100:170] = messi_head
"""
points = []

b, g, r = cv2.split(img)
blue, green, red = cv2.split(img2)
img = cv2.merge((b, g, r))
img2 = cv2.merge((blue, green, red))

"""
ball = img[280:340, 330:390]
img[50:110, 120:180] = ball
"""
"""
here when we add to imags together should be have same size of matrix so  we use resize 
"""

img = cv2.resize(img, (512, 512))
img2 = cv2.resize(img2, (512, 512))

# dst = cv2.add(img2, img)
dst = cv2.addWeighted(img, .9, img2, .09, 10)
# ROI  region of interst  copy any shape in other region

cv2.imshow('image', dst)
cv2.setMouseCallback('image',click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()


