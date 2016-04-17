from echoNY import Echo
from threading import Thread
from mainFrame import *


class connectionController():
    
    def __init__(self, server):   
        self.cThread = Thread(target=self.start_echo(self.riverDB))
        self.cThread.start()              
        
        
        
    
    def start_echo(self, db):
        s = Echo(db)
        s.start_socket()
        
        

conn = connectionController("y")


            
            
            
            