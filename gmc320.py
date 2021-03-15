#!/usr/bin/python
# -*- coding: UTF-8 -*-

def getVER(ser):
    ser.write(b'<GETVER>>')
    rec = ser.read(14)   
    return rec

def getCPM(ser):
    ser.write(b'<GETCPM>>')
    rec = ser.read(2)
    return ord(rec[0])<< 8 | ord(rec[1])
    
def getVOLT(ser):
    ser.write(b'<GETVOLT>>')
    rec = ser.read(1)
    return ord(rec)/10.0 

def getCFG(ser):
    ser.write(b'<GETCFG>>')
    rec = ser.read(256)    
    cfg = []
    for i in range(0,256):
        cfg.append(ord(rec[i]))
    return cfg

def getSERIAL(ser):
    ser.write(b'<GETSERIAL>>')
    a = ser.read(7)
    hexlookup = "0123456789ABCDEF"    
    rec =""
    for i in range(0,7):    
        n1   = ((ord(a[i]) & 0xF0) >>4)
        n2   = ((ord(a[i]) & 0x0F))
        rec += hexlookup[n1] + hexlookup[n2]
    return rec

def getDATETIME(ser):
    ser.write(b'<GETDATETIME>>')
    dt = ser.read(7)
    idt = []
    for i in range(0,6):
        idt.append( ord(dt[i]))
    idt[0] += 2000
    return datetime.datetime(idt[0], idt[1], idt[2], idt[3],idt[4],idt[5])

def getTEMP(ser):
    ser.write(b'<GETTEMP>>')
    rec = ser.read(4)
    signe = "+"
    if ord(rec[2]) != 0:
        signe = "-"
    temp = signe + str(ord(rec[0])) + "." + str(ord(rec[1]))
    return temp
    
def getGYRO(ser):
    ser.write(b'<GETGYRO>>')
    rec = ser.read(7)
    return rec
    
