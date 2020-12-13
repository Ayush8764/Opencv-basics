import numpy as np
import cv2

a = np.ones([300,300,3],dtype='uint8')*255
print(a)

a[0:100,0:300] = [0,0,255]
a[101:200,0:300] = [0,255,0]
a[201:300,0:300] = [255,0,0]
# Opencv works in BGR format and not in RGB format

cv2.imshow('White Background',a)
cv2.waitKey(0)   
cv2.destroyAllWindows()
