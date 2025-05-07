import RPi.GPIO as gpio
import time
import numpy as np
import matplotlib.pyplot as plt

dac = [8, 11, 7, 1, 0, 5, 12, 6]
leds = [2, 3, 4, 17, 27, 22, 10, 9]
comp = 14
troyka = 13
dt = 0.005

gpio.setmode(gpio.BCM)
gpio.setup(dac, gpio.OUT)
gpio.setup(leds, gpio.OUT, initial=gpio.LOW)
gpio.setup(troyka, gpio.OUT)
gpio.setup(comp, gpio.IN)

def decimal2binary(value):
    return [int(bit) for bit in format(value, 'b').zfill(8)]

def to_dac(value):
    signal = [int(bit) for bit in format(value, 'b').zfill(8)]
    gpio.output(dac, signal)
    time.sleep(dt)

def to_leds(value):
    signal = [int(bit) for bit in format(value, 'b').zfill(8)]
    gpio.output(leds, signal)
    time.sleep(dt)

def adc():

    value = 128
    signal = [int(bit) for bit in format(value, 'b').zfill(8)]
    gpio.output(dac, signal)
    time.sleep(dt)
    if gpio.input(comp) == 1:
        value -= 128

    value += 64
    signal = [int(bit) for bit in format(value, 'b').zfill(8)]
    gpio.output(dac, signal)
    time.sleep(dt)
    if gpio.input(comp) == 1:
        value -= 64

    value += 32
    signal = [int(bit) for bit in format(value, 'b').zfill(8)]
    gpio.output(dac, signal)
    time.sleep(dt)
    if gpio.input(comp) == 1:
        value -= 32

    value += 16
    signal = [int(bit) for bit in format(value, 'b').zfill(8)]
    gpio.output(dac, signal)
    time.sleep(dt)
    if gpio.input(comp) == 1:
        value -= 16

    value += 8
    signal = [int(bit) for bit in format(value, 'b').zfill(8)]
    gpio.output(dac, signal)
    time.sleep(dt)
    if gpio.input(comp) == 1:
        value -= 8

    value += 4
    signal = [int(bit) for bit in format(value, 'b').zfill(8)]
    gpio.output(dac, signal)
    time.sleep(dt)
    if gpio.input(comp) == 1:
        value -= 4

    value += 2
    signal = [int(bit) for bit in format(value, 'b').zfill(8)]
    gpio.output(dac, signal)
    time.sleep(dt)
    if gpio.input(comp) == 1:
        value -= 2

    value += 1
    signal = [int(bit) for bit in format(value, 'b').zfill(8)]
    gpio.output(dac, signal)
    time.sleep(dt)
    if gpio.input(comp) == 1:
        value -= 1

    return value

try:
    data = []
    start_time = time.time()
    gpio.output(troyka, gpio.HIGH)
    voltage = 0
    while voltage < 2.64:
        val = adc()
        voltage = val * 3.3 / 256
        data.append(voltage)

    gpio.output(troyka, gpio.LOW)
    while voltage > 2.17:
        val = adc()
        voltage = val * 3.3 / 256
        data.append(voltage)

    finish_time = time.time()
    duration = finish_time - start_time #Общая продолжительность эксперимента
    n = len(data) #количество измерений
    sample_rate = n / duration #частота дискретизации
    T = duration / n #период одного измерения
    step = 3.3 / 256 #шаг квантования
    plt.plot(np.array(data))
    plt.savefig("picture.png")

    with open('data.txt', 'w') as file:
        for data_el in data:
            file.write(str(data_el) + '\n')
        file.close()

    with open('settings.txt', 'w') as file:
        file.write(str(sample_rate) + '\n')
        file.write(str(step))
        file.close() 

    print("Общая продолжительность эксперимента: {:.2f}с.".format(duration))
    print("Период одного измерения: {:.2f}с.".format(T))
    print("Средняя частота дискретизации проведённых измерений: {:.2f}Гц.".format(sample_rate))
    print("Шаг квантования АЦП: {:.4f}В.".format(step))
except KeyboardInterrupt:
    gpio.cleanup()

finally:
    gpio.output(dac, 0)
    gpio.output(leds, 0)
    gpio.cleanup()
