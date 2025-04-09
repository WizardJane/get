#2-2-bin-number.py

import RPi.GPIO as gpio 
import time

dac = [26, 19, 13, 6, 5, 11, 9, 10]
num = []

gpio.setmode(gpio.BCM)

gpio.setup(dac, gpio.OUT)

#num = [0, 1] * 4
#num = [0, 0, 0, 0, 0, 0, 1, 0] #2
#num = [1, 1, 1, 1, 1, 1, 1, 1] #255
#num = [0, 1, 1, 1, 1, 1, 1, 1] #127
#num = [0, 1, 0, 0, 0, 0, 0, 0] #64
#num = [0, 0, 1, 0, 0, 0, 0, 0] #32
#num = [0, 0, 0, 0, 0, 1, 0, 1] #5
num = [0, 0, 0, 0, 0, 0, 0, 0] #0

gpio.output(dac, num)
#time.sleep(15)
gpio.output(dac, 0)
gpio.cleanup()


