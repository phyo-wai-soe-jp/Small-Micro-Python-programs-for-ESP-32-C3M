from machine import PWM,Pin
from time import sleep

SPEAKER_PIN = 21
duty_in_per = 0.1
speaker = PWM(Pin(SPEAKER_PIN))
DUTY = int(duty_in_per / 100 * 65535)

notes = [
          
  [659, 462, 0],
  [740, 462, 0],
  [880, 462, 0],
  [831, 462, 0],
  [740, 462, 0],
  [659, 462, 0],
  [554, 923, 0],
  [659, 1846, 30],
  [659, 462, 0],
  [740, 462, 0],
  [880, 462, 0],
  [831, 462, 0],
  [740, 462, 0],
  [659, 462, 0],
  [554, 923, 0],
  [659, 1846, 30],

        ]
for f, s, p in notes :
    speaker.duty_u16(DUTY)
    speaker.freq(f)
    sleep(s/1000)
    speaker.duty_u16(0)          
    sleep(p / 1000)              

    
