#!/usr/bin/env python
# -*- coding: utf-8 -*-
import serial, time
import hmac, hashlib

def exp(i):
    ser = serial.Serial('/dev/tty.SLAB_USBtoUART', 115200, timeout=1)

    #---------------------------------------------------------------------------------------------
    #| 00 | 01 | 02 | 03 |  04 | 05 |  06 | 07 |  08 | 09 |  10 |   11 |  12 |   13 |  14 |   15 |
    #---------------------------------------------------------------------------------------------
    #|  L |  T | 46 | 00 | ID1 | R1 | ID2 | R2 | ID3 | R3 | ID4 | SIG1 | ID5 | SIG2 | ID6 | SIG3 |
    #---------------------------------------------------------------------------------------------

    company_name = "\x46\x00"
    name = "AIS666"
    random_num = [0x01, 0x02, 0x03]
    count = i

    ser.write("b" + payload)
    ser.readline()
    print "[+] " + ser.readline()
    time.sleep(4)


for i in range(0,1000):
    exp(i)

