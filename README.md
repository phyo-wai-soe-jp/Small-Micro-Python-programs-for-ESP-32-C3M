# IoT Programs in MicroPython

A collection of MicroPython scripts for the ESP32-C3M-TRY board, covering the onboard peripherals one at a time: RGB LEDs (NeoPixel), PWM/servo control, switches, and onboard sensors. Also includes a small buzzer melody player.

## Contents

- `onboard*.py` — onboard LED / sensor basics
- `RGB-ex*.py` — NeoPixel RGB LED control (GPIO 10)
- `pwm-ex*.py`, `PWM-サンプル３.py` — PWM signal generation
- `servo-ex*.py` — servo angle control via PWM (GPIO 7)
- `sw-ex*.py` — switch/button input handling
- `Perfect.py`, `River flows in you.py` — buzzer melody playback (GPIO 21)
- `d.py` — Wi-Fi network scanner

## Setup

Flash a MicroPython firmware build to the board, then copy the scripts over with `mpremote` or Thonny.
