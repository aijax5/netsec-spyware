import time
import os
import cv2

class RecordVideo:
    def __init__(self,length = 20,fileName = "output.mp4"):
        self.length = length
        self.FILENAME = fileName
    
    def record(self,verbose = 0):
        cap = cv2.VideoCapture(0)
        frameCount = 0
        frameWidth = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        frameHeight = cap.get(cv2.CAP_PROP_FRAME_HEIGHT) 

        fourcc = cv2.VideoWriter_fourcc(*"mp4v")
        out = cv2.VideoWriter(self.FILENAME,fourcc, 20.0, (int(frameWidth),int(frameHeight)))

        t_end = time.time()+self.length       
        while(cap.isOpened() and time.time() < t_end ):
            ret, frame = cap.read()

            if ret == True:
                frame = cv2.flip(frame,1)
                out.write(frame)
                if(self.verbose == 2):
                    cv2.imshow('frame',frame)
            else:
                break
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

            frameCount += 1

        cap.release()
        out.release()
        cv2.destroyAllWindows()
