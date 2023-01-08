#!/usr/bin/python

import curses
from pymycobot.mycobot import MyCobot
from pymycobot import PI_PORT, PI_BAUD
import time

def print_index_pos(index_pos):
    screen.addstr(3,0, "[ " + str(index_pos[0]) + ", " + str(index_pos[1]) + ", " + str(index_pos[2]) + ", " + str(index_pos[3]) + ", " + str(index_pos[4]) + ", " + str(index_pos[5]) + " ]")

# Connect to MechARM via serial comms
mycobot = MyCobot('/dev/ttyAMA0', 1000000)

# get the curses screen window
screen = curses.initscr()

screen.addstr(0, 0, "[A, B, C, D, E, F] - [t-y, g-h, v-b, u-i, j-k, n-m ]")
screen.addstr(1, 0, "[GRIPPER-CLOSE, GRIPPER-OPEN] - [d,f]")
screen.addstr(2, 0, "[ q ] - QUIT")
# turn off input echoing
curses.noecho()

# respond to keys immediately (don't wait for enter)
curses.cbreak()

# map arrow keys to special values
screen.keypad(True)

# Print current angle positions:
str1 = "[ "
index_pos = mycobot.get_angles()
for index in range(0, len(index_pos)):
    if index == (len(index_pos) - 1):
        str1 = str1 + str(index_pos[index])
    else:
        str1 = str1 + str(index_pos[index]) + ", "

str1 = str1 + " ]"
screen.addstr(3, 0, str1)
move_delay = 0
move_gradient = 5

try:
    while True:
        char = screen.getch()
        if char == ord('q'):
            break
        elif char == ord('t'):
            index_pos[0] = index_pos[0] - move_gradient
            print_index_pos(index_pos)
            mycobot.wait(move_delay).send_angles(index_pos, 50)
        elif char == ord('y'):
            index_pos[0] = index_pos[0] + move_gradient
            print_index_pos(index_pos)
            mycobot.wait(move_delay).send_angles(index_pos, 50)
        elif char == ord('g'):
            index_pos[1] = index_pos[1] + move_gradient
            print_index_pos(index_pos)
            mycobot.wait(move_delay).send_angles(index_pos, 50)
        elif char == ord('h'):
            index_pos[1] = index_pos[1] - move_gradient
            print_index_pos(index_pos)
            mycobot.wait(move_delay).send_angles(index_pos, 50)
        elif char == ord('v'):
            index_pos[2] = index_pos[2] - move_gradient
            print_index_pos(index_pos)
            mycobot.wait(move_delay).send_angles(index_pos, 50)
        elif char == ord('b'):
            index_pos[2] = index_pos[2] + move_gradient
            print_index_pos(index_pos)
            mycobot.wait(move_delay).send_angles(index_pos, 50)
        elif char == ord('u'):
            index_pos[3] = index_pos[3] + move_gradient
            print_index_pos(index_pos)
            mycobot.wait(move_delay).send_angles(index_pos, 50)
        elif char == ord('i'):
            index_pos[3] = index_pos[3] - move_gradient
            print_index_pos(index_pos)
            mycobot.wait(move_delay).send_angles(index_pos, 50)
        elif char == ord('j'):
            index_pos[4] = index_pos[4] - move_gradient
            print_index_pos(index_pos)
            mycobot.wait(move_delay).send_angles(index_pos, 50)
        elif char == ord('k'):
            index_pos[4] = index_pos[4] + move_gradient
            print_index_pos(index_pos)
            mycobot.wait(move_delay).send_angles(index_pos, 50)
        elif char == ord('n'):
            index_pos[5] = index_pos[5] + move_gradient
            print_index_pos(index_pos)
            mycobot.wait(move_delay).send_angles(index_pos, 50)
        elif char == ord('m'):
            index_pos[5] = index_pos[5] - move_gradient
            print_index_pos(index_pos)
            mycobot.wait(move_delay).send_angles(index_pos, 50)
        elif char == ord('d'):
            mycobot.set_gripper_value(0, 100)
        elif char == ord('f'):
            mycobot.set_gripper_value(100, 100)
        elif char == ord('1'):
            c = mycobot.get_coords()
            c[4] = c[4] - 10
            mycobot.send_coords(c, 10, 0)
        elif char == ord('2'):
            c = mycobot.get_coords()
            c[4] = c[4] + 10
            mycobot.send_coords(c, 10, 0)
        elif char == ord('3'):
            c = mycobot.get_coords()
            c[5] = c[5] - 10
            mycobot.send_coords(c, 10, 0)
        elif char == ord('4'):
            c = mycobot.get_coords()
            c[5] = c[5] + 10
            mycobot.send_coords(c, 10, 0)
        elif char == curses.KEY_RIGHT:
            # print doesn't work with curses, use addstr instead
            screen.addstr(3, 0, 'right')
        elif char == curses.KEY_LEFT:
            screen.addstr(3, 0, 'left ')
        elif char == curses.KEY_UP:
            screen.addstr(3, 0, 'up   ')
        elif char == curses.KEY_DOWN:
            screen.addstr(3, 0, 'down ')
finally:
    # shut down cleanly
    curses.nocbreak()
    screen.keypad(0)
    curses.echo()
    curses.endwin()
