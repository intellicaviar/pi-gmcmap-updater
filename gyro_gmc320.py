#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf8')

import time
import datetime
import serial

device = "GQ_GMC_320E_plus"     # name of your device
port = "/dev/ttyUSB0"
baud = 115200

from gmc320 import getGYRO
    
ser = serial.Serial(port, baud)

print getGYRO(ser)

ser.close()
exit()