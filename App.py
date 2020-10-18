import tkinter
import cv2
import MyVideoCapture
import PIL.Image,PIL.ImageTk
import filters
import filtersGUI as fGUI

class App(tkinter.Tk):
    def __init__(self,videoSource = 0):
        super().__init__()

        self.videoSource = videoSource
        self.video = MyVideoCapture.MyVideoCapture(videoSource)


        #! VIDEO
        self.canvas = tkinter.Canvas(self,width = self.video.width,height = self.video.height)
        self.canvas.grid(row=0,column=1)
        #! FILTERS GUI
        self.filtersGui = fGUI.filtersGUI(self)
        self.filtersGui.grid(row=0,column=0)


        self.delay = 1
        self.update()


    def snapshot(self):
        if self.ret:
            cv2.imwrite('screenshot.png',cv2.cvtColor(self.frame,cv2.COLOR_RGB2BGR))


    def update(self):

        self.ret,self.frame = self.video.getFrame()
        
        if self.filtersGui.filterType == 'Normal':
            self.ret,self.frame = self.video.getFrame()

        if self.filtersGui.filterType == 'Edge Detection':
            self.frame = filters.customEdgeDetection((3,3),cv2.cvtColor(self.frame,cv2.COLOR_RGB2BGR))

        if self.ret:
            self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(self.frame))
            self.canvas.create_image(0,0,image = self.photo,anchor=tkinter.NW)

        self.after(self.delay,self.update)



win = App()
win.mainloop()



