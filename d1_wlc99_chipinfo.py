import driver_ft260

wlc99 = driver_ft260.ft260_dongle(i2c_speed = 100,dev_addr_set = 0x2C)
wlc99.chip_info()

#test log
# Open FT260 device OK
# [WR],@0x0x10 >> 0x00 0x35 0x38 0x30 0x38 0x52 0x36 0x47 0x0D 0x00 0x00 0x00 0x1B 0x00 0x20 0x00
# Device ID 0x: 00353830385236470D0000001B002000
# [WR],@0x0x0 >> 0x63 0x00 0x02 0x00 0x55 0x01 0x60 0x12 0x00 0x00 0x00 0x2C 0x07 0x07 0x00 0x00
# ChipID:0x0063 rev:2 patchid:0x1260 cfgid:0x2C00
# CHIPID_WLC99