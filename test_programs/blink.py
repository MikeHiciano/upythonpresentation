import machine
import time

led = machine.Pin(5,machine.Pin.OUT)

def blinks():
    led.off()
    time.sleep(1)
    led.on()
    time.sleep(1)
