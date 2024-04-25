from machine import Pin, SoftSPI
import st7789py
import time
import vga1_16x32 as font

# 此处sck对应屏幕SCK所接的开发板的GPIO2脚，mosi对应屏幕SDA所接的开发板的GPIO3脚
spi = SoftSPI(baudrate=80000000,
              polarity=0,
              sck=Pin(2, Pin.OUT),
              mosi=Pin(3, Pin.OUT),
              miso=Pin(8))
# 此处reset对应屏幕RES所接的开发板的GPIO1脚，dc对应屏幕DC所接的开发板的GPIO6脚
tft = st7789py.ST7789(spi,
                      240,
                      240,
                      reset=Pin(10, Pin.OUT),
                      dc=Pin(6, Pin.OUT),
                      cs=Pin(7, Pin.OUT),
                      backlight=Pin(8, Pin.OUT),
                      rotation=0)  # rotation 方向0-3方位
tft.fill(st7789py.color565(256, 0, 0))


def main():
    tft.text(font, "Welcome China!", 0, 108, st7789py.color565(0, 0, 0),
             st7789py.color565(255, 255, 255))
    print("Welcome China!")
    while True:
        pass


if __name__ == "__main__":
    main()
