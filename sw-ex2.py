#　0P01023 -  ピョー　ウェイ　ソー

from machine import Pin
from neopixel import NeoPixel
from time import sleep
#   プロコラムの実行スピード 最速度になるため、モジュール全体じゃなくて、特定のクラスだけを抜き出す。
#  　To maximize the running speed of program, importing only necessary classes, not the whole modules.

led = NeoPixel(Pin(10,Pin.OUT),3)
#    Using two LEDs from GPIO Pin no. 10.


SW1 = 2 ; sw1 = Pin(SW1, Pin.IN)
SW2 = 3 ; sw2 = Pin(SW2, Pin.IN)
SW3 = 6 ; sw3 = Pin(SW3, Pin.IN)
sw  = [sw1, sw2, sw3]

#Program Settings

switch_number   = 1       #  used switch number
led_number       = 2       #  used led number
led_color           = "red"   #  used color
press_actv_dur_s = 2       #  long press duration in sec
light_dur_s      = 3       #  led's lighting duration in sec

color_box = {
    "rose":      (48, 12, 20),
    "amber":     (49, 30,  4),
    "gold":      (49, 42,  8),
    "lime":      (28, 49, 10),
    "emerald":   (10, 49, 26),
    "teal":      ( 6, 45, 44),
    "sky":       (12, 36, 49),
    "indigo":    (16, 14, 48),
    "violet":    (34, 12, 49),
    "magenta":   (49, 10, 40),
    "red" :      (50,  0,  0),
}

OFF =   (  0, 0, 0 )

def check_frequency() :
    sleep(0.1)

def off() :
    for i in range(3):                      
            led[i] = OFF
            led.write()
            
count_number = press_actv_dur_s * 0.1 * 100
count = 0
    
try :
    while True :
       
        if  sw[switch_number - 1].value() == 0 :
                count += 1
        else   :
                count = 0
           
        if count >= count_number : 
                led[led_number - 1] = color_box.get(led_color) ; led.write()
                sleep(light_dur_s)
                led[led_number - 1] = OFF ; led.write()
                count = 0
        
        check_frequency()
        
        
except KeyboardInterrupt:
         off()
         print("Program stopped")
        
            

