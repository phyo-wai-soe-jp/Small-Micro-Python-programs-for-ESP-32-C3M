# オンボードLEDを10回点滅させる
# onboard2.py

# ハードウエア制御のモジュールをインポートする
import machine

# timeモジュールをインポートする
import time

# オンボードLEDはD0(GPIO0)に接続されている
LED = 0

# インスタンス(オブジェクト)を作成
led = machine.Pin(LED, machine.Pin.OUT)

# 1秒ごとにLEDの点灯、消灯を10回繰り返す
for n in range(10):
    # LED点灯
    led.on()

    # 1秒間ONの状態を保持する
    time.sleep(0.3)

    # LEDを消灯
    led.off()
    
    # 1秒間OFFの状態を保持する
    time.sleep(0.1)