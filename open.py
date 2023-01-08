#!/usr/bin/python

from pymycobot.mycobot import MyCobot
from pymycobot import PI_PORT, PI_BAUD
import time


mycobot = MyCobot('/dev/ttyAMA0', 1000000)

def open_gripper():
    mycobot.set_gripper_value(100, 100)

if __name__ == '__main__':
    print("[ open_gripper ] - Initializing")
    open_gripper()
    print("[ open_gripper ] - COMPLETED. Exiting...")

