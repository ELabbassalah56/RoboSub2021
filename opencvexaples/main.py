import cv2
img=cv2.imread('lena.jpg',1) #to read an img
print(img)
cv2.imshow('img',img) #to display an  img
k=cv2.waitKey(0) & 0xFF   #to wait display window   0xFF to masking all data 
if k==27:      #27 is the scii code of esc
  cv2.destroyAllWindows()   #to destroy all open window
elif k==ord('s'): #ord function to tack ascii code from user
  cv2.imwrite('lena_copy2jpg',img)   #to write an img
  cv2.destroyAllWindows()