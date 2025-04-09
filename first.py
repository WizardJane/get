import RPi.GPIO as gpio 
import time


gpio.setmode(gpio.BCM)

gpio.setup(14, gpio.OUT)
gpio.output(14, 1)

gpio.setup(15, gpio.IN)
gpio.input(15)
