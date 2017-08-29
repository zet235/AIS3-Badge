# AIS3 BLE Lab

```
       ___       ____   _____    _____
      /   |     /  _/  / ___/   |__  /
     / /| |     / /    __      /_ <
    / ___ |   _/ /    ___/ /   ___/ /
   /_/  |_|  /___/   /____/   /____/

*****************************************
            AIS3 IoT Security
          By Prof. Shi-Cho, Cha
    AIS3 Badge by power Li, idic, Zet
*****************************************

 Available Command:
 'k' Change HMAC Key
 'b' Change Advertisement Data
 'h' Show This Help
 'Press X Key' Enter Central Mode
 'Press Y Key' Enter Perpherial Mode

  You have to send command in 100ms
  Maximum input length is 40 bytes

  Button Layout:
   ____________________________________________
  |            [UP]                   [Y]      |
  |   [LEFT] [CENTER] [RIGHT]       [X] [B]    |
  |           [DOWN]                  [A]      |
  |                                            |
  |    {USR_LED}          [USR] [RST]          |
  |____________________________________________|
```


**chat room** : [tlk.io/ais3_2017_ble](https://tlk.io/ais3_2017_ble)

**Environment** :

- driver : [CP210x USB to UART](https://www.silabs.com/products/development-tools/software/usb-to-uart-bridge-vcp-drivers)
- serial package for python2.7 : [pyserial](https://pypi.python.org/pypi/pyserial/2.7)
- `exp` directory include pyserial if you don't want to use pip to install, you can `cd` to exp directory and run python script

**How to connect**

- rate baud : `115200`
- Windows `COM3` 
  > Check your Device Manager COM port
- Linux `/dev/ttyUSB0`
- macOS `/dev/tty.SLAB_USBtoUART`

you can run `test.py` to test

## challenge

**challenge 1 :**

``` diff
#---------------------------------------------------------------------------------------------
#| 00 | 01 | 02 | 03 |  04 | 05 |  06 | 07 |  08 | 09 |  10 |   11 |  12 |   13 |  14 |   15 |
#---------------------------------------------------------------------------------------------
#|  L |  T | 46 | 00 | ID1 | R1 | ID2 | R2 | ID3 | R3 | ID4 | SIG1 | ID5 | SIG2 | ID6 | SIG3 |
#---------------------------------------------------------------------------------------------
```

> ID   : your name  (6 bytes)  
R    : random (3 bytes)  
key  : random (3 bytes) + count (1 byte) + count shift 8 (1 byte) + count shift 16 (1 byte)  
SIG  : hmac out put (use ID to be the message)  
SIG1 : SIG first byte  
SIG2 : SIG second byte  
SIG3 : SIG thired byte  


**challenge 3  :**

```diff
#--------------------------------------------------------------
#| 00 | 01 | 02 | 03 |  04 |  05 |  06 |  07 |  08 |  09 |  10 |
#--------------------------------------------------------------
#|  L |  T | 46 | 00 | ID1 | ID2 | ID3 | ID3 | ID4 | ID5 | ID6 |
#--------------------------------------------------------------
```

> send ID and key(name + some string in challenge3.apk)

**exploit is python2 version**

## thanks

power Li@NTUST

idic@NTUST

> More Info: https://github.com/x43x61x69/HITCON-Badge