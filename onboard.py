
import machine
import time
LED=0
led= machine.Pin(LED,machine.Pin.OUT)

for n in range(2):
    led.on()
    time.sleep(1)
    led.off()
    time.sleep(1)
    