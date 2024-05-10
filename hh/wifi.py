import network, time
from machine import Pin

LED_GREEN = 19 #绿灯
LED_on = 1
LED_off = 0

def wifi_Connect(SSID, PASSWORD):
    wifi_led = Pin(LED_GREEN, Pin.OUT)#wifi连接状态灯
    wlan = network.WLAN(network.STA_IF)#STA模式——连接wifi
    wlan.active(True)
    starttime = time.time()
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect('SSID', 'PASSWORD')
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
        return True
    
    else:
        return False
    
