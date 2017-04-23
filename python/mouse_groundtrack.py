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
FILENAME = '/dev/input/event10'
mouse0 = evdev.InputDevice(FILENAME)

def main():
	"""Just print out some event infomation when the mouse is used."""
	x = 0
	y = 0
	while 1:
		event = mouse0.read_one()
		if(event):
			print(evdev.util.categorize(event))
			if(event.code == evdev.ecodes.SYN_REPORT):
				print("mouse0 relative: ", x, y)
				x = 0
				y = 0
			elif(event.code == evdev.ecodes.REL_X):
				x += event.value
			elif(event.code == evdev.ecodes.REL_Y):
				y += event.value
			else:
				print(evdev.util.categorize(event))







if __name__ == "__main__":
    main()
