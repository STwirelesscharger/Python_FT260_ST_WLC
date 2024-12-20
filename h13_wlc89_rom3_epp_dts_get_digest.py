"""
  ******************************************************************************
  * Copyright (c) 2024, STMicroelectronics - All Rights Reserved
  * Author(s): ACD (Analog Custom Devices) Software Team for STMicroelectronics.
  *
  * License terms: BSD 3-clause "New" or "Revised" License.
  *
  * Redistribution and use in source and binary forms, with or without
  * modification, are permitted provided that the following conditions are met:
  *
  * 1. Redistributions of source code must retain the above copyright notice, this
  * list of conditions and the following disclaimer.
  *
  * 2. Redistributions in binary form must reproduce the above copyright notice,
  * this list of conditions and the following disclaimer in the documentation
  * and/or other materials provided with the distribution.
  *
  * 3. Neither the name of the copyright holder nor the names of its contributors
  * may be used to endorse or promote products derived from this software
  * without specific prior written permission.
  *
  * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
  * AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
  * IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
  * DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
  * FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
  * DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
  * SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
  * CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
  * OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
  * OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
  *
  ******************************************************************************
"""
import driver_ft260
from wlc89_rom3_register import *
import time
#QI 1.3 define
QI13_Head_Digest_Response      = 0x11
QI13_Head_Certificate_Response = 0x12
QI13_Head_Challenge_Response   = 0x13
#QI 1.3 define
QI13_Head_Digest_Request      = 0x19
QI13_Head_Certificate_Request = 0x1A
QI13_Head_Challenge_Request   = 0x1B


i2c = driver_ft260.ft260_dongle()
i2c.wlc89_rom3_info()
def wlc89_rom3_adc():
    vout_meas = i2c.wread16(I2CREG_VOUT_MEAS,2)
    vrect_meas = i2c.wread16(I2CREG_VRECT_MEAS,2)
    icur_meas = i2c.wread16(I2CREG_ICUR_MEAS,2)
    chip_temp = i2c.wread16(I2CREG_CHIP_TEMP_MEAS,2) / 10
    opfreq = i2c.wread16(I2CREG_OP_FREQ,2)
    mode = i2c.wread16(I2CREG_RXOP_MODE)#0x002B
    print(f"wlc89_rom3,vrect,{vrect_meas},vout,{vout_meas},curr,{icur_meas},die,{chip_temp},freq,{opfreq}khz,mode,{mode}")
    if(32 == mode):
        print("BPP")
    elif(64 == mode):
        print("EPP")
    elif(32*4 == mode):
        print("MPP")
    return mode

print("tx use stwbc2 EVK and wlc89 use epp cfg setting")
mode = wlc89_rom3_adc()
if(64 == mode):
    print("EPP get digest")
    i2c.write16(I2CREG_INTR_CLR,[0xFF]*4)
    i2c.write16(0x0800,[0]*38)
    i2c.write16(0x0800,[0X10,2,0,0,QI13_Head_Digest_Request,0X0F])
    i2c.write16(0x004F,2)
    time.sleep(10)
    i2c.log1()
    i2c.wread16(I2CREG_INTR_LATCH,4)#0X001C
    i2c.wread16(0x0800,4+34)

# tx use stwbc2 and wlc89 use epp cfg setting
# ChipID:0x0159 rev:0x40 patchid:0xC767 cfgid:0x2302
# CUT2.3
# wlc89_rom3,vrect,9734,vout,8995,curr,68,die,43.3,freq,145khz,mode,64
# EPP
# EPP get digest
# [WR],@0x0x1c >> 0x00 0x03 0x00 0x00
# [WR],@0x0x800 >> 0x10 0x22 0x00 0x00 0x11 0x11 0x34 0xFB 0x7B 0x07 0xE4 0xB2 0x68 0xD5 0x0F 0x65 0xDC 0xA2 0x71 0x78 0x71 0x89 0x42 0xFA 0x50 0xE0 0x0B 0xB3 0x6D 0xB9 0x3E 
# 0xBF 0xD4 0xE9 0x8A 0xB0 0x5E 0xD4

