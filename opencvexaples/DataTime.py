import cv2
import datetime
cap=cv2.VideoCapture(0);


while(cap.isOpened()):
    ret,frame = cap.read()
    if ret == True:
        cv2.putText(frame,'Width'+str(cv2.CAP_PROP_FRAME_WIDTH)+' '+'Higth'+str(cv2.CAP_PROP_FRAME_HEIGHT),(100,100)
                    ,cv2.FONT_HERSHEY_COMPLEX,1,(0,255,255),1,cv2.LINE_AA)
        cv2.putText(frame,str(datetime.datetime.now()),(10, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 255), 1, cv2.LINE_AA)
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0XFF == ord('q') :
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()