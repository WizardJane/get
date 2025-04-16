import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)
dac = [8, 11, 7, 1, 0, 5, 12, 6]
gpio.setup(dac, gpio.OUT)

def dec2bin(value):
    return [int(bit) for bit in format(value, 'b').zfill(8)]

try:
    try:
        n = input("Введите период в секундах: ")
        n = float(n)

        if n < 0:
            print("Число меньше 0")
        else:
            T = n #s
            gpio.output(dac, 0)
            while True:
                for i in range(256):
                    gpio.output(dac, dec2bin(i))
                    time.sleep(T/ 2 / 255)

                for i in range(254, 0, -1):
                    gpio.output(dac, dec2bin(i))
                    time.sleep(T/ 2 / 255)

        

    except ValueError:
        print("Нечисловое значeние")
    
except KeyboardInterrupt:
    gpio.output(dac, 0)
    gpio.cleanup()
finally:
    gpio.setmode(gpio.BCM)
    gpio.setup(dac, gpio.OUT)
    gpio.output(dac, 0)
    gpio.cleanup()