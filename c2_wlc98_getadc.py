import driver_ft260
from wlc98_register import *

wlc98 = driver_ft260.ft260_dongle()
wlc98.chip_info()

def wlc98_getadc():#wlc98
    read_buff = wlc98.wread16(I2CREG_RX_VRECT,12)
    vrect = read_buff[0] + read_buff[1] * 256
    vout  = read_buff[2] + read_buff[3] * 256
    iin   = read_buff[4] + read_buff[5] * 256
    die   = read_buff[6] + read_buff[7] * 256
    die /= 10
    freq  = read_buff[8] + read_buff[9] * 256
    ntc   = read_buff[10] + read_buff[11] * 256
    ntc /= 10
    print(f"rx,vrect/mV,{vrect},vout/mV,{vout},cur/mA,{iin},die/C,{die},freq/khz,{freq},ntc/mV,{ntc}")

    RX_PTC_FSK_CFG = wlc98.wread16(0x00B0,1)
    isEPP = (1 << 7) & RX_PTC_FSK_CFG
    if(0 == isEPP):
        print("BPP Mode")
    else:
        print("EPP Mode")

    read_buff = wlc98.wread16(I2CREG_RX_CTRL_ERR,5)
    rx_ctrl_err = read_buff[0] + read_buff[1] * 256
    if(rx_ctrl_err > 0x7FF):
        rx_ctrl_err = rx_ctrl_err - 0XFFFF
    rx_ctrl_err /= 256
    rx_rcvd_pwr = read_buff[2] + read_buff[3] * 256
    rx_signal_strength = read_buff[4]
    print(f"rx_ctrl_err/mV,{rx_ctrl_err},rx_rcvd_pwr/mW,{rx_rcvd_pwr},rx_signal_strength,{rx_signal_strength}")
    
wlc98_getadc()

#test log1
# Open FT260 device OK
# [WR],@0x0x10 >> 0x00 0x34 0x31 0x30 0x32 0x35 0x30 0x51 0x14 0x00 0x00 0x00 0x19 0x00 0x19 0x00
# Device ID 0x: 00343130323530511400000019001900
# [WR],@0x0x0 >> 0x62 0x00 0x02 0x00 0x01 0x02 0x54 0x14 0x00 0x00 0x00 0x2C 0x06 0x00 0x02 0x51
# ChipID:0x0062 rev:2 patchid:0x1454 cfgid:0x2C00
# CHIPID_WLC98
# [WR],@0x0x92 >> 0x4E 0x24 0x54 0x23 0x29 0x00 0x57 0x01 0x7C 0x00 0xF0 0x3F
# rx,vrect/mV,9294,vout/mV,9044,cur/mA,41,die/C,34.3,freq/khz,124,ntc,16368
# [WR],@0x0xb0 >> 0x80
# EPP Mode
# [WR],@0x0xa8 >> 0xCA 0xFF 0x00 0x7F 0x5E
# rx_ctrl_err/mV,-0.20703125,rx_rcvd_pwr/mW,32512,rx_signal_strength,94
