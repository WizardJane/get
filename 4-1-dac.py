import RPi.GPIO as gpio
gpio.setmode(gpio.BCM)

dac = [8, 11, 7, 1, 0, 5, 12, 6]
gpio.setup(dac, gpio.OUT)

def decimal2binary(value):
    return [int(bit) for bit in format(value, 'b').zfill(8)]


try:
    try:
        n = input("Введите число от 0 до 255: ")
        n = int(n)

        if n < 0:
            print("Число меньше 0")
        elif n > 255:
            print("Число больше 255")
        else:
            gpio.output(dac, decimal2binary(n))
            print("U =", n * 3.3 / 256)

    except ValueError:
        try:
            n = float(n)
            print("Нецелое число")
        except ValueError:
            print("Нечисловое значeние")
        
except KeyboardInterrupt:
    gpio.cleanup()
finally:
    gpio.output(dac, 0)
    gpio.cleanup()
    
    
