#　0P01023 -  ピョー　ウェイ　ソー

from machine import PWM, Pin
from time import sleep

SERVO_PIN = 7
FREQ = 50
servo = PWM(Pin(SERVO_PIN), freq = FREQ)

def angl_ns(angl_deg) :
    if -90 <= angl_deg <= 90 :
        return int(10**5 * (5 + (angl_deg + 90)/9))
    else :
        raise ValueError("角度の範囲を超えています")

angles = [ i for i in range (-90, 96, 6)]
dur_s  = 1

try :
    for deg in angles :
        servo.duty_ns(angl_ns(deg))
        sleep(dur_s)
        print ( f" {deg}°  {dur_s}秒")
        
finally:
    servo.deinit() 
