import random
from machine import Pin, SoftSPI, RTC, Timer
import st7789py as st7789
import vga1_8x16 as font

week = [
    'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday',
    'Sunday'
]

time_list = ['', '', '']

spi = SoftSPI(baudrate=80000000,
              polarity=0,
              phase=0,
              sck=Pin(2, Pin.OUT),
              mosi=Pin(3, Pin.OUT),
              miso=Pin(8))

tft = st7789.ST7789(spi,
                    240,
                    240,
                    reset=Pin(10, Pin.OUT),
                    cs=Pin(7, Pin.OUT),
                    dc=Pin(6, Pin.OUT),
                    backlight=Pin(8, Pin.OUT),
                    rotation=0)

print('ok')

rtc = RTC()

if rct.datetime()[0] == 2024:
    rtc.datetime((2024, 4, 25, 0, 0, 0, 0, 0))


def RTC_RUN():
    datetime = rtc.datetime()
    tft.text(font, "ZUCC RTC", 0, 0, st7789.WHITE, st7789.BLACK)
    time = str(datetime[0]) + '-' + str(datetime[1]) + '-' + str(
        datetime[2]) + '-' + week[datetime[3]]
