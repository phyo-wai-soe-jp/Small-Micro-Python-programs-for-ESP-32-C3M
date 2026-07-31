#　0P01023 -  ピョー　ウェイ　ソー

from machine import PWM, Pin
from random import choice
import time

SPEAKER_PIN = 21
DUTY    = int(50 / 100 * 65535)
SCALE   = [523, 587, 659, 698, 783, 880, 987, 1046]

speaker = PWM(Pin(SPEAKER_PIN))

try :
    while True:
        f = choice(SCALE)
        print(f)
        duty_u16 = DUTY
        speaker.freq(f)
        time.sleep(1)

except KeyboardInterrupt:
        speaker.duty_u16(0)
       
