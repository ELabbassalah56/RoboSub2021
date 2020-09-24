import numpy as np
import cv2


# events=[i for i in dir(cv2) if 'EVENT' in i ]
# print(events,end='\n')


def click_event(event, x_coord, y_coord, event_flag, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        blue = img[x_coord, y_coord, 0]
        green = img[x_coord, y_coord, 1]
        red = img[x_coord, y_coord, 2]
        cv2.circle(img, (x_coord, y_coord), 3, (250, 0, 250), -1)
        my_color_img = np.zeros((512, 512, 3), np.uint8)
        my_color_img[:] = [blue, green, red]
        cv2.imshow('color', my_color_img)


# img = np.zeros((512, 512, 3), np.uint8)
img = cv2.imread('lena.jpg', 1)
cv2.imshow('image', img)
cv2.setMouseCallback('image', click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()

