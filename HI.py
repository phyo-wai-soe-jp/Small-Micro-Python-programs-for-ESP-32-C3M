# オンボードLEDの点滅
# onboard.py

# ハードウエア制御のモジュールをインポートする
import machine

# timeモジュールをインポートする
import time

# オンボードLEDはD0(GPIO0)に接続されている
LED = 0

# インスタンス(オブジェクト)を作成
led = machine.Pin(LED, machine.Pin.OUT)

# ledをONにしてLEDを点灯
led.on()

# 3秒間ONの状態を保持する
time.sleep(3)

# LEDを消灯
led.off()