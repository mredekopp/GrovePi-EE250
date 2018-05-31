# LED Server
# 
# This program runs on the Raspberry Pi and accepts requests to turn on and off
# the LED via TCP packets.

import sys
# By appending the folder of all the GrovePi libraries to the system path here,
# we are successfully `import grovepi`
sys.path.append('../../../Software/Python/')

import grovepi
import time
from grovepi import *

# use TCP
"""Example python3 server-side socket program using TCP from the tutorial video below.

https://www.youtube.com/watch?v=bTThyxVy7Sk&index=6&list=PL1A2CSdiySGIPxpSlgzsZiWDavYTAx61d
"""
import socket

def Main():
    # Connect the Grove LED to digital port D4
    led = 4

    pinMode(led,"OUTPUT")
    time.sleep(1)

#    host = '10.0.2.15' #'127.0.0.1'
    host = '192.168.1.213'
    port = 9001

    s = socket.socket()
    s.bind((host,port))

    s.listen(1)
    c, addr = s.accept()
    print("Connection from: " + str(addr))
    while True:
        try:
            data = c.recv(1024).decode('utf-8')
            if not data:
                break

            if(data == 'LED_ON'):
                digitalWrite(led,1)		# Send HIGH to switch on LED
                print ("LED ON!")
                c.send("LED turned ON".encode('utf-8'))
            elif(data == 'LED_OFF'):
                digitalWrite(led,0)		# Send LOW to switch off LED
                print ("LED OFF!")
                c.send("LED turned OFF".encode('utf-8'))
            elif(data == 'q'):
                print("Received quit command...exiting!")
                c.send("Server shutdown!".encode('utf-8'))
                break
            else:
                c.send("Unrecognized command".encode('utf-8'))
        except KeyboardInterrupt:	# Turn LED off before stopping
            digitalWrite(led,0)		# Send LOW to switch off LED
            c.send("Server had an unexpected error...quitting".encode('utf-8'))
            break
        except IOError:				# Print "Error" if communication error encountered
            c.send("Server had an unexpected error...quitting".encode('utf-8'))
            print ("Error")
            break

    c.close()



        
if __name__ == '__main__':
    Main()
