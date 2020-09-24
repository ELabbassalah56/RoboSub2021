import cv2
img = cv2.imread("lena.jpg")
layer = img.copy()

gp = [layer]
for i in range(6):
    layer = cv2.pyrDown(layer)
    gp.append(layer)
    cv2.imshow(str(i), layer)
layer = gp[5]
cv2.imshow('upper level gaussian pyramid', layer)
lp = [layer]

for i in range(5, 0, -1):
    gaussian_extend = cv2.pyrUp(gp[i])
    laplacian = cv2.subtract(gp[i-1], gaussian_extend)
    cv2.imshow(str(i), laplacian)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()




"""
Ir1 = cv2.pyrDown(img)
Ir2 = cv2.pyrDown(Ir1)
Ir3 = cv2.pyrDown(Ir2)
hr1 = cv2.pyrUp(Ir3)
hr2 = cv2.pyrUp(hr1)
hr3 = cv2.pyrUp(hr2)

cv2.imshow('Ir1', Ir1)
cv2.imshow('Ir2', Ir2)
cv2.imshow('Ir3', Ir3)
cv2.imshow('hr1', hr1)
cv2.imshow('hr2', hr2)
cv2.imshow('hr3', hr3)
"""