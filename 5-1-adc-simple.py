import RPi.GPIO as gpio
import time

dac = [26, 19, 13, 6, 5, 11, 9, 10]
leds = [21, 20, 16, 12, 7, 8, 25, 24][::-1]

comp = 4
troyka = 17

gpio.setmode(gpio.BCM)
gpio.setup(dac, gpio.OUT)
gpio.setup(troyka, gpio.OUT, initial=gpio.HIGH)
gpio.setup(comp, gpio.IN)
gpio.setup(leds, gpio.OUT)


def decimal2binary(value):
    return [int(bit) for bit in format(value, 'b').zfill(8)]

def adc():
    for value in range(256):
        signal = decimal2binary(value)
        gpio.output(dac, signal)
        time.sleep(0.01)
        comp_value = gpio.input(comp)
        #print(signal, comp_value)
        if comp_value == 0:
            return value
    return 0

try:
    while True:
    #for i in range(100):
        # t1 = time.time()
        # val = adc()
        # t2 = time.time()
        # voltage = val / 256 * 3.3
        # print("Value: {:.2f}, voltage: {:.2f}, time: {:.2f}".format(val, voltage, t2 - t1))
        val = adc()
        #val = (val // (256 // 8))
        voltage = val / 256 * 3.3
        val = round((val / 43) * 8)
        for i in range(8):
            if val > i:
                gpio.output(leds[i], 1)
            else:
                gpio.output(leds[i], 0)
        print("Value: {:.2f}, voltage: {:.2f}".format(val, voltage))

except KeyboardInterrupt:
    gpio.cleanup()

finally:
    gpio.output(dac, 0)
    gpio.cleanup()
