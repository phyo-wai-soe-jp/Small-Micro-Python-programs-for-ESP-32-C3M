#　0P01023 -  ピョー　ウェイ　ソー

from machine import PWM, Pin
from time import sleep

SPEAKER_PIN = 21
DUTY = int(50 / 100 * 65535)
speaker = PWM(Pin(SPEAKER_PIN), duty_u16 = DUTY)

MELODY =  [494, 392, 294, 392, 440, 587,0,
                  294,440, 494, 440, 294, 392,0]

for m in MELODY :
    if m == 0 :
        speaker.duty_u16(0)
        sleep(0.5)
    else :
        print(m)
        speaker.duty_u16(DUTY)
        speaker.freq(m)
        sleep(0.6)
        
speaker.duty_u16(0)
