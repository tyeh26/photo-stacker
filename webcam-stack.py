import argparse
import numpy as np
import cv2
import sys
import time
import queue

ap = argparse.ArgumentParser()
ap.add_argument("-fps", "--fps", default=15,  type=int)
ap.add_argument("-wd", "--width", type=int)
ap.add_argument("-ht", "--height", type=int)
args = vars(ap)

queue = queue.Queue()

def stack_photos(args):
    fps = int(args.get('fps'))
    height = args.get('height')
    width = args.get('width')

    cap = cv2.VideoCapture(0)
    if height:
        cap.set(4, height)
    else:
        height = int(cap.get(4))
    if width:
        cap.set(3, width)
    else:
        width = int(cap.get(3))

    while(True):
        # Capture frame-by-frame
        start = time.time()
        ret, frame = cap.read()
        frame = np.float32(frame)/255
        frame = cv2.resize(frame, (width, height))

        queue.put(frame)

        array_of_frames = np.array(queue.queue)
        summed_frame = array_of_frames.sum(axis=0)
        averaged_frame = summed_frame/queue.qsize()*255
        # display_frame = np.uint8(averaged_frame)
        display_frame = np.median(array_of_frames,0)

        # Display the resulting frame
        cv2.imshow('frame',display_frame)
        process_time = time.time() - start
        if process_time > 1/fps and queue.qsize() > 2:
            queue.get()
            queue.get()
        print(queue.qsize())
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    args = vars(ap.parse_args())
    stack_photos(args)