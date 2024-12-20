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

mode = wlc89_rom3_adc()
if(32*4 == mode):
    print("MPP get certify 128 bytes")
    i2c.write16(I2CREG_INTR_CLR,[0xFF]*4)
    i2c.write16(0x0800,[0X20,4,0,0,QI13_Head_Certificate_Request,0,0,0x7F])#read 128bytes
    #0x20 4 0 0 0x1A 0 0 32
    i2c.write16(0x004F,2)
    time.sleep(2)
    for item in range(0,10):
        rx_int = i2c.wread16(I2CREG_INTR_LATCH+1)#0X001D
        if(0x03 == rx_int):
            break
        else:
            print("wait")
            time.sleep(2)
    buff = i2c.wread16(0x0800,4+3)
    print_hex("first 7bytes:",buff)
    length = buff[5]*256 + buff[6]
    print(f"certif len {length}")

    buff = i2c.wread16(0x0800,128+4)
    print_hex("read all:",buff)

# first 7bytes:
#  0x20, 0x80, 0x00, 0x00, 0x12, 0x02, 0xBC,
# certif len 700
# read 128:
#  0x20, 0x80, 0x00, 0x00, 0x12, 0x02, 0xBC, 0xA1,
#  0x75, 0x9E, 0xCC, 0xA0, 0xBE, 0x3B, 0x85, 0x01,
#  0x18, 0x18, 0x3E, 0xD6, 0xCD, 0xD6, 0xD4, 0xA5,
#  0xDB, 0x7D, 0x83, 0xE6, 0xFD, 0x0E, 0x6F, 0x47,
#  0x5C, 0xE4, 0xBB, 0x6E, 0xA0, 0x14, 0x24, 0x30,
#  0x82, 0x01, 0x44, 0x30, 0x81, 0xEB, 0xA0, 0x03,
#  0x02, 0x01, 0x02, 0x02, 0x08, 0x79, 0x14, 0x67,
#  0x59, 0xCD, 0x80, 0xCF, 0xCB, 0x30, 0x0A, 0x06,
#  0x08, 0x2A, 0x86, 0x48, 0xCE, 0x3D, 0x04, 0x03,
#  0x02, 0x30, 0x11, 0x31, 0x0F, 0x30, 0x0D, 0x06,
#  0x03, 0x55, 0x04, 0x03, 0x0C, 0x06, 0x57, 0x50,
#  0x43, 0x43, 0x41, 0x31, 0x30, 0x20, 0x17, 0x0D,
#  0x32, 0x33, 0x31, 0x31, 0x32, 0x34, 0x31, 0x30,
#  0x31, 0x38, 0x35, 0x38, 0x5A, 0x18, 0x0F, 0x39,
#  0x39, 0x39, 0x39, 0x31, 0x32, 0x33, 0x31, 0x32,
#  0x33, 0x35, 0x39, 0x35, 0x39, 0x5A, 0x30, 0x12,
#  0x31, 0x10, 0x30, 0x0E, 0x00, 0x00, 0x00, 0x00,
#  0x00, 0x00,