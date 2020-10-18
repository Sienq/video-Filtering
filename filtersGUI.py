import tkinter

class filtersGUI(tkinter.Frame):
    def __init__(self,master):
        super().__init__(master)

        #! FILTER BUTTONS
        self.master = master
        self.buttonEdge = tkinter.Button(self,text = 'Edge Detection',width = 50,command = self.edge)
        self.buttonEdge.grid(row=1,column=0)
        self.buttonNormal = tkinter.Button(self,text = 'Normal',width = 50,command = self.normal)
        self.buttonNormal.grid(row=2,column=0)
        self.buttonBlur = tkinter.Button(self,text = 'Blur',width = 50,command = self.blur)
        self.buttonBlur.grid(row=3,column=0)
        self.buttonSharpen = tkinter.Button(self,text = 'Sharpen',width = 50,command = self.sharpen)
        self.buttonSharpen.grid(row=4,column=0)
        self.buttonAsymethric = tkinter.Button(self,text = 'Asymethric',width = 50,command = self.asymethric)
        self.buttonAsymethric.grid(row=5,column=0)
        self.buttonLaplacian = tkinter.Button(self,text = 'Laplacian',width = 50,command = self.laplacian)
        self.buttonLaplacian.grid(row=6,column=0)
        
        self.filterType = 'Normal'

    def edge(self):
        self.filterType = 'Edge Detection'
    
    def normal(self):
        self.filterType = 'Normal'

    def blur(self):
        self.filterType = 'Custom Blur'

    def sharpen(self):
        self.filterType = 'Custom Sharpen'

    def asymethric(self):
        self.filterType = 'Custom Asymethric'

    def laplacian(self):
        self.filterType = 'Custom Laplacian'


        