#import libs
import pyfiglet
import sys
import socket
from datetime import datetime

#Banner
ascii_banner = pyfiglet.figlet_format(" PORT ENUM")
print(ascii_banner)
print("  # Coded By Mohamed-Ali @mohamed-ali101")


target = input(str(" [+] Target IP: " ))

print("_" * 50)
print(" [+] Scanning Target: " + target)
print(" [+] Scanning Started at: " + str(datetime.now()))
print("_" * 50)

try:
    #scan every port
    for port in range(1,65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.5)

    #Return open port
        result = s.connect_ex((target,port))
        if result == 0:
           print("[+] Port {} is open".format(port))
        s.close()
    
except KeyboardInterrupt:
        print("\n Exiting")
        sys.exit()

except socket.error:
        print(" Host Not Responding :( ")
        sys.exit()