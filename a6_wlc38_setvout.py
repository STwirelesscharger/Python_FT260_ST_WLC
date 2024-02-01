import driver_ft260
from wlc38_register import *
import time
wlc38 = driver_ft260.ft260_dongle()
wlc38.chip_info()


print("set vout off")
wlc38.write16(I2CREG_RX_CMD,(1<<BIT_RX_VOUT_OFF))
time.sleep(1)
print("set vout on")
wlc38.write16(I2CREG_RX_CMD,(1<<BIT_RX_VOUT_ON))
time.sleep(1)
print("set vout 5025mV")
wlc38.wlc38_vout_set(5025)


