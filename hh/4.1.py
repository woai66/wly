from machine import Pin, SoftSPI, Timer
import onewire, ds18x20
import st7789py as st7789
from romfonts import vga1_16x32 as font

spi = SoftSPI(baudrate=80000000,
              polarity=0,
              sck=Pin(2, Pin.OUT),
              mosi=Pin(3, Pin.OUT),
              miso=Pin(8))

tft = st7789.ST7789(spi,
                    240,
                    240,
                    reset=Pin(10, Pin.OUT),
                    dc=Pin(6, Pin.OUT),
                    cs=Pin(7, Pin.OUT),
                    backlight=Pin(8, Pin.OUT),
                    rotation=0) 

ow = onewire.OneWire(Pin(4, Pin.PULL_UP))
ds = ds18x20.DS18X20(ow)
rom = ds.scan()
rom_id = rom[0]
print(rom_id)

tft.text(font, "hzcu", 10, 0, st7789.WHITE, st7789.BLACK)


def read_temp(tim):
    ds.convert_temp()
    temp = ds.read_temp(rom_id)

    tft.text(font, "temp: {:.2f}C".format(temp), 10, 40, st7789.WHITE,
             st7789.BLACK)
    print("temp: {:.2f}C".format(temp))


tim = Timer(0)
tim.init(period=1000, mode=Timer.PERIODIC, callback=read_temp)
