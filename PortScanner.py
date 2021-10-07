
#!/bin/pyton

### 
# This will be a basic port scanner with nmap 


###/



import sys
import  socket
from datetime import datetime


# basic port scanner with nmap 

if len(sys.argv) == 2:
    target =socket.gethostbyname(sys.argv[1]) # translate to IPv4

else:
    print("invalid argument")     
    print("Syntax: PortScanner.py")


print("=" * 50 )
print(" ")
print("scanner target" + target )
print("Time started: " + str(datetime.now))
print(" ")
print("=" * 50 )

try:
    for port in range(50,85):
        s =socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        resul = s.connect_ex((target, port)) # returne the error idicator 
        if resul == 0:
            print("Port {} is opend".format(port))

except KeyboardInterrupt:
    print("\nExiting programe.")

except socket.gaierror:
    print("Hostaname could not be resolved.")
    sys.exit()

except socket.error:
    print("Couldn't connect to server.")
    sys.exit()