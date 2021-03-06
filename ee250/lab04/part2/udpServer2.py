"""Example python3 server side socket program using UDP adopted from the 
video tutorial below.

https://www.youtube.com/watch?v=bTThyxVy7Sk&index=6&list=PL1A2CSdiySGIPxpSlgzsZiWDavYTAx61d
"""

import socket

def Process2():
    # Change the host and port as needed. For ports, use a number in the 9000 
    # range. 
    host = '10.0.2.15' #'127.0.0.1'
    port = 9002

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host,port))

    print("Process 2 Server Started")
    while True:
        data, addr = s.recvfrom(1024)
        data = data.decode('utf-8')
        print("Message From: " + str(addr))
        print("From connected user: " + data)
        data = data.upper()
        print("Sending: " + data)
        s.sendto(data.encode('utf-8'), addr)
    c.close()

if __name__ == '__main__':
    Process2()
    
