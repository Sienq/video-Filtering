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

        self.pause = tkinter.Button(self,text = "Pause/Play",width = 50) #! NOT WORKING YET
        self.pause.grid(row=1,column=1)


        self.delay = 1
        self.update()


    def snapshot(self): #! NOT WORKING YET
        if self.ret:
            cv2.imwrite('screenshot.png',cv2.cvtColor(self.frame,cv2.COLOR_RGB2BGR))

    def update(self):

        
        #! FILTERS APPLYING
        if not self.filtersGui.filterType == 'Normal':
            self.ret,self.frame = self.video.getFrame()
            self.frame = filters.ApplyFilter(self.filtersGui.filterType,frame = self.frame,ksize=(int(self.filtersGui.filterValue.get()),int(self.filtersGui.filterValue.get())))
        else:
            self.ret,self.frame = self.video.getFrame()

        #! DRAWING VIDEO FRAME
        if self.ret:
            self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(self.frame))
            self.canvas.create_image(0,0,image = self.photo,anchor=tkinter.NW)

        self.after(self.delay,self.update)  



win = App()
win.mainloop()



