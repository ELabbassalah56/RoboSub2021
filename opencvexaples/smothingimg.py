import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('lena.jpg')

img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
# img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

kernel = np.ones((5, 5), np.float32)/25.00   ##  K = 1/(Kwidth * Kheight) * matrix((5*5)=1)
dst = cv.filter2D(img, -1, kernel)
blur = cv.blur(img, (5, 5))
gblur = cv.GaussianBlur(img, (5, 5), 0)
median = cv.medianBlur(img, 5, None)    # kernal size should be odd number except 1
bilateral = cv.bilateralFilter(img, 9, 75, 75)
# second arg d is the diameter of nighbore pixles
"""
img2 = cv.cvtColor(gblur, cv.COLOR_RGB2GRAY)
Th1 = cv.adaptiveThreshold(img2, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 2)
ker = np.ones((4, 4), np.uint8)
closing = cv.morphologyEx(Th1, cv.MORPH_CLOSE, ker, iterations=1)
"""
title = ['image', '2D Convolution', 'blur', 'gblur', 'median', 'bilateral']

image = [img, dst, blur, gblur, median, bilateral]


for i in range(6):
    plt.subplot(3, 3, i+1), plt.imshow(image[i], 'gray')
    plt.title(title[i])
    plt.xticks([]), plt.yticks([])

plt.show()

















"""
image kernel is a small matrix used to 
apply effects like the ones you might find in Photoshop or Gimp, such as blurring,
sharpening, outlining or embossing. They're also used in machine learning for 'feature extraction',
a technique for determining the most important portions of an image.
************************************************************
====>>>>>>>
Convolution pseudo code in python 
for each image row in input image:
   for each pixel in image row:

      set accumulator to zero

      for each kernel row in kernel:
         for each element in kernel row:

            if element position  corresponding* to pixel position then
               multiply element value  corresponding* to pixel value
               add result to accumulator
            endif

      set output image pixel to accumulator
==========>
"""