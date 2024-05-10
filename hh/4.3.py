from machine import Pin,SoftSPI,Timer, SoftI2C
import bmp280
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

i2c1 = SoftI2C(scl=Pin(21), sda=Pin(20))
bmp = bmp280.BMP280(i2c1)   # Create a BMP280 object

tft.text(font, "QIYA", 40,0, st7789.WHITE, st7789.BLACK)

def fun(tim):
    tft.text(font, "temp: {:.2f}C".format(bmp.getTemp()), 10, 30, st7789.WHITE, st7789.BLACK)
    print("temp: {:.2f}C".format(bmp.getTemp()))  
    tft.text(font, "press: {:.2f}Pa".format(bmp.getPress()), 10, 70, st7789.WHITE, st7789.BLACK)
    print("press: {:.2f}Pa".format(bmp.getPress()))
    tft.text(font, "alt: {:.2f}m".format(bmp.getAltitude()), 10, 110, st7789.WHITE, st7789.BLACK)
    print("alt: {:.2f}m".format(bmp.getAltitude()))

tim = Timer(0)
tim.init(period=1000, mode=Timer.PERIODIC, callback=fun)