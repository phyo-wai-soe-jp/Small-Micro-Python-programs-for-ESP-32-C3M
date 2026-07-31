#　0P01023 -  ピョー　ウェイ　ソー

from machine import Pin
from neopixel import NeoPixel
from time import sleep

led = NeoPixel(Pin(10,Pin.OUT),2)
sw  = Pin(2,Pin.IN)

#  Program Settings

press_actv_dur_s = 2  #  long press duration in sec
RED = ( 50, 0, 0 )    #  colors in RGB system 
OFF = (  0, 0, 0 )
led[1] = RED

def check_frequency() :
    sleep(0.1)

count_number = press_actv_dur_s * 0.1 * 100
count = 0
    
try :
    while True :
        if  sw.value() == 0 :
                count += 1
        else   :
                count = 0
        
        
        if count >= count_number   :
            if led[1] == OFF :
                led[1] = RED
                led.write()
                
            elif led[1] == RED :
                led[1] = OFF
                led.write()
            count = 0
            
        check_frequency()
        
except KeyboardInterrupt:
         led[1] = OFF
         led.write()
         print("Program stopped")
        
            


