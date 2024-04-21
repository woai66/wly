# from machine import Pin, SoftI2C
 
# i2c = SoftI2C(sda=Pin(3), scl=Pin(2), freq=100000)
 
# lcdAddr = i2c.scan() # scan for devices
# print(lcdAddr)  # 打印出lcd的地址

# # G2 SCL G3 SDA G1 RES G6 DC
from machine import Pin, SPI
import st7789py as st7789

# 初始化SPI
spi = SPI(1, baudrate=40000000, sck=Pin(2), mosi=Pin(3))

# 初始化LCD
lcd = st7789.ST7789(spi, 240, 240, reset=Pin(1), cs=Pin(5), dc=Pin(6))

# 清屏
lcd.fill(st7789.BLACK)

# 显示文本
lcd.text("Hello, World!", 10, 10, st7789.WHITE)

# 刷新显示
lcd.show()
