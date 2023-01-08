#!/usr/bin/python

from pymycobot.mycobot import MyCobot
from pymycobot import PI_PORT, PI_BAUD
import time


mycobot = MyCobot('/dev/ttyAMA0', 1000000)

def move_to_home():
    mycobot.wait(1).sync_send_angles([0.870, 81.65, 67.93, -87.45, -87.97, 20.47], 50)

if __name__ == '__main__':
    print("[ moving_to_home ] - Initializing")
    move_to_home()
    print("[ moving_to_home ] - COMPLETED. Exiting...")
        

