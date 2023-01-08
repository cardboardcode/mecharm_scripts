#!/usr/bin/python

from pymycobot.mycobot import MyCobot
from pymycobot import PI_PORT, PI_BAUD
import time


mycobot = MyCobot('/dev/ttyAMA0', 1000000)

def close_gripper():
    mycobot.set_gripper_value(0, 100)

if __name__ == '__main__':
    print("[ close_gripper ] - Initializing")
    close_gripper()
    print("[ close_gripper ] - COMPLETED. Exiting...")

