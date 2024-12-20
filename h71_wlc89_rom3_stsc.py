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
#config must work at bpp mode
STSC_Auth_Req = [0x48, 0xA5, 0x00, 0x00, 0x16]
STSC_Req = [0x48, 0x5C, 0x64, 0xAE, 0x00]
STSC_RP24_Req= [0x48, 0x24, 0x52, 60, 0x00]
STSC_5V_Req  = [0x48, 0x73, 0x00, 0x88, 0x13]
STSC_9V_Req  = [0x48, 0x73, 0x00, 0x28, 0x23]
STSC_12V_Req = [0x48, 0x73, 0x00, 0xE0, 0x2E]
STSC_15V_Req = [0x48, 0x73, 0x00, 0x98, 0x3A]
STSC_18V_Req = [0x48, 0x73, 0x00, 0x50, 0x46]
STSC_20V_Req = [0x48, 0x73, 0x00, 0x20, 0x4E]
STSC_FIX_FREQ= [0x48, 0x68, 0x11, 140, 140]

rx = driver_ft260.ft260_dongle()
rx.wlc89_rom3_info()
rx.log1()
print("tx use stwbc2 EVK and wlc89 use bpp cfg setting")
rx.write16(I2CREG_RCVD_MSG_CMD,[0]*10)#clear
rx.write16(I2CREG_SEND_MSG_HDR,STSC_9V_Req)
rx.write16(I2CREG_CMD,1<<BIT_SEND_MSG)
#delay 1s
time.sleep(1)
rx.wread16(I2CREG_RCVD_MSG_CMD,10)


# Open FT260 device OK
# ChipID:0x0159 rev:0x40 patchid:0xB767 cfgid:0x2600
# CUT2.3
# [W],@0x0xd4 >> 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00
# [W],@0x0x50 >> 0x48 0x73 0x00 0x28 0x23
# [W],@0x4E >> 0x1
# [WR],@0x0xd4 >> 0x1E 0x01 0x1F 0x00 0x00 0x00 0x00 0x00 0x00 0x00





