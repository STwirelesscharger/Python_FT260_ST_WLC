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
    mode = i2c.wread16(I2CREG_RXOP_MODE)
    print(f"wlc89_rom3,vrect,{vrect_meas},vout,{vout_meas},curr,{icur_meas},die,{chip_temp},freq,{opfreq}khz,mode,{mode}")
    if(32 == mode):
        print("BPP")
    elif(64 == mode):
        print("EPP")
    elif(32*4 == mode):
        print("MPP")
    return mode

mode = wlc89_rom3_adc()
if(32*4 == mode):
    print("MPP get certify first 16 bytes")
    i2c.write16(I2CREG_INTR_CLR,[0xFF]*4)#0x0024
    #i2c.write16(0x0800,[0]*38)
    i2c.write16(0x0800,[0X20,4,0,0,QI13_Head_Certificate_Request,0,0,15])#set length to 15
    i2c.write16(0x004F,2)
    time.sleep(2)
    i2c.log1()
    i2c.wread16(I2CREG_INTR_LATCH,4)#0X001C
    buff = i2c.wread16(0x0800,4+2+16)

# Open FT260 device OK
# ChipID:0x0159 rev:0x40 patchid:0xB053 cfgid:0x4011
# CUT2.3
# wlc89_rom3,vrect,13735,vout,12996,curr,72,die,66.0,freq,360khz,mode,128
# MPP
# MPP get digest
# [WR],@0x0x1c >> 0x00 0x03 0x08 0x00
# [WR],@0x0x800 >> 0x20 0x10 0x00 0x00 
# 0x12 0x02< 
# 0xBC< 0xA1 0x75 0x9E 
# 0xCC 0xA0 0xBE 0x3B 
# 0x85 0x01 0x18 0x18 
# 0x3E 0xD6 0x00 0x00
# length = 0x02BC + 1 = 700bytes