from machine import Timer,Pin
from micropython import const
LEDPIN = const(17)
led = Pin(LEDPIN, Pin.OUT,value=1)
count = 0

def fun(tim):
    global count
    count += 1
    led.value(not led.value())
    print("fun", count)

tim = Timer(-1)
tim.init(period=1000, mode=Timer.PERIODIC, callback=fun)






















from machine import Pin
from micropython import const
import time
LED_GREEN_PIN = const(19)
LED_YELLOW_PIN = const(18)

led_green_pin = Pin(LED_GREEN_PIN, Pin.OUT,value=1)
led_yellow_pin = Pin(LED_YELLOW_PIN, Pin.OUT,value=1)

KEY1pin = const(8)
KEY = Pin(KEY1pin, Pin.IN, Pin.PULL_UP) #构建·按键对象

state = 1 #led状态

def fun(KEY):
    global state
    time.sleep(0.01)
    if KEY.value() == 0:
        state = not state
    
KEY.irq(trigger=Pin.IRQ_FALLING, handler=fun)

LED = [led_green_pin, led_yellow_pin]
while True:
    for led in LED:
        led.value(0)
    time.sleep(0.5)
    for led in LED:
        led.value(1)
    time.sleep(0.5)