from view import *
from riverController import *

# Contains information about the tkinter frame
# and loads the canvas and RiverController
# that interacts with the river data
class ourFrame():
    
    def __init__(self, width, height, master):
        # Create the background frame
        frame = Frame(master, width=width, height=height, bd=1)
        frame.pack()
        
        # Create the "inner frame" to make it look nicer
        self.iframe5 = Frame(frame, bd=2, relief=RAISED)
        self.iframe5.pack(expand=1, fill=X, pady=10, padx=5)
        
        # Grab the data of our canvas and create a new one.
        canvasData = ourCanvas(1400, 500, self.iframe5)
        c = canvasData.w
        c.pack()
        canvasData.setUp()
        
        # Create the riverController, feed it the TK master and the canvas.
        self.riverController = riverController(master, canvasData)
        
        
        




