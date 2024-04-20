import driver_ft260
from wlc99_register import *
import time

wlc99 = driver_ft260.ft260_dongle(i2c_speed = 100,dev_addr_set = 0x2C)
wlc99.chip_info()

print("this is use for external 5V  demo")

print("use extern 5V and connect WLC99 LDO5V")
wlc99.write16(I2CREG_RX_CMD1,(1<<BIT_RX_EXT5V_ON))
time.sleep(1)

input("remove extern 5V and dis-connect WLC99 LDO5V")
wlc99.write16(I2CREG_RX_CMD1,(1<<BIT_RX_EXT5V_OFF))
