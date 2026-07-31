#　0P01023 -  ピョー　ウェイ　ソー

from machine import Pin
from neopixel import NeoPixel
from time import sleep

# 関数−１
def off():
    for i in range(3):
        traffic_light[i] = (0, 0, 0)
    traffic_light.write()

# 関数-2
def dur():
   sleep(0.5)
    
# Object-1 for the 3 Pixcels
traffic_light = NeoPixel(Pin(10,Pin.OUT),3)

RED   = (50, 0, 0)
GREEN = (0, 50, 0)
BLUE  = (0, 0, 50)
color = [ RED, GREEN, BLUE ]

try:
    while True:
       for x in range(3):
           off()
           traffic_light[x] = color[x]
           traffic_light.write()
           dur()
           
           
           
except KeyboardInterrupt:
          off()
          print("Program stopped")
    
    