import driver_ft260
from wbc86_register import *
wbc86 = driver_ft260.ft260_dongle()
wbc86.chip_info()

wbc86.wread16(I2CREG_TX_EPT_REASON_RCVD,3)
