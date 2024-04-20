import driver_ft260
from wlc99_register import *

wlc99 = driver_ft260.ft260_dongle(i2c_speed = 100,dev_addr_set = 0x2C)
wlc99.chip_info()

def wlc99_getadc():#wlc99
    freq = wlc99.wread16(I2CREG_OP_FREQ,2)
    iin = wlc99.wread16(I2CREG_MEAS_S32,2)
    read_buff = wlc99.wread16(I2CREG_MEAS_S16,12)
    vrect = read_buff[0] + read_buff[1] * 256
    vout  = read_buff[2] + read_buff[3] * 256
    die   = read_buff[4] + read_buff[5] * 256
    die /= 10
    ntc   = read_buff[8] + read_buff[9] * 256
    ntc *= 0.164795
    print(f"rx,vrect/mV,{vrect},vout/mV,{vout},cur/mA,{iin},die/C,{die},freq/khz,{freq},ntc,{ntc}mV")

    RX_PTC_FSK_CFG = wlc99.wread16(0x00B0,1)
    isEPP = (1 << 7) & RX_PTC_FSK_CFG
    if(0 == isEPP):
        print("BPP Mode")
    else:
        print("EPP Mode")

    read_buff = wlc99.wread16(I2CREG_LAST_RP,5)
    rx_rcvd_pwr = read_buff[0] + read_buff[1] * 256
    rx_ctrl_err = read_buff[2] + read_buff[3] * 256
    if(rx_ctrl_err > 0x7FF):
        rx_ctrl_err = rx_ctrl_err - 0XFFFF
    #rx_ctrl_err /= 256
    rx_signal_strength = read_buff[4]
    print(f"rx_ctrl_err/mV,{rx_ctrl_err},rx_rcvd_pwr/mW,{rx_rcvd_pwr},rx_signal_strength,{rx_signal_strength}")

wlc99_getadc()

#test log
# Open FT260 device OK
# [WR],@0x0x10 >> 0x00 0x35 0x38 0x30 0x38 0x52 0x36 0x47 0x0D 0x00 0x00 0x00 0x1B 0x00 0x20 0x00
# Device ID 0x: 00353830385236470D0000001B002000
# [WR],@0x0x0 >> 0x63 0x00 0x02 0x00 0x55 0x01 0x60 0x12 0x00 0x00 0x00 0x2C 0x07 0x07 0x00 0x00
# ChipID:0x0063 rev:2 patchid:0x1260 cfgid:0x2C00
# CHIPID_WLC99
# [WR],@0x0x3e >> 0x73 0x00
# [WR],@0x0x40 >> 0x03 0x00
# [WR],@0x0x44 >> 0x74 0x17 0x9A 0x13 0x46 0x01 0xD7 0x09 0x3F 0x5B 0x35 0x00
# rx,vrect/mV,6004,vout/mV,5018,cur/mA,3,die/C,32.6,freq/khz,115,ntc,3849.446405mV
# [WR],@0x0xb0 >> 0x00
# BPP Mode
# [WR],@0x0x5a >> 0xB8 0x0E 0x3C 0x00 0xC9
# rx_ctrl_err/mV,0.234375,rx_rcvd_pwr/mW,3768,rx_signal_strength,201
