# main.py -- put your code here!
import pyb
import os
pyb.LED(2).on()
try:
    s=os.stat('/sd/log.txt')
    os.remove('/sd/log.txt')
    print("Del file ok!")
    pyb.LED(2).off()
except OSError:
    pyb.LED(3).on()