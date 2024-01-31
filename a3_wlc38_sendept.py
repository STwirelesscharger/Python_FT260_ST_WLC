import driver_ft260
from wlc38_register import *

wlc38 = driver_ft260.ft260_dongle()
wlc38.chip_info()

wlc38.write16(I2CREG_RX_EPT_MSG,11)
wlc38.write16(I2CREG_RX_CMD,(1<<BIT_RX_SEND_EPT))#rx send ept
