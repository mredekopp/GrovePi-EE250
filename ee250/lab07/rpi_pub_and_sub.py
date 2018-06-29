"""EE 250L Lab 07 Skeleton Code

Run rpi_pub_and_sub.py on your Raspberry Pi."""
import sys
sys.path.append('../../Software/Python/')
import grovepi
from grovepi import *
import paho.mqtt.client as mqtt
import time
import _thread
from grove_rgb_lcd import *

def lcd_callback(client, userdata, message):
    #the third argument is 'message' here unlike 'msg' in on_message
    msg_str = str(message.payload, "utf-8")
    setText(msg_str);
    setRGB(0,128,64)


def led_callback(client, userdata, message):
    #the third argument is 'message' here unlike 'msg' in on_message
    msg_str = str(message.payload, "utf-8")
    led = 2
    if msg_str == 'LED_ON':
        digitalWrite(led,1)
    elif msg_str == 'LED_OFF':
        digitalWrite(led,0)
    
def on_connect(client, userdata, flags, rc):
    print("Connected to server (i.e., broker) with result code "+str(rc))

    #subscribe to topics of interest here
    client.subscribe("anrg-pi4/led")
    client.message_callback_add("anrg-pi4/led", led_callback)
    client.subscribe("anrg-pi4/lcd")
    client.message_callback_add("anrg-pi4/lcd", lcd_callback)

#Default message callback. Please use custom callbacks.
def on_message(client, userdata, msg):
    print("on_message: " + msg.topic + " " + str(msg.payload, "utf-8"))


    
def checkButton(client, button):
    while True:
        buttonval = grovepi.digitalRead(button)
        #print(buttonval)
        if buttonval==1:
            client.publish("anrg-pi4/button","pressed")
        time.sleep(0.1)
    

if __name__ == '__main__':
    led = 2
    pinMode(led, "OUTPUT")
    ultrasonic_ranger = 3
    button = 8
    grovepi.pinMode(button,"INPUT")
    #this section is covered in publisher_and_subscriber_example.py
    client = mqtt.Client()
    client.on_message = on_message
    client.on_connect = on_connect
    client.connect(host="eclipse.usc.edu", port=11000, keepalive=60)
    client.loop_start()

    _thread.start_new_thread(checkButton, (client,button))
    while True:
        # Get Ultrasonic sensor
        try:
            # Read distance value from Ultrasonic
            message = str(grovepi.ultrasonicRead(ultrasonic_ranger))
             
        except TypeError:
            print ("Error")
        except IOError:
            print ("Error")
        client.publish("anrg-pi4/ultrasonicRanger", message);
        time.sleep(1)
            

