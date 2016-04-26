# -*- coding: utf-8 -*-
# OBS! Dårlig kodingstil! For eksempel, kommentarer skal høre til funksjoner og være mellom '''disse'''

from sm import SM
import sys


class River(SM):
    
    river_db = [] # En klønete måte å definere database på, bør være i egen klasse og kanskje ikke en liste?
    
    
    # Blir kalt hver gang klassen blir instansiert
    def __init__(self, initialValue): 
        self.startState = initialValue
        self.river_db = self.startState
        

    
    def crossriver(self):
        # Meget primitiv implementasjon av crossriver, her må flere detaljer inn!
        if (['man isat boat'] in self.river_db):
            if ['boat isat left'] in self.river_db:
                self.remove(['boat isat left'])
                self.add(['boat isat right'])
            elif ['boat isat right'] in self.river_db:
                self.remove(['boat isat right'])
                self.add(['boat isat left']) 
        else:
            print "Man is not in boat. Please get in."
        self.updateWorld()
            
    
    def putIn(self, item):
        if ([item +' isat left'] in self.river_db):
            self.remove([item+' isat left'])
        else:
            self.remove([item+' isat right'])
        self.add([item+' isat boat'])
        self.updateWorld()
    
    def takeOut(self, item):
        self.remove([item+' isat boat'])
        if ['boat isat left'] in self.river_db:
            self.add([item+' isat left'])
        if ['boat isat right'] in self.river_db:
            self.add([item+' isat right'])
        self.updateWorld()
    
    
    def getIn(self):
        # Check where man is, remove the correct one(existing one)
        if ['man isat left'] in self.river_db:
            self.remove(['man isat left'])
        elif ['man isat right'] in self.river_db:
            self.remove(['man isat right'])
            
        self.add(['man isat boat']) # Add man to boat.
        self.updateWorld()
    
    def getout(self):
        # Check if the man is in the boat at all
        if ['man isat boat'] in self.river_db:
            self.remove(['man isat boat']) # Remove man from boat
            
            # Check if man is exiting on left or right side.
            if ['boat isat left'] in self.river_db:
                self.add(['man isat left'])
            elif ['boat isat right'] in self.river_db:
                self.add(['man isat right'])
        else:
            print 'Cannot get out. The man is not in the boat.' # If man is not in the boat.
        self.updateWorld()
            
    def manCheck(self): 
        # Run a check to see where the man is currently and apply the ' man' to the relevant string. 
        self.boatman = ''
        self.landmanleft = ''
        self.landmanright = ''
        
        if (['man isat boat'] in self.river_db):
            self.boatman = ' man'

    
        if (['man isat left'] in self.river_db):
            self.landmanleft = ' man'

        
        if (['man isat right']) in self.river_db:
            self.landmanright = ' man'  
         
    
    def interface(self):
        # Her implementeres logikken for "vakker" utskrift
        # ...
        
        
        print "** Here is the state of the river-world:"
        
        self.s1         = "** [chicken fox grain" +self.landmanleft+" ---\\ \\_" + self.boatman+"_/ _____________/---"+self.landmanright+"]"
        self.s2         = "** [fox grain" +self.landmanleft+" ---\\ \\_chicken" + self.boatman+"_/ _____________/---"+self.landmanright+"]"
        self.s3         = "** [fox grain"+self.landmanleft+"---\\ \ _________________\_ chicken"+self.boatman+" _//---"+self.landmanright+"]"
        self.s4         = "** [fox grain"+self.landmanleft+"---\\ \ _________________\_"+self.boatman+"_//---chicken"+self.landmanright+"]"
        self.s5         = "** [fox grain"+self.landmanleft+"---\\ \ _________________\_"+self.boatman+"_//---chicken"+self.landmanright+"]"
        self.s6         = "** [fox grain"+self.landmanleft+"---\\ \\_"+self.boatman+"_/ ________________ /---chicken"+self.landmanright+"]"
        self.s7         = "** [fox grain"+self.landmanleft+"---\\ \\_"+self.boatman+"_/ ________________ /---chicken"+self.landmanright+"]"
        self.s8         = "** [fox "+self.landmanleft+"---\\ \\_grain"+self.boatman+"_/ ________________ /---chicken"+self.landmanright+"]"
        self.s9         = "** [fox "+self.landmanleft+"---\\ \________________ \_grain"+self.boatman+"_/ /---chicken"+self.landmanright+"]"
        self.s10        = "** [fox"+self.landmanleft+"---\\ \________________ \_"+self.boatman+"_/ /---grain chicken"+self.landmanright+"]"
        self.s11        = "** [fox"+self.landmanleft+"---\\ \________________ \_"+self.boatman+"_/ /---grain chicken"+self.landmanright+"]"
        self.s12        = "** [fox"+self.landmanleft+"---\\ \________________ \_chicken"+self.boatman+"_/ /---grain "+self.landmanright+"]"
        self.s13        = "** [fox "+self.landmanleft+"---\\ \\_chicken"+self.boatman+"_/ ________________ /---grain"+self.landmanright+"]"
        self.s14        = "** [fox chicken"+self.landmanleft+"---\\ \\_"+self.boatman+"_/ ________________ /---grain"+self.landmanright+"]"
        self.s15        = "** [fox chicken"+self.landmanleft+"---\\ \\_"+self.boatman+"_/ ________________ /---grain"+self.landmanright+"]"
        self.s16        = "** [chicken"+self.landmanleft+"---\\ \\_fox"+self.boatman+"_/ ________________ /---grain"+self.landmanright+"]"
        self.s17        = "** [chicken"+self.landmanleft+"---\\ \________________ \_fox"+self.boatman+"_/ /---grain "+self.landmanright+"]"
        self.s18        = "** [chicken"+self.landmanleft+"---\\ \________________ \_"+self.boatman+"_/ /---fox grain "+self.landmanright+"]"
        self.s19        = "** [chicken"+self.landmanleft+"---\\ \________________ \_"+self.boatman+"_/ /---fox grain "+self.landmanright+"]"
        self.s20        = "** [chicken"+self.landmanleft+"---\\ \\_"+self.boatman+"_/ ________________ /---fox grain"+self.landmanright+"]"
        self.s21        = "** [chicken"+self.landmanleft+"---\\ \\_"+self.boatman+"_/ ________________ /---fox grain"+self.landmanright+"]"
        self.s22        = "** ["+self.landmanleft+"---\\ \\_chicken"+self.boatman+"_/ ________________ /---fox grain"+self.landmanright+"]"
        self.s23        = "** ["+self.landmanleft+"---\\ \________________ \_chicken"+self.boatman+"_/ /---fox grain "+self.landmanright+"]"
        self.s24        =  "** ["+self.landmanleft+"---\\ \________________ \_"+self.boatman+"_/ /---chicken fox grain "+self.landmanright+"]"
        self.s25        = "Congratulations! The farmer can now sell his goods at the market!"
        
        
        #
        self.f1         = "** [chicken fox " +self.landmanleft+" ---\\ \\_grain" + self.boatman+"_/ _____________/---"+self.landmanright+"]"
        self.f2         = "** [fox chicken"+self.landmanleft+"---\\ \ _________________\_ grain"+self.boatman+" _//---"+self.landmanright+"]"
        
        #All at right
        self.allAtRight      = "** ["+self.landmanleft+"---\\ \\_"+self.boatman+"_/ ________________ /---chicken fox grain"+self.landmanright+"]"
        
        
        
        
        # .... slik kan alle tilstander "tegnes"
        
        
        # Bruk betingelse og finn ut tilstanden fra database (db, som er en liste av lister)
        # For eksempel, hvis alt er på venstre siden av elven, skriv ut allAtLeft "bilde"
        # Dette er ikke en korrekt kode, - man bør sjekke på flere tilstandsvariabler
        # eller implementere datastrukturer som genererer "bilder" automatisk, basert på innholdet
        # i databasen
        
    def statusCheck(self):
        
        
        #All At Left
        if ['man isat left'] in self.river_db and ['boat isat left'] in self.river_db and ['fox isat left'] in self.river_db and ['chicken isat left'] in self.river_db and ['grain isat left'] in self.river_db:
            print self.s1
            return "s1"
            
        #All at left, chicken in boat  
        elif ['man isat left'] in self.river_db and ['boat isat left'] in self.river_db and ['chicken isat boat'] in self.river_db and ['fox isat left'] in self.river_db and ['grain isat left'] in self.river_db:
            print self.s2
            return "s2"
            
        # Some at left, chicken at right in boat 
        elif ['man isat boat'] in self.river_db and ['boat isat right'] in self.river_db and ['chicken isat boat'] in self.river_db and ['fox isat left'] in self.river_db and ['grain isat left'] in self.river_db:
            print self.s3
            return "s3"
        
        # som at left, chicken at right
        elif ['man isat right'] in self.river_db and ['boat isat right'] in self.river_db and ['chicken isat right'] in self.river_db and ['fox isat left'] in self.river_db and ['grain isat left'] in self.river_db:
            print self.s4
            return "s4"
            
        #some at left, chicken at right, boat at left
        elif ['boat isat left'] in self.river_db and ['chicken isat right'] in self.river_db and ['fox isat left'] in self.river_db and ['grain isat left'] in self.river_db:
            print self.s6
            return "s6"
            
        #some at left, boat at left, grain in boat, chicken at right
        elif ['boat isat left'] in self.river_db and ['chicken isat right'] in self.river_db and ['fox isat left'] in self.river_db and ['grain isat boat'] in self.river_db:
            print self.s8
            return "s8"
            
        #som at left, boat at right, grain in boat, chicken at right 
        elif ['boat isat right'] in self.river_db and ['chicken isat right'] in self.river_db and ['fox isat left'] in self.river_db and ['grain isat boat'] in self.river_db:
            print self.s9
            return "s9"
    
        
        #fox at left, boat at right, chicken and grain at right 
        elif ['boat isat right'] in self.river_db and ['chicken isat right'] in self.river_db and ['fox isat left'] in self.river_db and ['grain isat right'] in self.river_db:
            print self.s10
            return "s10"
        
        #fox at left, boat at right, chicken at boat, grain at right 
        elif ['boat isat right'] in self.river_db and ['chicken isat boat'] in self.river_db and ['fox isat left'] in self.river_db and ['grain isat right'] in self.river_db:
            print self.s12
            return "s12"
            
        #fox at left, boat at left, chicken at boat, grain at right 
        elif ['boat isat left'] in self.river_db and ['chicken isat boat'] in self.river_db and ['fox isat left'] in self.river_db and ['grain isat right'] in self.river_db:
            print self.s13
            return "s13"
            
        #fox at left, chicken at left, boat at left, grain at right
        elif ['boat isat left'] in self.river_db and ['chicken isat left'] in self.river_db and ['fox isat left'] in self.river_db and ['grain isat right'] in self.river_db:
            print self.s14
            return "s14"
        
        #chicken at left, boat at left, fox at boat, grain at right
        elif ['boat isat left'] in self.river_db and ['chicken isat left'] in self.river_db and ['fox isat boat'] in self.river_db and ['grain isat right'] in self.river_db:
            print self.s16
            return "s16"
    
            
        #chicken at left, boat at right, fox at boat, grain at right
        elif ['boat isat right'] in self.river_db and ['chicken isat left'] in self.river_db and ['fox isat boat'] in self.river_db and ['grain isat right'] in self.river_db:
            print self.s17
            return "s17"
            
        #chicken at left, boat at right, fox at right, grain at right 
        elif ['boat isat right'] in self.river_db and ['chicken isat left'] in self.river_db and ['fox isat right'] in self.river_db and ['grain isat right'] in self.river_db:
            print self.s18
            return "s18"
        
        #chicken at left, boat at left, rest at right 
        elif ['boat isat left'] in self.river_db and ['chicken isat left'] in self.river_db and ['fox isat right'] in self.river_db and ['grain isat right'] in self.river_db:
            print self.s20
            return "s20"
            
        #boat at left, chicken at boat, rest at right 
        elif ['boat isat left'] in self.river_db and ['chicken isat boat'] in self.river_db and ['fox isat right'] in self.river_db and ['grain isat right'] in self.river_db:
            print self.s22 
            return "s22"
            
        
        #boat at right, chicken at boat, rest at right 
        elif ['boat isat right'] in self.river_db and ['chicken isat boat'] in self.river_db and ['fox isat right'] in self.river_db and ['grain isat right'] in self.river_db:
            print self.s23
            return "s23"
            
        elif ['boat isat right'] in self.river_db and ['chicken isat right'] in self.river_db and ['fox isat right'] in self.river_db and ['grain isat right'] in self.river_db:
            print self.s24
            return "s24"
        # ALL AT RIGHT, YOU WIN
        elif ['boat isat right'] in self.river_db and ['chicken isat right'] in self.river_db and ['fox isat right'] in self.river_db and ['grain isat right'] in self.river_db and ['man isat right'] in self.river_db:
            print self.s25
            return "s25"
            
            
        elif ['fox isat left'] in self.river_db and ['chicken isat left'] in self.river_db and ['grain isat boat'] in self.river_db:
            print self.f1
            return "f1"
        elif ['fox isat left'] in self.river_db and ['chicken isat left'] in self.river_db and ['grain isat boat'] in self.river_db and ['boat isat right'] in self.river_db:
            print self.f2
            return "f2"
            
            
    def winCondition(self):
        #Boat at right, man in boat
        if ['boat isat right'] in self.river_db and ['man isat boat'] in self.river_db:
            if ['chicken isat left'] in self.river_db and ['grain isat left'] in self.river_db:
                print 'MISHAP -- The chicken has eaten the grain! Try again.'
                self.killWorld()
            elif ['chicken isat left'] in self.river_db and ['fox isat left'] in self.river_db:
                print 'MISHAP -- The fox has eaten the chicken! Try again.'
                self.killWorld()

        #Boat at left, man in boat
        elif ['boat isat left'] in self.river_db and ['man isat boat'] in self.river_db:
            if ['chicken isat right'] in self.river_db and ['grain isat right'] in self.river_db:
                print 'MISHAP -- The chicken has eaten the grain! Try again.'
                self.killWorld()
            elif ['chicken isat right'] in self.river_db and ['fox isat right'] in self.river_db:
                print 'MISHAP -- The fox has eaten the chicken! Try again.'
                self.killWorld()
                
        elif ['chicken isat right'] in self.river_db and ['grain isat right'] in self.river_db and ['fox isat right'] in self.river_db:
            print self.s25
            self.killWorld()
            
    # Denne funksjonen skal definere alle overgangene fra en tilstand til en annen
    # De kan være mange, så her må man skrive en smart kode
    # Eksperimentere først med enkelte kommandoer, og så implementere denne funksjonen
    def getNextValues(self, state, inp):
        # input her er et kommandonavn og den tilsvarende funksjonen må kalles opp
        pass
        
    # Database "saker", bør ligge i egen modul
    def database(self):
        print self.river_db
    def add(self, item):
        self.river_db.append(item)
    def remove(self, item):
        self.river_db.remove(item) # typisk MISHAP, hvis item ikke finnes i listen river_db
    def updateWorld(self): # Kjører alle sjekkene for hvor ting befinner seg pluss laster inn riktig "interface print"
        self.manCheck()
        self.interface()        
        self.statusCheck()
        self.winCondition()
        
    def killWorld(self):
        sys.exit()    
