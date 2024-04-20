import driver_ft260
from wlc98_register import *
import time
wlc98 = driver_ft260.ft260_dongle()
wlc98.chip_info()

print("example code set gpio0 pin input float")
wlc98.write16(I2CREG_GPIO0_FUNC,GPIO_FUNC_IN_FL)
time.sleep(1)

print("example code set gpio0 pin pp high")
wlc98.write16(I2CREG_GPIO0_FUNC,GPIO_FUNC_PP_HI)
time.sleep(1)
print("example code set gpio0 pin pp low")
wlc98.write16(I2CREG_GPIO0_FUNC,GPIO_FUNC_PP_LO)

# Open FT260 device OK
# [WR],@0x0x10 >> 0x00 0x34 0x31 0x30 0x32 0x35 0x30 0x51 0x14 0x00 0x00 0x00 0x19 0x00 0x19 0x00
# Device ID 0x: 00343130323530511400000019001900
# [WR],@0x0x0 >> 0x62 0x00 0x02 0x00 0x01 0x02 0x54 0x14 0x00 0x00 0x00 0x2C 0x06 0x00 0x02 0x53
# ChipID:0x0062 rev:2 patchid:0x1454 cfgid:0x2C00
# CHIPID_WLC98
# example code set gpio0 pin input float
# [W],@0x30 >> 0x0
# example code set gpio0 pin pp high
# [W],@0x30 >> 0x4
# example code set gpio0 pin pp low
# [W],@0x30 >> 0x3