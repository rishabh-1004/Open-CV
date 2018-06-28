import numpy as np
import cv2

img=cv2.imread('sample1.jpg',cv2.IMREAD_COLOR)
cv2.line(img,(0,0),(150,150),(255,255,255),15)
cv2.rectangle(img,(0,0),(250,250),(0,255,0),15)
cv2.circle(img,(100,100),55,(255,0,0),15)

pts= np.array([[10,5],[20,30],[70,20],[50,10]],np.int32)
cv2.polylines(img,[pts],True,(0,0,255),15)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'OpenCv Tuts..!',(0,130),font,1,(200,255,255),2,cv2.LINE_AA)

cv2.imshow('image',img)
cv2.waitKey()
cv2.destroyAllWindows()