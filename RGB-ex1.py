#　0P01023 -  ピョー　ウェイ　ソー

from machine import Pin
from neopixel import NeoPixel
from time import sleep

# GPIO Pin 10  にある　３つの　LED を　使う
traffic_light = NeoPixel(Pin(10,Pin.OUT),3)

# LED-off  関数
def off():
    for i in range(3):
        traffic_light[i] = (0, 0, 0)
    traffic_light.write()
    
#  for loop  のために　 リスト   
light_list = [ (50,0,0),(50,50,0), (0,50,30) ]
sleep_list = [ 3, 1, 3 ]


try:
    
    while True:
        
        for x in range (3) :
            off()
            traffic_light[x] = light_list[x]
            traffic_light.write()
            sleep(sleep_list[x])
    
except KeyboardInterrupt:
        off()
        print("Program stopped")
        
 
    
        


