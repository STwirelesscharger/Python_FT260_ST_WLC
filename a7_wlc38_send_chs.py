import driver_ft260
from wlc38_register import *
import time
wlc38 = driver_ft260.ft260_dongle()
wlc38.chip_info()

rx_send_chargeStatus_value = 100
wlc38.write16(I2CREG_SEND_MSG,[0x05,rx_send_chargeStatus_value])
wlc38.write16(I2CREG_RX_CMD,(1<<BIT_RX_SEND_MSG))

# Test log
# Open FT260 device OK
# [WR],@0x0x10 >> 0x00 0x5A 0x34 0x30 0x32 0x54 0x55 0xAA 0x02 0x53 0x3C 0x0F 0x55 0xAA 0x55 0xAA
# Device ID 0x: 005A3430325455AA02533C0F55AA55AA
# [WR],@0x0x0 >> 0x26 0x00 0x03 0x00 0x61 0x01 0x37 0x14 0x00 0x00 0x47 0x1F 0x07 0x00 0x02 0x51
# ChipID:0x0026 rev:3 patchid:0x1437 cfgid:0x1F47
# CHIPID_WLC38
# [W],@0x0x180 >> 0x05 0x64
# [W],@0x90 >> 0x4
