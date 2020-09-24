import cv2
#to read a data from camera or specific file mp4 or avi or device (-1/0) are indises for defualt camera
#if i have other cameras 1 for 1st  ,2 for 2nd  and so on
from numpy import half

cap=cv2.VideoCapture(0);
fourcc=cv2.VideoWriter_fourcc(*'XVID')   #fource code meaning the type to save that file
out= cv2.VideoWriter('vedio.avi',fourcc,20.0,(640,480))  #specis to read vedio and save it
# is opened that return true if file  opened  false otherwise
while (cap.isOpened()):
    ret ,frame = cap.read()  #create to variable ret for indecate that frame is there ,frame to recorded data enter
    if(ret == True):
      print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))  #to get higth and width of current videos
      print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
      out.write(frame)
      gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)    #cvt meaning convert to
      #make a vedio gray scale
      cv2.imshow('Frame',gray)
      #show my frame
      if cv2.waitKey(1) & 0xff == ord('q'): #wait until user enter a key
         break
    else:
        break
out.release()
cap.release()
cv2.destroyAllWindows()
