#　0P01023 -  ピョー　ウェイ　ソー

from machine import Pin
from neopixel import NeoPixel
import time

# declaration on switches

## GPIO PIN Number
SW1 = 2
SW2 = 3
SW3 = 6

sw1 = Pin(SW1, Pin.IN)
sw2 = Pin(SW2, Pin.IN)
sw3 = Pin(SW3, Pin.IN)


# about LEDs

## GPIO PIN Number
LED = 10

led = NeoPixel(Pin(LED, Pin.OUT), 3)


# Variable for Led_color

RED   = (50, 0, 0)
GREEN = (0, 50, 0)
BLUE  = (0, 0, 50)


# function for Led_off
 
def off():
    for i in range(3):
        led[i] = (0, 0, 0)
    led.write()

# Task loop
 
while True:
    sw1_value = sw1.value()
    sw2_value = sw2.value()
    sw3_value = sw3.value()

    off()
    
    if   sw1_value == 0 :
             led[0] = RED
         
        
    elif sw2_value == 0 :
             led[1] = GREEN
         
    
    elif sw3_value == 0 :
             led[2] = BLUE
    
    led.write()
    time.sleep(1)

    












