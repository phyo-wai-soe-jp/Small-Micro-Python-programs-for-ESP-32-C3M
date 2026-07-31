#　0P01023 -  ピョー　ウェイ　ソー

from machine import Pin
from neopixel import NeoPixel
from random import randint
from time import sleep

# 関数−１
def off():
    for i in range(3):
        random_sprinkle[i] = (0, 0, 0)
        random_sprinkle.write()
        
# 関数-2
def dur():
    sleep(0.1)

   
# Object-1 for the 3 Pixcels    
random_sprinkle = NeoPixel(Pin(10, Pin.OUT), 3)

try:
    while True:
        for i in range(3): 
            random_sprinkle[i] = (randint(0, 50), randint(0, 50), randint(0, 50))
            random_sprinkle.write()
            dur()
            

except KeyboardInterrupt:
        off()
        print("Program stopped")    

    
