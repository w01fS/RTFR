import cv2
import numpy as np
import time
import sys

faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
video_capture = cv2.VideoCapture(0)

while True:

    # Capture frame-by-frame
    retval, frame = video_capture.read()

    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect features specified in Haar Cascade
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.03,
        minNeighbors=5,
        
    )
    
    # Draw a rectangle around recognized faces 
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (50, 50, 200), 2)
        #Save the frame
        cv2.imwrite("frame.jpg", frame)

    # Display the resulting frame
    cv2.imshow('Video', frame)
    

    # Exit the camera view
    if cv2.waitKey(5) & 0xFF == ord('q'):
       cv2.destroyAllWindows()
       video_capture.release()
       sys.exit()
    else:
        time.sleep(2)
