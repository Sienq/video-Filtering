import tkinter
import cv2
import MyVideoCapture
import PIL.Image,PIL.ImageTk
import filters

class App:
    def __init__(self,window,window_name,videoSource = 0):
        self.window = window
        self.window_name = window_name
        self.window.title(self.window_name)

        self.videoSource = videoSource
        self.video = MyVideoCapture.MyVideoCapture(videoSource)

        self.canvas = tkinter.Canvas(window,width = self.video.width,height = self.video.height)
        self.canvas.pack()

        self.buttonScreen = tkinter.Button(self.window,text='Screenshot',width=50,command = self.snapshot)
        self.buttonScreen.pack(anchor=tkinter.CENTER,expand = True)

        self.buttonEdge = tkinter.Button(self.window,text = 'Edge Detection',width = 50,command = self.edgeFilter)
        self.buttonEdge.pack(anchor=tkinter.CENTER,expand = True)

        self.buttonEdge = tkinter.Button(self.window,text = 'Normal',width = 50,command = self.normal)
        self.buttonEdge.pack(anchor=tkinter.CENTER,expand = True)

        self.flag = 0

        self.delay = 15
        self.update()

        self.window.mainloop()

    def snapshot(self):
        if self.ret:
            cv2.imwrite('screenshot.png',cv2.cvtColor(self.frame,cv2.COLOR_RGB2BGR))


    def edgeFilter(self):
        self.flag = 1

    def normal(self):
        self.flag = 0

    def update(self):

        self.ret,self.frame = self.video.getFrame()
        if self.flag == 0:
            self.ret,self.frame = self.video.getFrame()

        if self.flag == 1:
            self.frame = filters.customEdgeDetection((3,3),cv2.cvtColor(self.frame,cv2.COLOR_RGB2BGR))
            self.frame = cv2.cvtColor(self.frame,cv2.COLOR_BGR2RGB)

        if self.ret:
            self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(self.frame))
            self.canvas.create_image(0,0,image = self.photo,anchor=tkinter.NW)

        self.window.after(self.delay,self.update)

App(tkinter.Tk(),"no_moje")



