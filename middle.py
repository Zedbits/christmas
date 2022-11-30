import board
import digitalio as dio
import time
import neopixel
import random

num_pixels = 30
np = neopixel.NeoPixel(board.A7, num_pixels, brightness=1, auto_write=False)

"""
Name: middle
Description: This function take a color and pulses it from both ends of the LED strip to the 
middle and then blackens it from the same ends
Parameters: colors(tuple) - This is the RGB value that will be pulsed. stop(floating point) - this will control how fast each pulse is
Return: none
"""
def middle(colors, stop):
    color = colors
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
