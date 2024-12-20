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
import random
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

def print_hex(title, _bytes, modulo=8):
    print(title)
    for i in range(0, len(_bytes)):
        print(' 0x{:02X},'.format(_bytes[i]), end='' )
        if(modulo != 0):
            if((i != 0) and ((i+1)%modulo) == 0):
                print()
    if(modulo == 0):
        print(" ... ...")
    elif(len(_bytes) % modulo != 0):
        print()

print("tx use stwbc2 EVK and wlc89 use epp cfg setting")
mode = wlc89_rom3_adc()
if(64 == mode):
    print("EPP challenge send:")
    i2c.write16(I2CREG_INTR_CLR,[0xFF]*4)
    p_challrx = [0x20,12,0,0] + [QI13_Head_Challenge_Request,0x00]
    for i in range(16):#add 16byte random data
        p_challrx.append(random.randint(0,255))
    print_hex("send: ",p_challrx)
    i2c.write16(0x0800,p_challrx)
    i2c.write16(0x004F,2)
    time.sleep(5)
    i2c.log1()
    i2c.wread16(I2CREG_INTR_LATCH,4)#0X001C
    i2c.wread16(0x0800,4+67)

# Open FT260 device OK
# send:
#  0x20, 0x0C, 0x00, 0x00, 0x1B, 0x00, 0x12, 0x63,
#  0x4C, 0x91, 0xC5, 0x57, 0x2C, 0x19, 0x94, 0xAC,
#  0x31, 0x14, 0x94, 0x3C, 0x38, 0x45,
# [WR],@0x0x1c >> 0x00 0x03 0x08 0x00
# [WR],@0x0x800 >> 0x20 0x43 0x00 0x00 <-- 0X43 means 67
# 0x13 0x11 
# 0x7D 0xB8 0xD6 0xA3 0x62 0x6F 0x4C 0xD2 
# 0x08 0xAE 0xE0 0x77 0x48 0xA6 0x4F 0x37 
# 0x8B 0xAE 0x3B 0xB4 0x2D 0x08 0x70 0xC9 
# 0xDD 0x3E 0xEB 0x6C 0x68 0x35 0xD7 0xF8 
# 0xA5 0x04 0xE6 0x14 0x48 0xBD 0x12 0xD1 
# 0x81 0xF6 0xB1 0xF8 0xE5 0xED 0x5C 0x37 
# 0x69 0xC9 0x7C 0x74 0x51 0xB1 0x6F 0x66 
# 0x5B 0x8E 0x84 0xF5 0x5E 0xD4 0xA0 0x52 0x37