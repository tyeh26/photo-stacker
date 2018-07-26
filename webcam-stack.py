import numpy as np
import cv2
import time
import queue

cap = cv2.VideoCapture(0)
queue = queue.Queue()

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    frame = np.float32(frame)/255


    queue.put(frame)

    array_of_frames = np.array(queue.queue)
    summed_frame = array_of_frames.sum(axis=0)
    averaged_frame = summed_frame/queue.qsize()*255
    # import pdb; pdb.set_trace()
    # display_frame = np.uint8(averaged_frame)
    display_frame = np.median(array_of_frames,0)

    # Display the resulting frame
    cv2.imshow('frame',display_frame)
    if queue.qsize() >= 15:
    	queue.get()
    print(queue.qsize())
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()