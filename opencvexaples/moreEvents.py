import numpy as np
import cv2
#events=[i for i in dir(cv2) if 'EVENT' in i ]
#print(events,end='\n')


def Click_event(event,x_coord,y_coord,event_Flag,param):
    if event == cv2.EVENT_LBUTTONDOWN:
      cv2.circle(img,(x_coord , y_coord),5 ,(250,0,250) ,-1,cv2.LINE_AA)
      points.append((x_coord , y_coord))
      if len(points)>=2 :
          cv2.line(img,points[-1],points[-2],(0,250,250),2,cv2.LINE_8)
      cv2.imshow('image',img)


img = np.zeros((512,512,3),np.uint8)
points=[]
#img=cv2.imread('lena.jpg',1)
cv2.imshow('image',img)
cv2.setMouseCallback('image',Click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()