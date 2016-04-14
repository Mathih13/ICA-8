
from Tkinter import *
from canvasTest import *
from RiverController import *

#BROOOOM
class ourFrame():
    
    def __init__(self, width, height, master):
        frame = Frame(master, width=width, height=height, bd=1)
        frame.pack()
    
        self.iframe5 = Frame(frame, bd=2, relief=RAISED)
        self.iframe5.pack(expand=1, fill=X, pady=10, padx=5)
        canvasData = ourCanvas(1400, 500, self.iframe5)
        c = canvasData.w
        c.pack()
        canvasData.setUp()
        
        self.riverController = riverController(master, canvasData)
        
        
        



root = Tk()
frame = ourFrame(2000, 1500, root)
root.title('River Crossing')
root.mainloop()


'''canvas = ourCanvas(1400, 500)
canvas.setUp()
mainloop()'''