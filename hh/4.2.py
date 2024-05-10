from machine import Pin,SoftSPI,Timer
import machine,time,dht
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

d = dht.DHT11(Pin(4))
time.sleep(1)

tft.text(font, "DH11", 40,0, st7789.WHITE, st7789.BLACK)

def dht_get(tim):
    d.measure()

    tft.text(font, "temp: {:.2f}C".format(d.temperature()), 10, 40, st7789.WHITE, st7789.BLACK)
    print("temp: {:.2f}C".format(d.temperature()))
    tft.text(font, "hum: {:.2f}%".format(d.humidity()), 10, 70, st7789.WHITE, st7789.BLACK)
    print("hum: {:.2f}%".format(d.humidity()))


tim = Timer(0)
tim.init(period=2000, mode=Timer.PERIODIC, callback=dht_get)




