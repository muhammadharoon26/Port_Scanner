#!/bin/python3
import sys #allows us to enter command line arguments among other things
import socket
from datetime import datetime
#define our target
if(len(sys.argv)==2):
        target = socket.gethostbyname(sys.argv[1])
else:
        print("invalid amount of arguments")
        print(" python3 port_scanner.py <ip>")
        sys.exit()
#add pretty banner
print("-"*50)
print("scanning target" + target)
print("time started:" + str(datetime.now()))
print("-"*50)
try:
        for port in range(50,86):
            s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            socket.setdefaulttimeout(1) #is a float
            result = s.connect_ex((target,port)) #returns error indicator
            print("checking port {}........................................................".format(port))
            if(result==0):
                    print("port {} is open".format(port))
            else:
                    print("port {} is closed".format(port))
            s.close()
except KeyboardInterrupt:
        print("-"*50)
        print("exiting program" + "."*50)
        print("-"*50)
        sys.exit()
except socket.gaierror:
        print("hostname could not be resolved")
        sys.exit()
except socket.error:
        print("could not connect to server")
        sys.exit()