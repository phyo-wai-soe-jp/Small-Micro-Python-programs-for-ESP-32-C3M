#　0P01023 -  ピョー　ウェイ　ソー

from machine import Pin
from neopixel import NeoPixel
from time import sleep

led = NeoPixel(Pin(10, Pin.OUT), 3)

SW1 = 2 ; sw1 = Pin(SW1, Pin.IN)
SW2 = 3 ; sw2 = Pin(SW2, Pin.IN)
SW3 = 6 ; sw3 = Pin(SW3, Pin.IN)
switch = [sw1, sw2, sw3]

#Program Settings

press_actv_dur_s = 2  #  long press duration 
light_dur_s      = 3  #  led's lighting duration in sec
RED     = (50,  0,  0)  #  colors in RGB system 
GREEN = ( 0, 50,  0)
BLUE    = ( 0,  0, 50)
OFF      = ( 0,  0,  0)

color = [RED, GREEN, BLUE]

def check_frequency():
    sleep(0.1)
    
def t3s_light(x):
    global count
    led[x] = color[x] ; led.write()
    sleep(light_dur_s)
    led[x] = OFF      ; led.write()
    count = 0

count_number = press_actv_dur_s * 0.1 * 100
count = 0

try:
    while True:
        for x in range(3):
            if switch[x].value() == 0:      
                count += 1
                if count >= count_number :
                    t3s_light(x)
        check_frequency()                   

except KeyboardInterrupt:
    for i in range(3):                      
        led[i] = OFF
    led.write()
    print("Program stopped")