from machine import Pin, SoftSPI
import st7789py as st7789
import micropython
from romfonts import vga1_16x32 as font


gc.collect()

print(micropython.mem_info())


spi = SoftSPI(baudrate=80000000, polarity=0, phase=0, sck=Pin(2,Pin.OUT), mosi=Pin(3,Pin.OUT), miso=Pin(8))

tft = st7789.ST7789(spi,240,240,reset=Pin(10, Pin.OUT),cs=Pin(7, Pin.OUT),dc=Pin(6, Pin.OUT), backlight=Pin(8, Pin.OUT),rotation=0)

tft.text(font, "HZCU 1", 80, 0, st7789.BLUE, st7789.BLACK)
tft.text(font, "HZCU 2", 80, 16, st7789.GREEN, st7789.BLACK)
tft.text(font, "HZCU 3", 80, 32, st7789.RED, st7789.BLACK)
tft.text(font, "HZCU 4", 80, 48, st7789.YELLOW, st7789.BLACK)
