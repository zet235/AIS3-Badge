#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import serial, time
import hmac, hashlib

ser = serial.Serial('/dev/tty.SLAB_USBtoUART', 115200, timeout=1)

#--------------------------------------------------------------
#| 00 | 01 | 02 | 03 |  04 | 05 |  06 | 07 |  08 | 09 |  10    |
#--------------------------------------------------------------
#|  L |  T | 46 | 00 | ID1 | ID2 | ID3 | ID3 | ID4 | ID5 | ID6 |
#--------------------------------------------------------------

company_name = "\x46\x00"
name = "aisxxx"
bid = company_name + name
print "bid : " + bid.encode('hex')

ser.write("b" + bid)
time.sleep(0.5)

key = name + "xxxxxx"
print "key : " + key.encode('hex')
ser.write("k" + key)

time.sleep(1)
