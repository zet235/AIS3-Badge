#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import time, sys
if (sys.version_info > (3, 0)):
    sys.stdout.write("Sorry not support python 3 ;( \n")
    sys.exit(1)
import serial, hmac, hashlib

ser = serial.Serial('/dev/tty.SLAB_USBtoUART', 115200, timeout=1)

company_name = "\x46\x00"
name = "zet666"
bid = company_name + name
print "bid : " + bid.encode('hex')

ser.write("b" + bid)
time.sleep(0.5)

key = name + "ais3b3"
print "key : " + key.encode('hex')
ser.write("k" + key)

time.sleep(1)