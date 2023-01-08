#!/usr/bin/python

from pymycobot.mycobot import MyCobot
from pymycobot import PI_PORT, PI_BAUD
import time


mycobot = MyCobot('/dev/ttyAMA0', 1000000)

def move_to_reset():
    mycobot.wait(1).sync_send_angles([0, 0, 0, 0, 0, 0], 50)

if __name__ == '__main__':
    print("[ moving_to_reset ] - Initializing")
    move_to_reset()
    print("[ moving_to_reset ] - COMPLETED. Exiting...")
        

