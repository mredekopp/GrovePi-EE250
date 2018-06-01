# Simple example of reading the MCP3008 analog input channels and printing
# them all out.
# Author: Tony DiCola
# License: Public Domain
import time

import RPi.GPIO as GPIO
led_pin = 17

#GPIO.setup(led_pin, GPIO.OUT)

# Import SPI library (for hardware SPI) and MCP3008 library.
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008
#import Adafruit_GPIO.GPIO as GPIO

# Software SPI configuration:
#CLK  = 23 #18
#MISO = 21 #23
#MOSI = 19 #24
#CS   = 24 #25
#mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)


# Hardware SPI configuration:
SPI_PORT   = 0
SPI_DEVICE = 0
mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))
GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin, GPIO.OUT)
while True:
    for i in range(5):
        GPIO.output(led_pin,1)
        time.sleep(0.5)
        GPIO.output(led_pin,0)
        time.sleep(0.5)
    for i in range(50):
        light_val = mcp.read_adc(0)
        print(light_val)
        if light_val < 511:
            print("dark")
        else:
            print("bright")
        time.sleep(0.1)
    for i in range(4):
        GPIO.output(led_pin,1)
        time.sleep(0.2)
        GPIO.output(led_pin,0)
        time.sleep(0.2)
    for i in range(50):
        sound_val = mcp.read_adc(1)
        if sound_val < 350:
            print("quiet")
            time.sleep(0.1)        
        else:
            print("loud")
            GPIO.output(led_pin,1)
            time.sleep(0.1)
            GPIO.output(led_pin,0)
    for i in range(4):
        GPIO.output(led_pin,1)
        time.sleep(0.2)
        GPIO.output(led_pin,0)
        time.sleep(0.2)
    
