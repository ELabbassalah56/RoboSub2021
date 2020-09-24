import numpy as np
import cv2

#img=cv2.imread('lena.jpg',-1)
#to draw line on img using line fun to line(imgage ,start coordinates, end coordinates ,BGR percentage ,thikness)
img=np.zeros([512,512,3],np.uint8)

cv2.line(img,(0,0),(25,20),(34.5,0,25),10)
cv2.arrowedLine(img,(255,255),(0,255),(34.5,50,71.52),10)
cv2.rectangle(img,(350,230),(215,255),(255,0,0),10)
cv2.circle(img,(447,63),25,(255,255,0),-1)
cv2.putText(img,'OpenCv',(10,350),cv2.FONT_ITALIC,4,(255,255,255),10,cv2.LINE_AA)

cv2.imshow('img',img)

cv2.waitKey(0)
cv2.destroyAllWindows()
