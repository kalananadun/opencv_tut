# script python 
import cv2 as cv  #import the dependencies 

# resize and rescale the images 
# img = cv.imread("./images/image.png")
# cv.imshow("original image",img) # display the image
# Rescale the image 
# modifying the height and width of the image 

# function to modify the resolution of the image dpi level 
def changeResolution(width,height):
    # change resolution function only works with live videos 
    capture.set(3,width) # set the width of the image
    capture.set(4,height) # set the height of the image
    
#function to rescale the image 
def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1]*scale) # rescaling the width of the image 
    height =int(frame.shape[0]*scale) # rescaling the height of the image 
    dimensions = (width , height) # tuple to store the dimension of the image 
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA) # pass the resized image 


# resized_image = rescaleFrame(img) 
# cv.imshow("Scaled image",resized_image) 

# reading the video 
capture = cv.VideoCapture("./videos/video1.mp4")

while True:
    isTrue, frame = capture.read()
    frame_resized = rescaleFrame(frame)
    cv.imshow("original scene",frame)
    cv.imshow("Resized scene",frame_resized)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break


capture.release() # release the video capture object
cv.destroyAllWindows() # destroy all the windows