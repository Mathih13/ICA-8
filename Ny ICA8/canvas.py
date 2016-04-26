from view import *


class ourCanvas():
    
    def __init__(self, width, height, root):
        self.canvasWidth = width
        self.canvasHeight = height
        self.master = root
        
        self.w = Canvas(self.master, width=self.canvasWidth, height=self.canvasHeight)
        


    def setUp(self):
        # Create objects river, man, chicken, grain, fox, boat
        self.man = WorldObject("man", "black", (self.canvasWidth-self.canvasWidth), (self.canvasHeight-self.canvasHeight), 50, 50, 0.9, self.w)
        
        self.chicken = WorldObject("chicken", "green", (self.canvasWidth-self.canvasWidth), (self.canvasHeight-self.canvasHeight), 50, 50, 0.7, self.w)
        
        self.grain = WorldObject("grain", "yellow", (self.canvasWidth-self.canvasWidth), (self.canvasHeight-self.canvasHeight), 50, 50, 0.7, self.w)
        
        self.fox = WorldObject("grain", "red", (self.canvasWidth-self.canvasWidth), (self.canvasHeight-self.canvasHeight), 50, 50, 0.7, self.w)
        
        self.boat = WorldObject("boat", "black", (self.canvasWidth-self.canvasWidth), (self.canvasHeight-self.canvasHeight), 150, 20, 0.7, self.w)
        
        # Create river, position and get coordinates 
        self.river = WorldObject("river", "blue", (self.canvasWidth/3.5), (self.canvasHeight/8), 900, 30, 1, self.w)
        self.river.move(0, self.canvasHeight/1.2)
        self.riverCoords = self.river.returnCoords()
        
        # Move all other objects relative to the position
        # of the river object
        
        
        
        
        self.man.move(self.riverCoords[2]/2.75, self.riverCoords[0])
        self.boat.move(self.riverCoords[2]/2.25, self.riverCoords[0]+30)
        
        self.chicken.move(self.riverCoords[2]/3.25, self.riverCoords[0]+10)
        self.grain.move(self.riverCoords[2]/4, self.riverCoords[0]+10)
        self.fox.move(self.riverCoords[2]/5, self.riverCoords[0]+10)
        
        
        
       








