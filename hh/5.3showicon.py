from machine import Pin, SoftSPI
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
                    rotation=0)

WHITE = 0xFFFF
tft.fill(WHITE)

tft.showIcon48x48("./icon/sunny.dat")