import driver_ft260
from wlc99_register import *
import time
wlc99 = driver_ft260.ft260_dongle(i2c_speed = 100,dev_addr_set = 0x2C)
wlc99.chip_info()

print("example code set gpio0 pin input float")
wlc99.write16(I2CREG_GPIO0_FUNC,GPIO_FUNC_IN_FL)
time.sleep(1)

print("example code set gpio0 pin pp high")
wlc99.write16(I2CREG_GPIO0_FUNC,GPIO_FUNC_PP_HI)
time.sleep(1)
print("example code set gpio0 pin pp low")
wlc99.write16(I2CREG_GPIO0_FUNC,GPIO_FUNC_PP_LO)

# Open FT260 device OK
# [WR],@0x0x10 >> 0x00 0x35 0x38 0x30 0x38 0x52 0x36 0x47 0x0D 0x00 0x00 0x00 0x1B 0x00 0x20 0x00
# Device ID 0x: 00353830385236470D0000001B002000
# [WR],@0x0x0 >> 0x63 0x00 0x02 0x00 0x55 0x01 0x60 0x12 0x00 0x00 0x00 0x2C 0x07 0x07 0x00 0x00
# ChipID:0x0063 rev:2 patchid:0x1260 cfgid:0x2C00
# CHIPID_WLC99
# example code set gpio0 pin input float
# [W],@0x30 >> 0x0
# example code set gpio0 pin pp high
# [W],@0x30 >> 0x4
# example code set gpio0 pin pp low
# [W],@0x30 >> 0x3
