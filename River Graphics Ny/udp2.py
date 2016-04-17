# some code from https://pymotw.com/2/socket/tcp.html
import socket
import sys

host = 'cm-84.214.46.25.getinternet.no';
port = 8888;

def client(command) :
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    except socket.error:
        print 'Failed to create socket'
        sys.exit()


    

    try:
        # Send data
        s.sendto(command, (host, port))

        # Look for the response
        amount_received = 0
        amount_expected = len(command)

        # while there is data that are to be proceeded
        while amount_received < amount_expected:
            data = s.recvfrom(1024)
            amount_received += len(data)
            #print >>sys.stderr, 'received "%s"' % data
            return data[0]

    finally:
        s.close()
        
    
inp = raw_input("command: ")

c = client(inp)