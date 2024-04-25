from machine import Pin, SoftSPI
import st7789py as st7789
import micropython
from romfonts import font_gb_16x16 as font


gc.collect()

print(micropython.mem_info())


spi = SoftSPI(baudrate=80000000, polarity=0, phase=0, sck=Pin(2,Pin.OUT), mosi=Pin(3,Pin.OUT), miso=Pin(8))

tft = st7789.ST7789(spi,240,240,reset=Pin(10, Pin.OUT),cs=Pin(7, Pin.OUT),dc=Pin(6, Pin.OUT),rotation=0)

tft.text_gb16(font, "章永琪最帅", 80, 0, st7789.BLUE, st7789.BLACK)
# tft.text(font, "章永琪最帅", 80, 16, st7789.BLUE, st7789.BLACK)