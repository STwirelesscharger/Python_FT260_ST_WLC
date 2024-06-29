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
from wlc38_register import *
import time
wlc38 = driver_ft260.ft260_dongle()
wlc38.chip_info()
wlc38.log1()
#rx put some type tx and this tx can reply ask 0x38 packet
wlc38.write16(I2CREG_RX_INTR_CLR,[0xFF,0xFF,0xFF,0xFF])#clear intr
wlc38.write16(I2CREG_RCVD_MSG,[0]*8)#clear read buff
#wlc38.write16(I2CREG_SEND_MSG,[0x38,0x3B,0x88,0x66])#rx send 0x38 0x3B 0x88 0x66 packet
wlc38.write16(I2CREG_SEND_MSG,[0x19,0x38])#rx send 0x19 0x38 pp packet
wlc38.write16(I2CREG_RX_CMD,(1<<BIT_RX_SEND_MSG_WAIT_REPLY))
time.sleep(1)
print("read int and read buff")
tx_reply_data = wlc38.wread16(I2CREG_RCVD_MSG,8)#0X0190
print("tx_reply_data: ", ' '.join( ['0x{:02X}'.format(x) for x in tx_reply_data]) )
#tx_reply_data:  0x97 0xC3 0xB4 0xE0 0x2F 0x86 0x68 0xC1 patchid:0x1437 cfgid:0x1F47

intr_latch = wlc38.wread16(I2CREG_RX_INTR_LATCH,4)#read int status
if(intr_latch[0] & (1<<BIT_RX_RCVD_MSG_INTR_LATCH) == (1<<BIT_RX_RCVD_MSG_INTR_LATCH)):
      print("BIT_RX_RCVD_MSG_INTR_LATCH")
wlc38.write16(I2CREG_RX_INTR_CLR,[0xFF,0xFF,0xFF,0xFF])#clear intr

#test log
# Open FT260 device OK
# [WR],@0x0x10 >> 0x00 0x5A 0x34 0x30 0x32 0x54 0x55 0xAA 0x02 0x53 0x3C 0x0F 0x55 0xAA 0x55 0xAA
# Device ID 0x: 005A3430325455AA02533C0F55AA55AA
# [WR],@0x0x0 >> 0x26 0x00 0x03 0x00 0x61 0x01 0x37 0x14 0x00 0x00 0x47 0x1F 0x07 0x00 0x02 0x51
# ChipID:0x0026 rev:3 patchid:0x1437 cfgid:0x1F47
# CHIPID_WLC38
# [W],@0x0x180 >> 0x38 0x3B 0x88 0x66
# [W],@0x90 >> 0x8
# read int and read buff
# [WR],@0x0x190 >> 0x3F 0x3B 0x88 0x66 0xEA 0x00 0x00 0x00
# tx_reply_data:  0x3F 0x3B 0x88 0x66 0xEA 0x00 0x00 0x00
# [WR],@0x0x88 >> 0x20 0x00 0x00 0x00
# [W],@0x0x84 >> 0xFF 0xFF 0xFF 0xFF
