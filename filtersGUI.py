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
        
        self.filterType = 'Normal'

    def edge(self):
        self.filterType = 'Edge Detection'
    
    def normal(self):
        self.filterType = 'Normal'


        