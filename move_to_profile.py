#!/usr/bin/python

from pymycobot.mycobot import MyCobot
from pymycobot import PI_PORT, PI_BAUD
import time


mycobot = MyCobot('/dev/ttyAMA0', 1000000)

def move_to_home():
    mycobot.wait(1).sync_send_angles([-47.62, -24.43, -59.5, -2.54, -32.34, -2.1799999999999997], 30)

if __name__ == '__main__':
    print("[ moving_to_profile ] - Initializing")
    move_to_home()
    print("[ moving_to_profile ] - COMPLETED. Exiting...")

