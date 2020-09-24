import cv2 as cv
import numpy as np

apple = cv.imread('apple.jpg', 1)
orange = cv.imread('orange.jpg', 1)
apple_orange = np.hstack((apple[:, :256], orange[:, 256:]))
print(apple.shape)
print(orange.shape)

# generate gaussian pyramid for apple
apple_cp = apple.copy()
gp_apple = [apple_cp]
for i in range(6):
    apple_cp = cv.pyrDown(apple_cp)
    gp_apple.append(apple_cp)

# generate gaussian pyramid for orange
orange_cp = orange.copy()
gp_orange = [orange_cp]
for i in range(6):
    orange_cp = cv.pyrDown(orange_cp)
    gp_orange.append(orange_cp)


# generate  laplaccian pyramid for apple
apple_cp = gp_apple[5]
la_apple = [apple_cp]
for i in range(5, 0, -1):
    gaussian_apple_extend = cv.pyrUp(gp_apple[i])
    laplacian_apple = cv.subtract(gp_apple[i-1], gaussian_apple_extend)
    la_apple.append(laplacian_apple)

# generate  laplaccian pyramid for apple
orange_cp = gp_orange[5]
la_orange = [orange_cp]
for i in range(5, 0, -1):
    gaussian_orange_extend = cv.pyrUp(gp_orange[i])
    laplacian_orange = cv.subtract(gp_orange[i-1], gaussian_orange_extend)
    la_orange.append(laplacian_orange)

# now add  left and right halves of images in each other
apple_orange_pyramid = []
count = 0
for apple_lap, orange_lap in zip(la_apple, la_orange):
    count += 1
    cols, rows, ch = apple_lap.shape
    laplacian = np.hstack((apple_lap[:, :int(cols/2)], orange_lap[:, int(cols/2):]))
    apple_orange_pyramid.append(laplacian)

# now we reconstruct
apple_orange_reconstruct = apple_orange_pyramid[0]
for i in range(1, 6):
    apple_orange_reconstruct = cv.pyrUp(apple_orange_reconstruct)
    apple_orange_reconstruct = cv.add(apple_orange_pyramid[i], apple_orange_reconstruct)


cv.imshow('apple', apple)
cv.imshow('orange', orange)
cv.imshow('apple_orange', apple_orange)
cv.imshow('apple_orange_cons', apple_orange_reconstruct)
cv.waitKey(0)
cv.destroyAllWindows()