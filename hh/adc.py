from machine import Pin, ADC, Timer

adc = ADC(Pin(0))
adc.atten(ADC.ATTN_11DB)
adc.width(ADC.WIDTH_12BIT)

def adc_test(tim):  # Add the missing parameter "tim" to the function definition
    msg = "{:.2f}".format(adc.read()*3.3/4095)
    print(msg)

tim = Timer(0)
tim.init(period=300, mode=Timer.PERIODIC, callback=adc_test)