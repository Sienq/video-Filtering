import cv2

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
            success,frame = video.read()
            if success:
                cv2.imshow(self._windowName,frame)

                if cv2.waitKey(25) & 0xFF == ord('q'):
                    break

            else:
                break

        video.release()
        cv2.destroyAllWindows()



    
    