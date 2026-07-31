

# 色の設定を全てのLED
from machine import Pin
from neopixel import NeoPixel
rgb = NeoPixel(Pin(10, Pin.OUT), 3)
rgb[0] = (0,0,0)
rgb[1]=(0,0,)
rgb[2]=(0,0,0)
rgb.write()