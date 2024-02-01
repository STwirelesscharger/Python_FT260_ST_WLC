import driver_ft260
from wbc86_register import *
import time
wbc86 = driver_ft260.ft260_dongle()
wbc86.chip_info()

#wbc86.write16(I2CREG_AUX_DATA,[0x1E,0x01,0x02])
wbc86.write16(I2CREG_AUX_DATA,0xFF)
wbc86.write16(I2CREG_TX_CMD,(1<<BIT_TX_SEND_MSG))
time.sleep(1)
wbc86.wread16(I2CREG_TX_CMD)
