import driver_ft260
from wbc86_register import *
wbc86 = driver_ft260.ft260_dongle()
wbc86.chip_info()

def wbc86_getadc():
    read_buff = wbc86.wread16(I2CREG_MEAS_VRECT,14)
    vrect = read_buff[0] + read_buff[1] * 256
    vout  = read_buff[2] + read_buff[3] * 256
    icur   = read_buff[4] + read_buff[5] * 256
    die   = read_buff[6] + read_buff[7] * 256
    die /= 10
    ntc  = read_buff[8] + read_buff[9] * 256
    ntc =  ntc/4 * 1500/1024
    adcin =read_buff[10] + read_buff[11] * 256
    freq = read_buff[12] + read_buff[13] * 256
    freq *= 4
    print(f"wbc86,RectifierVoltage,{vrect}mV,InputVoltage,{vout}mV,cur,{icur}mA,die,{die}C,ntc,{ntc}mV,adcin,{adcin}mV,freq/hz,{freq}")

wbc86_getadc()

# Test log
# Open FT260 device OK
# [WR],@0x0x10 >> 0x00 0x31 0x36 0x30 0x31 0x53 0x36 0x47 0x0B 0x00 0x00 0x00 0x17 0x00 0x33 0x00
# Device ID 0x: 00313630315336470B00000017003300
# [WR],@0x0x0 >> 0x56 0x00 0x02 0x00 0x18 0x01 0x53 0xA2 0x00 0x00 0x1D 0x12 0x01 0x04 0x03 0x01
# ChipID:0x0056 rev:2 patchid:0xA253 cfgid:0x121D
# CHIPID_WBC86
# [WR],@0x0x40 >> 0xF2 0x13 0xF9 0x06 0x00 0x00 0x03 0x01 0xFC 0x0F 0xC3 0x00 0x94 0x8E
# wbc86,RectifierVoltage,5106mV,InputVoltage,1785mV,cur,0mA,die,25.9C,ntc,1498.53515625mV,adcin,195mV,freq/hz,146000
