from mainFrame import *
from threading import Thread

'''THIS PYTHON FILE "STARTS" THE PROGRAM!'''



# Create the Tkinter frame, give it a title
# then enter mainloop.
def startRunning():
    root = Tk()
    frame = ourFrame(2000, 1500, root)
    
    root.title('River Crossing')
    
    gThread = Thread(target=root.mainloop())
    gThread.start()





startRunning()