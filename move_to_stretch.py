#!/usr/bin/python

from pymycobot.mycobot import MyCobot
from pymycobot import PI_PORT, PI_BAUD
import time


mycobot = MyCobot('/dev/ttyAMA0', 1000000)

def move_to_home():
    mycobot.wait(1).sync_send_angles([ 0.17, 0.17, 0.7, 0.26, -0.35, -4.900000000000006 ], 30)

if __name__ == '__main__':
    print("[ moving_to_stretch ] - Initializing")
    move_to_home()
    print("[ moving_to_stretch ] - COMPLETED. Exiting...")

