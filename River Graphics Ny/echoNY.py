import socket
import sys

from river import *

HOST = ''   # Symbolic name meaning all available interfaces
PORT = 8888 # Arbitrary non-privileged port

class Echo():
    
    def __init__(self, river):
        print "Here we go..."
        self.river = river
        self.riverDB = river.river_db
        
        
    def start_socket(self):
        try :
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            print 'Socket created'
            
        except socket.error, msg :
                print 'Failed to create socket. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
                sys.exit()
            
            
        # Bind socket to local host and port
        try:
            s.bind((HOST, PORT))
        except socket.error , msg:
            print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
            sys.exit()
        
        print 'Socket bind complete'   
        print 'Server started!'
        
        while True:
            data = s.recvfrom(1024)
            print data
            self.addr = data[1]          
            respons = self.decode(data)
            respons = str(respons)
            print respons
            if data:
                print >>sys.stderr, 'sending data back to the client'
                s.sendto(respons, (self.addr))
                
        
            else:
                print >>sys.stderr, 'no more data from', client_address
                break
        
            
        s.close()
        
    def decode(self, msg):
        if 'getriverDB' in msg:
            return self.riverDB
        
        elif 'getRiverInstance' in msg:
            return self.river
        
        elif 'riverStatusCheck' in msg:
            return self.river.statusCheck

        elif 'test' in msg:
            return "Hello, " + str(self.addr)        
        
        if 'get' in msg:
            if 'man' in msg :
                return  "pepe"
            elif 'boat' in msg:
                return self.state.tape.boat
            elif 'corn' in msg:
                return self.state.tape.corn
            elif 'fox' in msg:
                return self.state.tape.fox
            elif 'chicken' in msg:
                return self.state.tape.chicken        
            
server_River = River([['boat isat left'],['chicken isat left'],['fox isat left'],['man isat left'], ['grain isat left']])
e = Echo(server_River)
e.start_socket()