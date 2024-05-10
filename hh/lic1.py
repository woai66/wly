import random
from machine import Pin, SoftSPI
import st7789py as st7789

from romfonts import vga1_16x32 as font


def main():
    #构造一个SPI对象
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
    while True:
        for rotation in range(4):
            tft.rotation(rotation)
            tft.fill(st7789.BLUE)
            col_max = tft.width - font.WIDTH * 6
            row_max = tft.height - font.HEIGHT

            for _ in range(100):
                tft.text(
                    font, "Hello!", random.randint(0, col_max),
                    random.randint(0, row_max),
                    st7789.color565(random.getrandbits(8),
                                    random.getrandbits(8),
                                    random.getrandbits(8)),
                    st7789.color565(random.getrandbits(8),
                                    random.getrandbits(8),
                                    random.getrandbits(8)))


main()
