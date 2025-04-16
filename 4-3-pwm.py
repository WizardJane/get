import RPi.GPIO as gpio
import time
gpio.setmode(gpio.BCM)

gpio.setup(21, gpio.OUT)
frec = 0.5
p = gpio.PWM(21, frec)


try:
    while True: 
        try:
            n = input("Введите duty cycle в диапозоне от 0 до 100: ")
            n = float(n)
            if n < 0 or n > 100:
                print("Число не в диапазоне от 0 до 100")
            else:
                print(3.3 * n / 100)
                duty_cycle = n
                p.start(duty_cycle)
                input("Press return to stop")
                p.stop()
        except ValueError:
            print("Нечисловое значeние")
finally:
    gpio.cleanup()