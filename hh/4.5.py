from machine import Pin, SoftSPI, Timer, SoftI2C
from HCSR04 import HCSR04
import st7789py as st7789
from romfonts import vga1_16x32 as font

spi = SoftSPI(baudrate=80000000,
              polarity=0,
              sck=Pin(2, Pin.OUT),
              mosi=Pin(3, Pin.OUT),
              miso=Pin(8))
# 此处reset对应屏幕RES所接的开发板的GPIO1脚，dc对应屏幕DC所接的开发板的GPIO6脚
tft = st7789.ST7789(spi,
                    240,
                    240,
                    reset=Pin(10, Pin.OUT),
                    dc=Pin(6, Pin.OUT),
                    cs=Pin(7, Pin.OUT),
                    backlight=Pin(8, Pin.OUT),
                    rotation=0)  # rotation 方向0-3方位

trig = Pin(9, Pin.OUT)
echo = Pin(8, Pin.IN)
hc = HCSR04(trig, echo)
tft.text(font, "csbo", 40, 0, st7789.WHITE, st7789.BLACK)


def fun(tim):
    distance = hc.getDistance()
    tft.text(font, "distance: {:.2f}cm".format(distance), 10, 50, st7789.WHITE,
             st7789.BLACK)
    print("distance: {:.2f}cm".format(distance))


tim = Timer(0)
tim.init(period=1000, mode=Timer.PERIODIC, callback=fun)
