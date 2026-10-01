# ESP32-C3M-TRY のための MicroPython プログラム集

電子工作をはじめる人が、部品を1つずつ動かして覚えるための、短いプログラム集です。

## 1. 何の役に立つか

「まず光らせたい」「サーボを動かしたい」というときに、そのまま動く手本があります。

- 光らせる — RGB LED(NeoPixel)を1色、複数色、パターンで
- 動かす — PWM の基本と、サーボの角度指定
- 反応させる — スイッチの読み取り、押し方による動きの違い
- 測る — 基板に載っているセンサーの値を読む
- 鳴らす — 圧電ブザーで曲を演奏(『Perfect』『River flows in you』)
- つなぐ — まわりのWi-Fiを探す

どれも1ファイルで完結していて短いので、読んで、数字を変えて、すぐ試せます。授業や自習の出発点として使えます。

## 2. 使っている技術

- **MicroPython** — ESP32-C3M-TRY ボード向け
- **使っている部品とピン** — NeoPixel RGB LED(GPIO 10)、サーボ / PWM(GPIO 7)、圧電ブザー(GPIO 21)、スイッチ入力、オンボードセンサー、Wi-Fi

| ファイル | 中身 |
| --- | --- |
| `onboard*.py` | 基板のLED・センサーの基本 |
| `RGB-ex*.py` | NeoPixel RGB LED の制御 |
| `pwm-ex*.py`, `PWM-サンプル３.py` | PWM 信号の作り方 |
| `servo-ex*.py` | サーボの角度制御 |
| `sw-ex*.py` | スイッチ入力の扱い |
| `Perfect.py`, `River flows in you.py` | ブザーでの曲の再生 |
| `d.py` | Wi-Fi スキャナ |

使い方: ボードに MicroPython のファームウェアを書き込み、`mpremote` か Thonny でファイルを転送します。
