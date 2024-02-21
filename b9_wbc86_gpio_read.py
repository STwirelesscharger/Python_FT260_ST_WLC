import driver_ft260
from wbc86_register import *
import time
wbc86 = driver_ft260.ft260_dongle()
wbc86.chip_info()
print("example code set gpio pin as input floating and read gpio status")
print("connect external 1.8V to GPIO1")

value = wbc86.wreadFA(HWREG_GPIO_INPUT_VAL_RegAddr)
print(f"gpio input value 0x{value:X}")
if(value & 0x01):
    print("gpio0 input high")
else:
    print("gpio0 input low")
if(value & 0x02):
    print("gpio1 input high")
else:
    print("gpio1 input low")


#test log
# Open FT260 device OK
# [WR],@0x0x10 >> 0x00 0x31 0x36 0x30 0x31 0x53 0x36 0x47 0x0B 0x00 0x00 0x00 0x17 0x00 0x33 0x00
# Device ID 0x: 00313630315336470B00000017003300
# [WR],@0x0x0 >> 0x56 0x00 0x02 0x00 0x18 0x01 0x42 0x12 0x00 0x00 0x0D 0x12 0x01 0x04 0x03 0x01
# ChipID:0x0056 rev:2 patchid:0x1242 cfgid:0x120D
# CHIPID_WBC86
# example code set gpio pin as input floating and read gpio status
# connect external 1.8V to GPIO1
# R FA @0x2001A01C = 0x02
# gpio input value 0x2
# gpio0 input low
# gpio1 input high    
