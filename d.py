# Scan WiFi network aroud ESP32

import network
import time

# Make wlan instance as station
wlan = network.WLAN(network.STA_IF)

# Activate WiFi interface
wlan.active(True)

# Scan 5 times every 1 second
for n in range(5):
    print(wlan.scan())
    time.sleep(1)
    