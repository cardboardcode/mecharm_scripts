#!/usr/bin/python

from pymycobot.mycobot import MyCobot
from pymycobot import PI_PORT, PI_BAUD
import time


mycobot = MyCobot('/dev/ttyAMA0', 1000000)

def release_servos():
    mycobot.release_all_servos()

if __name__ == '__main__':
    print("[ moving_to_stretch ] - Initializing")
    release_servos()
    print("[ moving_to_stretch ] - COMPLETED. Exiting...")

