import RPi.GPIO as gpio
import time

dac = [26, 19, 13, 6, 5, 11, 9, 10]
comp = 4
troyka = 17

gpio.setmode(gpio.BCM)
gpio.setup(dac, gpio.OUT)
gpio.setup(troyka, gpio.OUT, initial=gpio.HIGH)
gpio.setup(comp, gpio.IN)

def decimal2binary(value):
    return [int(bit) for bit in format(value, 'b').zfill(8)]

def to_dac(value):
    signal = [int(bit) for bit in format(value, 'b').zfill(8)]
    gpio.output(dac, signal)
    time.sleep(0.01)

def adc():
    value = 0

    value += 128
    signal = [int(bit) for bit in format(value, 'b').zfill(8)]
    gpio.output(dac, signal)
    time.sleep(0.01)
    if gpio.input(comp) == 0:
        value -= 128

    value += 64
    signal = [int(bit) for bit in format(value, 'b').zfill(8)]
    gpio.output(dac, signal)
    time.sleep(0.01)
    if gpio.input(comp) == 0:
        value -= 64

    value += 32
    signal = [int(bit) for bit in format(value, 'b').zfill(8)]
    gpio.output(dac, signal)
    time.sleep(0.01)
    if gpio.input(comp) == 0:
        value -= 32

    value += 16
    signal = [int(bit) for bit in format(value, 'b').zfill(8)]
    gpio.output(dac, signal)
    time.sleep(0.01)
    if gpio.input(comp) == 0:
        value -= 16

    value += 8
    signal = [int(bit) for bit in format(value, 'b').zfill(8)]
    gpio.output(dac, signal)
    time.sleep(0.01)
    if gpio.input(comp) == 0:
        value -= 8

    value += 4
    signal = [int(bit) for bit in format(value, 'b').zfill(8)]
    gpio.output(dac, signal)
    time.sleep(0.01)
    if gpio.input(comp) == 0:
        value -= 4

    value += 2
    signal = [int(bit) for bit in format(value, 'b').zfill(8)]
    gpio.output(dac, signal)
    time.sleep(0.01)
    if gpio.input(comp) == 0:
        value -= 2

    value += 1
    signal = [int(bit) for bit in format(value, 'b').zfill(8)]
    gpio.output(dac, signal)
    time.sleep(0.01)
    if gpio.input(comp) == 0:
        value -= 1

    # for i in range(7, -1, -1):
    #     value += deg
    #     signal = decimal2binary(value)
    #     gpio.output(dac, signal)
    #     time.sleep(0.01)
    #     comp_value = gpio.input(comp)
    #     if comp_value == 0:
    #         value -= deg
    #     deg //= 2
    return value

try:
    while True:
        t1 = time.time()
        val = adc()
        t2 = time.time()
        voltage = val / 256 * 3.3
        print("Value: {:.2f}, voltage: {:.2f}, time: {:.5f}".format(val, voltage, t2 - t1))

except KeyboardInterrupt:
    gpio.cleanup()

finally:
    gpio.output(dac, 0)
    gpio.cleanup()
