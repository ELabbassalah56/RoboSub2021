import numpy as np
import cv2
"""
A color space is a specific organization of colors.
In combination with color profiling supported by various physical devices
"""


def nothing(x):
    pass


cap = cv2.VideoCapture(0)

cv2.namedWindow("Tracking")
cv2.createTrackbar('LH', "Tracking", 0, 255, nothing)
cv2.createTrackbar('LS', "Tracking", 0, 255, nothing)
cv2.createTrackbar('LV', "Tracking", 0, 255, nothing)
cv2.createTrackbar('UH', "Tracking", 255, 255, nothing)
cv2.createTrackbar('US', "Tracking", 255, 255, nothing)
cv2.createTrackbar('UV', "Tracking", 255, 255, nothing)

cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 150)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 150)

switch = "color/gray"
cv2.createTrackbar(switch, "Tracking", 0, 1, nothing)

while cap.isOpened():
    # frame = cv2.imread('colorballs.jpg', 1)
    _, frame = cap.read()
    # frame = cv2.resize(frame, (512, 512))

    # here  we want to convert colored img  to hsv
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # now we need to now the range of blue color  ##  threshold = is amount or level or scale or limit
    """
    to determine the threshold  of  specific color we need two array to determine 
    lower and upper threshold 
    """
    l_h = cv2.getTrackbarPos('LH', "Tracking")
    l_s = cv2.getTrackbarPos('LS', "Tracking")
    l_v = cv2.getTrackbarPos('LV', "Tracking")
    U_h = cv2.getTrackbarPos('UH', "Tracking")
    U_s = cv2.getTrackbarPos('US', "Tracking")
    U_v = cv2.getTrackbarPos('UV', "Tracking")
    l_b = np.array([l_h, l_s, l_v])
    u_b = np.array([U_h, U_s, U_v])

    # here we need to create instance from the range we are determine it so
    mask = cv2.inRange(hsv, l_b, u_b)
    res = cv2.bitwise_and(frame, frame, mask=mask)

    # slicing for color
    # i_mask = mask > 0
    # blue = np.zeros_like(frame, np.uint8)
    # blue[i_mask] = frame[i_mask]
    # cv2.imshow("blue", blue)
    s = cv2.getTrackbarPos(switch, "Tracking")
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    if s == 1:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    else:
        nothing(0)

    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)
    cv2.imshow("res", res)

cap.release()
cv2.destroyAllWindows()
