#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf8')

import time
import datetime
import serial

useraccountid = ''
geigercounterid = ''

device = "GQ_GMC_320E_plus"     # name of your device
port = "/dev/ttyUSB0"
baud = 115200

from gmc320 import getCPM
from gmc320 import getVOLT
from gmc320 import getTEMP

ser = serial.Serial(port, baud)

cpm = getCPM(ser)

data = { 
                    'rad_cpm' :       cpm, 
                    'rad_nsvh' :      cpm * 6.5 / 1000,
                    'voltage_V' :     getVOLT(ser),
                    'temperature_C' : getTEMP(ser)
                }
                
print "{:<10} {:<10} {:<10} {:<10}".format(data['rad_cpm'],data['rad_nsvh'],data['voltage_V'],data['temperature_C'])
import urllib2
urllib2.urlopen('http://www.gmcmap.com/log2.asp?AID='+useraccountid+'&GID='+geigercounterid+'&CPM='+str(data['rad_cpm'])+'&uSV='+str(data['rad_nsvh']))
 

ser.close()

f = open("/var/www/html/index.html", "w")
f.write("<html><body>")
f.write("<label for=""cpm"">CPM:"+str(data['rad_cpm'])+"</label>")
f.write("<meter id=""cpm"" value="+str(data['rad_cpm'])+" min=""5"" max=""50"">"+str(data['rad_cpm'])+"</meter>")
f.write("<br/><a href=""https://www.gmcmap.com/historyData.asp?Param_ID="+geigercounterid+""+">History</a>")
f.write("</html></body>")
f.close()


exit()
