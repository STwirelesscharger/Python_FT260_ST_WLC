import driver_ft260
from wbc86_register import *
wbc86 = driver_ft260.ft260_dongle()
wbc86.chip_info()

print("set tx enable")
wbc86.write16(I2CREG_TX_CMD,(1<<BIT_TX_EN))

print("set tx disable")
wbc86.write16(I2CREG_TX_CMD,(1<<BIT_TX_DIS))



