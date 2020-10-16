import tkinter
import cv2

class MyVideoCapture:
    def __init__(self,videoDestination):
        self.video = cv2.VideoCapture(videoDestination)

        if not self.video.isOpened():
            raise ValueError("Unable to display video",videoDestination)
        
        success,frame = self.video.read()
        
        self.height = frame.shape[0]
        self.width = frame.shape[1]

    def __del__(self):
        if self.video.isOpened():
            self.video.release()

    def getFrame(self):

        if self.video.isOpened():
            success,frame = self.video.read()
            if success:
                return (success,cv2.cvtColor(frame,cv2.COLOR_BGR2RGB))
            else:
                return (success,None)
        else:
            return (success,None)
    


    

