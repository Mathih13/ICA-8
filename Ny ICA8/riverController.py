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
        
        f= Button(self.master, text="Grain in", command=self.grainIn)
        f.pack(side=LEFT)        
        
        e= Button(self.master, text ="Fox in", command=self.foxIn)
        e.pack(side=LEFT)        
        
        d= Button(self.master, text="Drive boat right", command=self.moveBoatRight)
        d.pack(side=LEFT)
        
        
        h = Button(self.master, text="Drive boat left", command=self.moveBoatLeft)
        h.pack(side=LEFT)
        
        g= Button(self.master, text="chicken out", command=self.chickenOut)
        g.pack(side=LEFT)        
        
        j=Button(self.master, text="Fox Out", command=self.foxOut)
        j.pack(side=LEFT)
        
        i=Button(self.master, text="Grain Out", command=self.grainOut)
        i.pack(side = LEFT)
        
 
        
     
    
        
    def getOut(self):
        state=self.river.statusCheck()
        if (['man isat boat'] in self.river.river_db):
            if (['boat isat left'] in self.river.river_db):
                self.canvasData.man.move(-100, 20)
                self.river.getout()
            elif (['boat isat right'] in self.river.river_db):
                self.canvasData.man.move(+100, 20)
                self.river.getout()
                
            
        else:
            print "Man is not in boat"
            return


        
    def getIn(self):
        state = self.river.statusCheck()
        if (['man isat left'] in self.river.river_db and ["boat isat left"] in self.river.river_db):
            self.river.getIn()
            self.canvasData.man.move(100, -20)

            
        elif (["man isat right"] in self.river.river_db and ["boat isat right"] in self.river.river_db):
            self.river.getIn()
            self.canvasData.man.move(-100, -20)
        elif (['man isat boat'] in self.river.river_db):
            print "Man is already in boat"
            return

      
    def moveBoatRight(self):
        state = self.river.statusCheck()
        
        
        if (["chicken isat boat"] or ["fox isat boat"] or ["graint isat boat"] in self.river.river_db and (["boat isat left"] in self.river.river_db)):
            
            if (["chicken isat boat"] in self.river.river_db):
                self.canvasData.chicken.move(390,1)
                self.canvasData.boat.move(390,1)
                self.canvasData.man.move(390,1)
                self.river.crossriver()

                
            if (["grain isat boat"] in self.river.river_db):
                self.canvasData.grain.move(390,1)
                self.canvasData.boat.move(390,1)
                self.canvasData.man.move(390,1)
                self.river.crossriver()
            
            if (["fox isat boat"] in self.river.river_db):
                self.canvasData.fox.move(390, 1)
                self.canvasData.boat.move(390, 1)
                self.canvasData.man.move(390,1)
                self.river.crossriver()
                

    def moveBoatLeft(self):
        state = self.river.statusCheck()

        
        if (["chicken isat boat "] or ["fox isat boat"] or ["grain isat boat"] in self.river.river_db and ["boat isat right"] in self.river.river_db):
             
            if (["chicken isat boat"] in self.river.river_db):
                self.river.crossriver()
                self.canvasData.chicken.move(-390, -1)
                self.canvasData.boat.move(-390,-1)
                self.canvasData.man.move(-390,-1)
                
            else: 
                    self.canvasData.boat.move(-390,-1)
                    self.canvasData.man.move(-390,-1)
                    self.river.crossriver()  
                
        
    
        
            
    def chickenOut(self):
        state = self.river.statusCheck()
        if (['chicken isat boat']  and ["boat isat right"]in self.river.river_db):
            self.river.takeOut("chicken")
            self.canvasData.chicken.move(220, 20) 
            
        if (["chicken isat boat"] and ["boat isat left"] in self.river.river_db):
            self.river.takeOut("chicken")
            self.canvasData.chicken.move(-130, 20)
        
    
    
    def chickenIn(self):
        state = self.river.statusCheck()
        
        if (["grain isat boat"] in self.river.river_db):
            print "boat is full"        
        
        elif (["fox isat boat"]in self.river.river_db):
            print "boat is full"
        
        elif (["chicken isat right"] in self.river.river_db):
            self.river.putIn("chicken")
            self.canvasData.chicken.move(-180,-20)
            
        
        elif (self.river.statusCheck == "s1" or "s14" or "s20"):
            self.river.putIn("chicken")
            self.canvasData.chicken.move(130,-20)
            

     

    def foxIn(self):
        state = self.river.statusCheck()

        if (["chicken isat boat"] in self.river.river_db):
            print "boat is full"
            
        elif (["grain isat boat"] in self.river.river_db):
            print "boat is full"           
    
        elif (self.river.statusCheck == "s1" or "s6" or "s13" or "s14" ):
            self.river.putIn("fox")
            self.canvasData.fox.move(220, -20)   
        else:
            print"Noo noon noo"
            
    def foxOut(self):
        stat = self.river.statusCheck()
        if (["fox isat boat"] and ["boat isat right"] in self.river.river_db):
            self.river.takeOut("fox")
            self.canvasData.fox.move(210, 20)
       
        
    def grainIn(self):
        state = self.river.statusCheck()
        
        if (["chicken isat boat"] in self.river.river_db):
            print "boat is full"        
        
        elif (["fox isat boat"]in self.river.river_db):
            print "boat is full"        
        
        elif (['grain isat left'] and ["boat isat left"] in self.river.river_db):
            self.river.putIn("grain")
            self.canvasData.grain.move(180, -20)  
            
    def grainOut(self):
        state = self.river.statusCheck()
        if (["grain isat boat"] and ["boat isat right"] in self.river.river_db):
            self.river.takeOut("grain")
            self.canvasData.grain.move(+160, 20)