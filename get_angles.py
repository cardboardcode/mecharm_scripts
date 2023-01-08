#!/usr/bin/python

from pymycobot.mycobot import MyCobot
from pymycobot import PI_PORT, PI_BAUD
import time
from pymycobot.genre import Coord
import sys

mycobot = MyCobot('/dev/ttyAMA0', 1000000)

def lower_down():
    print("Angle of 6 MechARM Joints are:")
    print(mycobot.get_angles())

if __name__ == '__main__':
    lower_down()

