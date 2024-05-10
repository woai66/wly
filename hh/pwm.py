from machine import Pin, PWM
import time

LED_PIN1 = const(18)
LED_PIN2 = const(19)


led1_pwm = PWM(Pin(LED_PIN1), freq=1000, duty=0)
led2_pwm = PWM(Pin(LED_PIN2), freq=1000, duty=0)

while True:
    for i in range(0, 1024):
        led1_pwm.duty(i)
        led2_pwm.duty(1023-i)
        time.sleep_ms(1)
    for i in range(1023, -1, -1):
        led1_pwm.duty(i)
        led2_pwm.duty(1023-i)
        time.sleep_ms(1)