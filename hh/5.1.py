import network, time
from machine import Pin, SoftSPI
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
                    rotation=0)  # rotation 方向0-3方位
LED_GREEN = 19 #绿灯
LED_on = 1
LED_off = 0

def wifi_Connect():
    wifi_led = Pin(LED_GREEN, Pin.OUT)#wifi连接状态灯
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    starttime = time.time()
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect("1234zyq", "mimashishenme")
        while not wlan.isconnected():
            wifi_led.value(LED_on)
            time.sleep(0.3) 
            wifi_led.value(LED_off)
            time.sleep(0.3)

            if time.time() - starttime > 15:
                print('connect timeout!')
                break
    if wlan.isconnected():
        wifi_led.value(LED_on)
        print('network config:', wlan.ifconfig())

    
    tft.text(font, "IP:", 20, 0, st7789.WHITE,st7789.BLACK)
    tft.text(font,"{}".format(wlan.ifconfig()[0]), 20, 30, st7789.WHITE)
    tft.text(font, "ZiWangYanMa:", 20, 60, st7789.WHITE, st7789.BLACK)
    tft.text(font, "{}".format(wlan.ifconfig()[1]), 20, 90, st7789.WHITE)
    tft.text(font, "WangGuan:", 20, 120, st7789.WHITE, st7789.BLACK)
    tft.text(font, "{}".format(wlan.ifconfig()[2]), 20, 150, st7789.WHITE)
    

    
wifi_Connect();
