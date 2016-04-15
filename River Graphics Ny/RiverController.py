# Import data about canvas and it's objects as well as the frame
# for the program
from view import *

# River and SM are the "model" of this
# design
from river import *
from sm import *





class riverController():
    
    def __init__(self, master, canvasData):
        self.master = master
        self.canvasData = canvasData
        self.river = River([['boat isat left'],['chicken isat left'],['fox isat left'],['man isat left'], ['grain isat left']])
        self.river.updateWorld()
        self.setUpButtons()
       
    
    
  
        
    def setUpButtons(self):
        a = Button(self.master, text="Get In", command=self.getIn)
        a.pack(side=LEFT)
        
        b= Button(self.master, text="Get out", command=self.getOut)
        b.pack(side=LEFT)
        
        c = Button(self.master, text="Chicken in", command=self.chickenIn)
        c.pack(side=LEFT)
        
        d= Button(self.master, text="Drive boat right", command=self.moveBoatRight)
        d.pack(side=LEFT)
        
        h = Button(self.master, text="Drive boat left", command=self.moveBoatLeft)
        h.pack(side=LEFT)
        
        e= Button(self.master, text ="Fox in og out", command=self.foxIn_Out)
        e.pack(side=LEFT)
        
        f= Button(self.master, text="Grain in or out", command=self.grainIn_Out)
        f.pack(side=LEFT)
        
        g= Button(self.master, text="chicken out", command=self.chickenOut)
        g.pack(side=LEFT)
        
     
    
        
    def getOut(self):
        state=self.river.statusCheck()
        if (['man isat boat'] in self.river.river_db):
            if (['boat isat left'] in self.river.river_db):
                self.canvasData.man.move(-100, +20)
            elif (['boat isat right'] in self.river.river_db):
                self.canvasData.man.move(+100, -20)
                
            
        else:
            print "Man is not in boat"
            return


        
    def getIn(self):
        state = self.river.statusCheck()
        if (['man isat left'] in self.river.river_db):
            self.river.getIn()
            self.canvasData.man.move(100, -20)
        elif (state == "state where man is at right"):
            self.river.getIn()
            self.canvasData.man.move(-100, -20)
        elif (['man isat boat'] in self.river.river_db):
            print "Man is already in boat"
            return

      
    def moveBoatRight(self):
        state = self.river.statusCheck()
        if (["chicken isat boat"] or ["fox isat boat"] or ["graint isat boat"] in self.river.river_db and (["boat isat left"] in self.river.river_db)):
            
            if (["chicken isat boat"] in self.river.river_db):
                self.canvasData.chicken.move(450,1)
                self.canvasData.boat.move(390,1)
                self.river.crossriver()
                
            if (["grain isat boat"] in self.river.river_db):
                self.canvasData.grain.move(5450,1)
                self.canvasData.boat.move(390,1)
                self.river.crossriver()
            
            if (["fox isat boat"] in self.river.river_db):
                self.canvasData.fox.move(450,1)
                self.canvasData.boat.move(390,1)
                self.river.crossriver()
                
    def moveBoatLeft(self):
        state = self.river.statusCheck()
        if (self.river.statusCheck == "s3" or "s4" or "s9" or "s10" or "s12" or "s17" or "s18" or "s23" or "s24"):
            self.canvasData.boat.move(-390,-1)
            self.river.crossriver()  
        if (self.river.statusCheck == "s1" or "s2" or "s6" or "s8" or "s13" or "s14" or "s16" or "s20" or "s22"):
            print"boat is at left"
            return 
        
    
        
            
    def chickenOut(self):
        state = self.river.statusCheck()
        if (['grain isat left'] in self.river.river_db):
            self.river.takeOut("chicken")
            self.canvasData.chicken.move(200,1)        
        
    
    
    def chickenIn(self):
        state = self.river.statusCheck()
        if (self.river.statusCheck == "s1" or "s14" or "s20"):
            self.river.putIn("chicken")
            self.canvasData.chicken.move(115,-20)        
        #if(['chicken isat boat'] and ['boat is at right'] in self.river.river_db):
    
            
            

    def foxIn_Out(self):
        state = self.river.statusCheck()
        if (self.river.statusCheck == "s1" or "s6" or "s13" or "s14" ):
            self.river.putIn("fox")
            self.canvasData.fox.move(220,-10)   
        else:
            print"Noo noon noo"
       
        
    def grainIn_Out(self):
        if (['grain isat left'] in self.river.river_db):
            self.river.putIn("grain")
            self.canvasData.grain.move(180,-10)          





        
