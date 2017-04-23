#!/usr/bin/env python

"""Simple example showing how to get mouse events."""
from __future__ import print_function
import evdev

#import struct

"""
Underlying C structs:

//from /usr/include/linux/types.h
typedef __kernel_long_t __kernel_time_t;
typedef __kernel_long_t __kernel_suseconds_t; //assumption

//from /usr/include/linux/time.h
struct timeval {
	__kernel_time_t		tv_sec;		/* seconds */
	__kernel_suseconds_t	tv_usec;	/* microseconds */
};

//from /usr/include/linux/input.h
struct input_event {
	struct timeval time;
	__u16 type;
	__u16 code;
	__s32 value;
};
"""

#EVENT_FORMAT = str('llHHi')
#EVENT_SIZE = struct.calcsize(EVENT_FORMAT)
#FILENAME = '/dev/input/event10'

import argparse
parser = argparse.ArgumentParser(description='Python quick test to evaluate 3dof position tracking in a 2D plane using 2 computer mice.')
parser.add_argument('-r', '--right', default='/dev/input/event0', help='right mouse device node')
parser.add_argument('-l', '--left', default='/dev/input/event1', help='left mouse device node')
args = parser.parse_args()

rightmouse = evdev.InputDevice(args.right)
leftmouse = evdev.InputDevice(args.left)

def parse_xyevents(mouse):
	x = 0
	y = 0
	while 1:
		event = mouse.read_one()
		if(event):
			if(event.code == evdev.ecodes.REL_X):
				x += event.value
			if(event.code == evdev.ecodes.REL_Y):
				y += event.value
			if(event.code == evdev.ecodes.SYN_REPORT):
				break
	return (x, y)

if __name__ == "__main__":
	while 1:
		print(parse_xyevents(leftmouse), parse_xyevents(rightmouse))