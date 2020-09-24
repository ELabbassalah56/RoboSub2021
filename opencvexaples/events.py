import numpy as np
import cv2
#events=[i for i in dir(cv2) if 'EVENT' in i ]
#print(events,end='\n')


def Click_event(event,x_coord,y_coord,event_Flag,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x_coord,' , ',y_coord)
        cv2.putText(img,str(x_coord)+' , '+ str(y_coord),(x_coord, y_coord),cv2.FONT_HERSHEY_COMPLEX,.5,(250,250,250),2,
                    cv2.LINE_AA)
        cv2.imshow('image',img)
    elif event== cv2.EVENT_RBUTTONDOWN:
        blue=img[x_coord, y_coord,0]
        green=img[x_coord, y_coord,1]
        red=img[x_coord, y_coord,2]
        cv2.putText(img, str(blue) + ' , ' + str(green)+' , '+str(red), (x_coord, y_coord), cv2.FONT_HERSHEY_COMPLEX,.5,
                    (250, 250, 0),1,cv2.LINE_AA)
        cv2.imshow('image', img)
        print()

# img = np.zeros((512,512,3),np.uint8)
img = cv2.imread('lena.jpg',1)
cv2.imshow('image',img)
cv2.setMouseCallback('image',Click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()