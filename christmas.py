import board
import digitalio as dio
import time
import neopixel
import random

num_pixels = 30
np = neopixel.NeoPixel(board.A7, num_pixels, brightness=1, auto_write=False)

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
magenta = (255, 0, 255)
yellow = (255, 255, 0)
white = (255, 255, 255)
color = (red, green, blue, magenta, yellow)
thing  = (red, white)

def middle(hue, stop):
    color = hue
    for i in range(0, num_pixels/2, 1):
        np[i] = color[i%len(color)]
        np.show()
        time.sleep(stop)
        np[num_pixels - 1 - i] = color[i%len(color) - 1]
        np.show()
        time.sleep(stop)
    for i in range(num_pixels):
        np[i] = (0, 0, 0)
        np.show()
        time.sleep(stop)
        np[num_pixels - 1 - i] = (0, 0, 0)
        np.show()
        time.sleep(stop)

    """
    for i in range(num_pixels):
        np[i] = color[i%len(color) - 1]
        np.show()
        time.sleep(stop)
    """

while True:
    middle(color, .01)
