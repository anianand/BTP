import cv2
import numpy as np
img = cv2.imread('050.png')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #convert to grayscale
out=np.copy(gray) 	#copy of grayscale image 
cv2.equalizeHist(gray,out)	#histogram equalization
ret, thresh = cv2.threshold(out,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)  #Otsu's binarization
cv2.imshow('imge',thresh)
height,width=gray.shape
output=np.copy(img) #output copy
#substraction
#where we will get white in binarized image we will set white in output image 
for i in xrange(height):
	for j in xrange(width):
		if thresh[i][j]==255:
			output[i][j]=[255,255,255]
def white(l):
	if l[0]==255 and l[1]==255 and l[2]==255:
		return True
	else:
		return False
#mean filling
r,g,b=0,0,0
for i in xrange(height):
	for j in xrange(width):
		if white(output[i][j]):
			continue
		r+=output[i][j][0]
		g+=output[i][j][1]
		b+=output[i][j][2]
r=r/(height*width*1.0)
g=g/(height*width*1.0)
b=b/(height*width*1.0)
p=output[0][0]
p[0],p[1],p[2]=r,g,b
for i in xrange(height):
	for j in xrange(width):
		if white(output[i][j]):
			output[i][j]=p
#applying the binarisation and histogram equalisation again
img=np.copy(output)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #convert to grayscale
out=np.copy(gray) 	#copy of grayscale image 
cv2.equalizeHist(gray,out)	#histogram equalization
ret, thresh = cv2.threshold(out,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)  #Otsu's binarization
for i in xrange(height):
	for j in xrange(width):
		if thresh[i][j]==255:
			output[i][j]=[255,255,255]
#cv2.imwrite("051Filterd1.jpg",output)
cv2.imshow('image',output)
cv2.waitKey(0)
cv2.destroyAllWindows()
