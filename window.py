import cv2
import filters
#Class for window handling

class Window():

    def __init__(self,name):
        self._windowName = name
        self._window = cv2.namedWindow(name,cv2.WINDOW_NORMAL)

    def displayVideo(self,videoName):
        self._videoName = videoName
        video = cv2.VideoCapture(self._videoName)

        if not video.isOpened():
            print("ERROR WHILE OPENING VIDEO")
            return
        
        while video.isOpened():
            success,self.myFrame = video.read()
            if success:
                self.myFrame = filters.customBlur((5,5),self.myFrame)
                cv2.imshow(self._windowName,self.myFrame)

                if cv2.waitKey(25) & 0xFF == ord('q'):
                    break

            else:
                break

        video.release()
        cv2.destroyAllWindows()


    
    