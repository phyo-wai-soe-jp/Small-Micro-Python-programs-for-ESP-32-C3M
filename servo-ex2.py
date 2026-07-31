#　0P01023 -  ピョー　ウェイ　ソー

from machine import PWM, Pin
from time import sleep
###
SERVO_PIN = 7
FREQ = 50
servo = PWM(Pin(SERVO_PIN), freq = FREQ)

sw1, sw2, sw3 = [ Pin(x,Pin.IN, Pin.PULL_UP) for x in  (2, 3, 6) ]

###
def angl_ns(angl_deg) :
    if -90 <= angl_deg <= 90 :
        return int(10**5*(5 + (angl_deg + 90)/9))
    else :
        raise ValueError("角度の範囲を超えています")
    
###
sw      = [  sw1, sw2, sw3 ]
angles = [  0, 90, -90 ]

###
try :
    while True :
        for i in range (len(sw)) :
           if sw[i].value() == 0 :
               print(f"スイッチ{i+1}が押されました。角度: {angles[i]}°")
               servo.duty_ns( angl_ns(angles [i] ) )
        sleep(0.1)

finally:
    servo.deinit() 
            