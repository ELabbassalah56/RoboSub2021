import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
img = cv.imread('sudoku.png', cv.IMREAD_GRAYSCALE)
lap = cv.Laplacian(img, cv.CV_64F, ksize=1)    # kernal size is odd number
soblex = cv.Sobel(img, cv.CV_64F, 1, 0)  # third arg mention to order of derivative
sobley = cv.Sobel(img, cv.CV_64F, 0, 1)  # third arg mention to order of derivative

# here we will cast the output to uint8  to be suitable to output
lap = np.uint8(np.absolute(lap))
soblex = np.uint8(np.absolute(soblex))
sobley = np.uint8(np.absolute(sobley))
output = cv.bitwise_or(soblex, sobley)
# output = cv.bitwise_and(output, lap)
# output = cv.bitwise_not(output)
title = ['image', 'laplacian', 'soblex', 'sobley', 'output']
image = [img, lap, soblex, sobley, output]

for i in range(5):
    plt.subplot(2, 3, i+1), plt.imshow(image[i], 'gray')
    plt.title(title[i])
    plt.xticks([]), plt.yticks([])

plt.show()



"""
Image gradients can be used to extract information from images.
Gradient images are created from the original image 
(generally by convolving with a filter, one of the simplest being the Sobel filter=> is filter use to detect an edges )
for this purpose. 
Each pixel of a gradient image measures the change in intensity of that same point in the original image,
in a given direction.
To get the full range of direction,
gradient images in the x and y directions are computed
"""