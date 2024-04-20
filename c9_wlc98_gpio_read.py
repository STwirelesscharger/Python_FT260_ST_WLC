import driver_ft260
from wlc98_register import *
import time
wlc98 = driver_ft260.ft260_dongle()
wlc98.chip_info()
print("example code set gpio pin as input floating and read gpio status")
print("connect external 1.8V to GPIO1")
wlc98.write16(I2CREG_GPIO0_FUNC,GPIO_FUNC_IN_FL)
wlc98.write16(I2CREG_GPIO1_FUNC,GPIO_FUNC_IN_FL)

value = wlc98.wreadFA(HWREG_GPIO_INPUT_VAL_RegAddr)
print(f"gpio input value 0x{value:X}")
if(value & 0x01):
    print("gpio0 input high")
else:
    print("gpio0 input low")
if(value & 0x02):
    print("gpio1 input high")
else:
    print("gpio1 input low")

# Open FT260 device OK
# [WR],@0x0x10 >> 0x00 0x34 0x31 0x30 0x32 0x35 0x30 0x51 0x14 0x00 0x00 0x00 0x19 0x00 0x19 0x00
# Device ID 0x: 00343130323530511400000019001900
# [WR],@0x0x0 >> 0x62 0x00 0x02 0x00 0x01 0x02 0x54 0x14 0x00 0x00 0x00 0x2C 0x06 0x00 0x02 0x51
# ChipID:0x0062 rev:2 patchid:0x1454 cfgid:0x2C00
# CHIPID_WLC98
# example code set gpio pin as input floating and read gpio status
# connect external 1.8V to GPIO1
# [W],@0x30 >> 0x0
# [W],@0x31 >> 0x0
# R FA @0x2001A01C = 0x3E
# gpio input value 0x3E
# gpio0 input low
# gpio1 input high
