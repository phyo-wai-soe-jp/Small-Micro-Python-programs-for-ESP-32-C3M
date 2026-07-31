#　0P01023 -  ピョー　ウェイ　ソー

from machine import Pin
from neopixel import NeoPixel
from time import sleep

led = NeoPixel(Pin(10,Pin.OUT),3)

SW1 = 2 ; sw1 = Pin(SW1, Pin.IN)
SW2 = 3 ; sw2 = Pin(SW2, Pin.IN)
SW3 = 6 ; sw3 = Pin(SW3, Pin.IN)

color = [ RED, GREEN, BLUE ]
RED   = (50,  0, 0 )
GREEN = ( 0, 50, 0 )
BLUE  = ( 0,  0, 50)
OFF   = ( 0,  0, 0 )

def check_frequency() :
    sleep(0.1)

    

count = 0

    
try :
    while True :
       
        if    sw1.value() == 0 :
                count += 1
                
                if count  >= 20 :
                    led[0] = RED
                    led.write()
                    sleep(3)
                    led[0] = OFF
                    led.write()
                    count = 0
                
        if  sw2.value() == 0 :
                count += 1
                
                if count >= 20 :
                    led[1] = GREEN
                    led.write()
                    sleep(3)
                    led[1] = OFF
                    led.write()
                    count = 0
                
        if  sw3.value() == 0 :
                count += 1
                if count >= 20 :
                    led[2] = BLUE
                    led.write()
                    sleep(3)
                    led[2] = OFF
                    led.write()
                    count = 0
        
        
        check_frequency()
        
        
except KeyboardInterrupt:
         led[1] = OFF
         led.write()
         print("Program stopped")