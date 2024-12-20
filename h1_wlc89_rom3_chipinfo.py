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

rx = driver_ft260.ft260_dongle()
rx.log1()

def wlc89_rom3_info():
    read_buff = rx.wread16(I2CREG_CHIP_ID,8)#0x0000
    chipid = read_buff[0] + read_buff[1] * 256
    chiprev = read_buff[2]
    custid = read_buff[3]
    patchid = read_buff[4] + read_buff[5] * 256
    cfgid = read_buff[6] + read_buff[7] * 256
    print("ChipID:0x{:04X} rev:0x{:02X} patchid:0x{:04X} cfgid:0x{:04X}".format(chipid,chiprev,patchid,cfgid))
    if(chiprev == 0x20):
        print("CUT2.1")
    elif(chiprev == 0x30):
        print("CUT2.2")
    elif(chiprev == 0x40):
        print("CUT2.3")
    else:
        print("[ERR] Not ROM3")
    rx.wread16(I2CREG_OP_MODE)
    rx.wread16(I2CREG_OP_SUB_MODE)

def wlc89_rom3_DeviceId():
    read_buff = rx.wread16(I2CREG_RX_ID,6)
    print("Device ID 0x:",''.join( ['{:02X}'.format(x) for x in read_buff]) )

wlc89_rom3_info()
wlc89_rom3_DeviceId()

# Open FT260 device OK
# [WR],@0x0000 >> 0x59 0x01 0x40 0x00 0x44 0xE1 0x00 0x26
# ChipID:0x0159 rev:0x40 patchid:0xE144 cfgid:0x2600
# CUT2.3
# [WR],@0x0102 >> 0x02
# [WR],@0x0103 >> 0x0A
# [WR],@0x0010 >> 0x00 0x16 0x00 0x00 0x00 0x00
# Device ID 0x: 001600000000



