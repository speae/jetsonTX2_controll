import time

import RPi.GPIO as GPIO

led_pin = 29
sec = 5

# setting
GPIO.setmode(GPIO.BOARD)
GPIO.setup(led_pin, GPIO.OUT)
GPIO.output(led_pin, True)
time.sleep(5)
GPIO.output(led_pin, False)
GPIO.cleanup(led_pin)
