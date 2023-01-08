#!/usr/bin/python

from pymycobot.mycobot import MyCobot
from pymycobot import PI_PORT, PI_BAUD
import time


mycobot = MyCobot('/dev/ttyAMA0', 1000000)

def move_to_home():
    mycobot.wait(1).sync_send_angles([-78.48, -34.98, -45.17, -1.84, 82.17, 108.36], 30)

if __name__ == '__main__':
    print("[ moving_to_faceme ] - Initializing")
    move_to_home()
    print("[ moving_to_faceme ] - COMPLETED. Exiting...")

