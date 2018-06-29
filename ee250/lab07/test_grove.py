"""EE 250L Lab 07 Skeleton Code

Run rpi_pub_and_sub.py on your Raspberry Pi."""
import sys
sys.path.append('../../Software/Python/')
import grovepi
from grovepi import *
import paho.mqtt.client as mqtt
import time

from grove_rgb_lcd import *

if __name__ == '__main__':
    led = 2
    pinMode(led, "OUTPUT")
    ultrasonic_ranger = 3
    flag = 1
    setText("Hi");
    setRGB(0,128,64)

    while True:
        # Get Ultrasonic sensor
        try:
             # Read distance value from Ultrasonic
            message = str(grovepi.ultrasonicRead(ultrasonic_ranger))
            print(message)
        except TypeError:
            print ("Error")
        except IOError:
            print ("Error")
        digitalWrite(led,flag)
        flag ^= 1
        time.sleep(1)
            

