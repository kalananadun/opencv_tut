# script python 
import cv2 as cv  #import the dependencies 

# loading the video to the script 

# capture = cv.VideoCapture(0) # 0 is for the default camera 
capture = cv.VideoCapture("./videos/video1.mp4") 

while True:
    isTrue, frame = capture.read() # read the video frame at a time 
    cv.imshow("video1",frame) # 

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release() 
cv.destroyAllWindows()

# cv.waitKey(0) # wait for the key to be pressed 
# -215 error is about video file ran out of frames or could not find the video file 