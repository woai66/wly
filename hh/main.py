from machine import Pin
from micropython import const
import time
LED_GREEN_PIN = const(19)
LED_YELLOW_PIN = const(18)

led_green_pin = Pin(LED_GREEN_PIN, Pin.OUT,value=1)
led_yellow_pin = Pin(LED_YELLOW_PIN, Pin.OUT,value=1)

LED = [led_green_pin, led_yellow_pin]
while True:
    for led in LED:
        led.value(0)
    time.sleep(0.5)
    for led in LED:
        led.value(1)
    time.sleep(0.5)