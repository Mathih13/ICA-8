# Import data about canvas and it's objects as well as the frame
# for the program
from view import *

from udp2 import *

# River and SM are the "model" of this
# design


class riverController():
    
    def __init__(self, master, canvasData):
        self.master = master
        self.canvasData = canvasData
        self.riverDB = self.getRiverDB()
        self.setUpButtons()
       
        

  
        
    def setUpButtons(self):
        a = Button(self.master, text="Get In", command=self.getIn)
        a.pack(side=LEFT)
        
        b= Button(self.master, text="Get out", command=self.getOut)
        b.pack(side=LEFT)
        
        c = Button(self.master, text="Chicken In", command=self.chickenIn_Out)
        c.pack(side=LEFT)
        
        d= Button(self.master, text="Drive boat", command=self.moveBoat)
        d.pack(side=LEFT)
        
        e= Button(self.master, text ="Fox in og out", command=self.foxIn_Out)
        e.pack(side=LEFT)
        
        f= Button(self.master, text="Grain in or out", command=self.grainIn_Out)
        f.pack(side=LEFT)

        g= Button(self.master, text="Reset canvas", command=self.resetWorld)
        g.pack(side=LEFT)
        
        # DEBUG
        h= Button(self.master, text="Print DB", command=self.printDB)
        h.pack(side=LEFT)        
        
        j= Button(self.master, text="Connection test", command=self.connTest)
        j.pack(side=LEFT)        
        
    
        
    def getOut(self):
        state=self.serverStatusCheck()
        if (['man isat boat'] in self.riverDB):
            if (['boat isat left'] in self.riverDB):
                self.canvasData.man.move(-100, +20)
            elif (['boat isat right'] in self.riverDB):
                self.canvasData.man.move(+100, -20)
                
            # One main "getout" that changes the placement of the man
            # In the database
            self.river.getout()
                    
        else:
            print "Man is not in boat"
            return


        
    def getIn(self):
        state = self.serverStatusCheck()
        if (['man isat left'] in self.riverDB):
            self.river.getIn()
            self.canvasData.man.move(100, -20)
        elif (state == "state where man is at right"):
            self.river.getIn()
            self.canvasData.man.move(-100, -20)
        elif (['man isat boat'] in self.riverDB):
            print "Man is already in boat"
            return

      
    def moveBoat(self):
        state = self.serverStatusCheck()
        if(self.serverStatusCheck() == "s1" or "s6" or "s8" or "s13" or "s14" or "s16" or "s20" or "22"):
            self.river.crossriver()
            self.canvasData.boat.move(390,1)
        if (self.failCheck == True):
            self.resetWorld()
        
            
    
    def resetWorld(self):
        self.canvasData.resetCanvas()
        self.riverDB.remove(['man isat boat'])
        print self.riverDB
        
        
    
    def chickenIn_Out(self):
        state = self.serverStatusCheck()
        if (self.serverStatusCheck() == "s1" or "s14" or "s20"):
            self.river.putIn("chicken")
            self.canvasData.chicken.move(115,-20)        
        

            
            
    
            
    def foxIn_Out(self):
        if (self.serverStatusCheck() == "s1" or "s6" or "s13" or "s14" ):
            self.river.putIn("fox")
            self.canvasData.fox.move(220,-10)         
       
        
    def grainIn_Out(self):
        if (['grain isat left'] in self.riverDB):
            self.river.putIn("grain")
            self.canvasData.grain.move(180,-10)          


        
    def failCheck(self):
        if (self.river.doesFail == True):
            print "FAILED"
            return 
        
        
        
    
    # DEBUG FUNCTIONS
    
    def printDB(self):
        self.river.database()
        
        
    def connTest(self):
        print client("test")
        
        
    def getRiverFromServer(self):
        return (client("getRiverInstance"))
        
    def getRiverDB(self):
        rdb = client("getriverDB")
        print rdb
        print type(rdb)
        print "----------"
        arrayl = rdb.split(',')
        print arrayl
        print type(arrayl)
        return arrayl
    
    def serverStatusCheck(self):
        return client("riverStatusCheck")