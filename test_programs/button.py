import machine

led = machine.Pin(5,machine.Pin.OUT)
button = machine.Pin(4,machine.Pin.IN)

while True:
    if button.value() == True:
        led.on()

    else:
        led.off()
