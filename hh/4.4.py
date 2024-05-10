from machine import Pin, PWM
from neopixel import NeoPixel
import time

pin = Pin(8, Pin.OUT)
np = NeoPixel(pin, 1)

RED = (10, 0, 0)
GREEN = (0, 10, 0)
BLUE = (0, 0, 10)
YELLOW = (10, 10, 0)
PURPLE = (10, 0, 10)
CYAN = (0, 10, 10)
WHITE = (10, 10, 10)
BLACK = (0, 0, 0)

s = (0, 0, 0)





while True:
    # 呼吸灯效果
    for i in range(100):

        np[0] = (i, 0, 0)
        np.write()
        time.sleep(0.01)
    for i in range(100):

        np[0] = (100, i, 0)
        np.write()
        time.sleep(0.01)
    for i in range(100):

        np[0] = (100, 100, i)
        np.write()
        time.sleep(0.01)
