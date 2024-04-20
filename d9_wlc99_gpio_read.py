import driver_ft260
from wlc99_register import *


wlc99 = driver_ft260.ft260_dongle(i2c_speed = 100,dev_addr_set = 0x2C)
wlc99.chip_info()
print("example code set gpio pin as input floating and read gpio status")
print("connect external 1.8V to GPIO1")
wlc99.write16(I2CREG_GPIO0_FUNC,GPIO_FUNC_IN_FL)
wlc99.write16(I2CREG_GPIO1_FUNC,GPIO_FUNC_IN_FL)

value = wlc99.wreadFA(HWREG_GPIO_INPUT_VAL_RegAddr)
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
# [WR],@0x0x10 >> 0x00 0x35 0x38 0x30 0x38 0x52 0x36 0x47 0x0D 0x00 0x00 0x00 0x1B 0x00 0x20 0x00
# Device ID 0x: 00353830385236470D0000001B002000
# [WR],@0x0x0 >> 0x63 0x00 0x02 0x00 0x55 0x01 0x60 0x12 0x00 0x00 0x00 0x2C 0x07 0x07 0x00 0x00
# ChipID:0x0063 rev:2 patchid:0x1260 cfgid:0x2C00
# CHIPID_WLC99
# example code set gpio pin as input floating and read gpio status
# connect external 1.8V to GPIO1
# [W],@0x30 >> 0x0
# [W],@0x31 >> 0x0
# R FA @0x2001A01C = 0x02
# gpio input value 0x2
# gpio0 input low
# gpio1 input high
