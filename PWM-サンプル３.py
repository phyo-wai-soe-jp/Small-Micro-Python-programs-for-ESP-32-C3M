# Play scale using piezo speaker
# May 13th 2026 (C) iot101 at zenn.dev

from machine import PWM, Pin
import time

# Frequency of the scale
SCALE = [523, 587, 659, 698, 783, 880, 987, 1046]

# Speaker is connected to GPIO21 pin
SPEAKER_PIN = 21

# Set duty 50%
DUTY = int(50 / 100 * 65535)

# Make speakder object
speaker = PWM(Pin(SPEAKER_PIN), duty_u16=DUTY)

# Play scale
for f in SCALE:
    print(f)
    speaker.freq(f)
    time.sleep(1)

# Stop sound, set duty 0
speaker.duty_u16(0)
