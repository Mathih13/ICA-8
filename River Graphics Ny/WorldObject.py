# The job of this calss is to hold information about 
# The object that is supposed to be drawn
# It does not draw anything specifically in this file,
# But relies on an outside canvas


class WorldObject():
    
    def __init__(self, name, color, x, y, width, height , scale, canvas):
        self.name = name
        self.color = color
        self.scale = scale
        self.c = canvas
        
        self.model = self.c.create_rectangle(x*scale, y*scale, width*scale, height*scale, fill=color)
        
        
        
        
    def move(self, x, y):
        self.c.move(self.model, x, y)
        prnt = "Man moved "
        print "Man moved " + str(x) + str(y)
        
        
    def returnCoords(self):
        return self.c.coords(self.model)