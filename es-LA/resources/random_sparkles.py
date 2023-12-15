from sense_hat import SenseHat
from random import randint
from time import sleep

sensor = SenseHat()

while True:
    x = randint(0, 7)
    y = randint(0, 7)
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    sensor.set_pixel(x, y, r, g, b)
    sleep(0.01)
