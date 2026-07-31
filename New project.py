from machine import Pin, time_pulse_us
import time

trig = Pin(4, Pin.OUT)  # D4
echo = Pin(5, Pin.IN)   # D5

def distance_cm():
    trig.off()
    time.sleep_us(5)
    trig.on()
    time.sleep_us(10)
    trig.off()

    duration = time_pulse_us(echo, 1, 30000)

    if duration < 0:
        return None

    return duration * 0.0343 / 2

while True:
    distance = distance_cm()

    if distance is None:
        print("Sensor not detected")
    elif distance < 20:
        print("Object is NEAR: {:.1f} cm".format(distance))
    elif distance < 100:
        print("Object is FAR: {:.1f} cm".format(distance))
    else:
        print("Object is very far away")

    time.sleep(1)