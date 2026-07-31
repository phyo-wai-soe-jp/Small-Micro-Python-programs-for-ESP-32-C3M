#　0P01023 -  ピョー　ウェイ　ソー

from machine import PWM, Pin
from time import sleep

SERVO_PIN = 7
FREQ = 50
servo = PWM(Pin(SERVO_PIN), freq = FREQ)
### 
def angl_ns(angl_deg) :
    if -90 <= angl_deg <= 90 :
        return int(10**5 * (5 + (angl_deg + 90)/9))
    else :
        raise ValueError("角度の範囲を超えています")
###    
def strike(x,y,st,sc) :
    for a in range(sc):
        print( a+1 , "strike")
        for i in (x,y) :
            servo.duty_ns( angl_ns(i) )
            sleep(st/2)
        
###                
try :
    strike(0,20,1,10)
finally:
    servo.deinit() 

            