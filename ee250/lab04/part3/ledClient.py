# LED Client 
#
# This code sends requests to the Raspberry Pi to turn on and
#off the Grove LED using TCP packets.
import socket

def Main():
    """127.0.0.1 is the loopback address. Any packets sent to this address will
    essentially loop right back to your machine and look for any process 
    listening in on the port specified."""
    # host = '10.1.2.15'
    host = '192.168.1.124'
    port = 9002

    c = socket.socket() #by default, the socket constructor creates an TCP/IPv4 socket
    c.connect((host,port))

    message = input("-> ")
    while message != 'q':
        c.send(message.encode('utf-8')) 
        #1024 is the receive buffer size. It's enough for us, and it's a nice number. 
        data = c.recv(1024).decode('utf-8') 
        print("Status: " + data)
        message = input("-> ")
    c.close()

"""This if-statement checks if you are running this python file directly. That 
is, if you run `python3 tcpClient.py` in terminal, this if-statement will be 
true"""
if __name__ == '__main__':
    Main()
