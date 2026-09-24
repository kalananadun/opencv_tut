# script python 
import cv2 as cv  #import the dependencies 
#reading the images 
img = cv.imread("./images/madb.jpg")
cv.imshow("madb",img)
cv.waitKey(0)