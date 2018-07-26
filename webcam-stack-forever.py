import numpy as np
import cv2
import time

cap = cv2.VideoCapture(0)
ret, frame = cap.read()
average_stack = np.float32(np.copy(frame))/255
frames = 1.0

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    frame = np.float32(frame)/255

    average_stack = average_stack * frames + frame
    frames += 1.0
    average_stack = average_stack/frames

    # Display the resulting frame
    cv2.imshow('frame',np.uint8(average_stack*255))
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()