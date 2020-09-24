import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


def nothing(x):
    pass


cap = cv.VideoCapture('vtest.avi')
cv.namedWindow('cap')
ret, frame1 = cap.read()
ret, frame2 = cap.read()

cv.createTrackbar('object', 'cap', 0, 2000, nothing)
while cap.isOpened():
    # to detect motion object
    # 1st we need to take a difference between frame1 and frame2
    diff = cv.absdiff(frame1, frame2)
    # 2nd convert this different to gray scale because it too easy to detect contour
    gray = cv.cvtColor(diff, cv.COLOR_BGR2GRAY)
    # 3rd blur gray to erase noise from alternative frames
    # using gaussian filter algorithm  because working on different weight
    blur = cv.GaussianBlur(gray, (5, 5), 0)
    # 4th we thresholding the blur frames to separating objects from background
    _, Thresh = cv.threshold(blur, 20, 255, cv.THRESH_BINARY)
    # 5th we dilate the threshold frames to fill all hols this help to find contours
    dilate = cv.dilate(Thresh, None, iterations=3)
    # 6th we need now to find contours
    contours, _ = cv.findContours(dilate, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
    # 7th we need to draw rectangle boundries around person so we need to
    # iterate in contours list
    state = cv.getTrackbarPos('object', 'cap')
    for contour in contours:
        # we need to define all coordinates (x_coord, y_coord, weight, height)
        (x_coord, y_coord, weight, height) = cv.boundingRect(contour)
        # now we need to find  area of the contour
        if cv.contourArea(contour) < state:
            continue
        cv.rectangle(frame1, (x_coord, y_coord), (x_coord+weight, y_coord+height), (0, 255, 0), 2, cv.LINE_AA, None)
        cv.putText(frame1, "status: {}".format('Movement'), (10, 20), cv.FONT_ITALIC, 1, (255, 255, 0)
                   , 3)
    # 7th now we need to draw contours we apply on frame1  because we want to apply contour ion original frame
    # cv.drawContours(frame1, contours, -1, (0, 0, 255), 3)
    cv.imshow('feed ', frame1)
    frame1 = frame2
    ret, frame2 = cap.read()
    if cv.waitKey(50) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()




