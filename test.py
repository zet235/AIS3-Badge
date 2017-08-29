#!/usr/bin/env python
# -*- coding: utf-8 -*-

import serial, time, platform

os_version = platform.system()

if os_version == "Darwin":
    ser = serial.Serial('/dev/tty.SLAB_USBtoUART', 115200, timeout=1)
elif os_version == "Windows":
    ser = serial.Serial('COM3', 115200, timeout=1)
elif os_version == "Linux":
    ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=1)


#ser.write('\xde\xad\xbe\xef')
ser.write('s')
ser.readline()
print ser.readline()
