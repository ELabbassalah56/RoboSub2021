import cv2 as cv
img = cv.imread('images (1).png')
img = cv.resize(img, (512, 512))
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
_, thresh = cv.threshold(img_gray, 240, 255, cv.THRESH_BINARY)
contours, _ = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)

for contour in contours:
    approx = cv.approxPolyDP(contour, 0.01*cv.arcLength(contour, True), True)
    cv.drawContours(img, [approx], 0, (0, 0, 0), 5)
    x_approx = approx.ravel()[0]
    y_approx = approx.ravel()[1] - 5
    if len(approx) == 3:
        cv.putText(img, "Triangle", (x_approx, y_approx), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))
    elif len(approx) == 4:
        x1, y1, w, h = cv.boundingRect(approx)
        aspectRatio = float(w)/h
        if (aspectRatio >= 0.95) and (aspectRatio <= 1.05):
            cv.putText(img, "square", (x_approx, y_approx), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))
        else:
            cv.putText(img, "rectangle", (x_approx, y_approx), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))
    elif len(approx) == 5:
        cv.putText(img, "pentagon", (x_approx, y_approx), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))
    elif len(approx) == 6:
        cv.putText(img, "hexagon", (x_approx, y_approx), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))
    else:
        cv.putText(img, "Circle", (x_approx, y_approx), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))

cv.imshow('shape', img)
cv.waitKey(0)
cv.destroyAllWindows()
