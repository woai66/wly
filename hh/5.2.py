import wifi
import ntptime
import time
from machine import Pin, SoftSPI, Timer,I2C,RTC
import st7789py as st7789
from romfonts import vga1_16x32 as font


SSID = "1234zyq"
PASSWORD ="mimashishenme"

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

week = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
timelist = ['','','']

rtc = RTC() #rtc初始化

wifi_Connect = wifi.WIFI_Connect(SSID, PASSWORD)

timezone = 8
ntptime.host = 'ntp.aliyun.com'
print('before time:%s' % str(time.localtime()))
tampon2 = time.time()
#RTC时间设置
rtc.datetime(time.localtime(tampon2)[0:3] + (0,) + time.localtime(tampon2)[3:6]+ (0,))

def RTC_RUN(tim):
    datetime = rtc.datetime()#获取当前时间
    tft.text(font, "WYLZYQ", 80, 0, st7789.WHITE, st7789.BLACK)
    tft.text(font, 'ntp clock:', 0, 40, st7789.WHITE, st7789.BLACK)

    datestr = '{:s}-{:s}-{:s} {:s}'.format(str(datetime[0]), str(datetime[1]), str(datetime[2]), week[datetime[3]])
    tft.text(font, datestr, 0, 80, st7789.WHITE, st7789.BLACK)

    timestr = '{:02d}:{:02d}:{:02d}'.format(datetime[4], datetime[5], datetime[6])
    tft.text(font, timestr, 0, 120, st7789.WHITE, st7789.BLACK)

tim = Timer(0)
tim.init(period=500, mode=Timer.PERIODIC, callback=RTC_RUN)