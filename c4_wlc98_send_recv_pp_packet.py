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
from wlc98_register import *
import time
wlc98 = driver_ft260.ft260_dongle()
wlc98.chip_info()

STSC_RP24_Req= [0x48, 0x24, 0x52, 200, 0x00]

def wlc98_send_pp(packet):
    wlc98.write16(I2CREG_SEND_MSG,packet)#rx send 0x38 0x3B 0x88 0x66 packet
    wlc98.write16(I2CREG_RX_CMD,(1<<BIT_RX_SEND_MSG_WAIT_REPLY))
    time.sleep(1)
    print("read int and read buff")
    tx_reply_data = wlc98.wread16(I2CREG_RCVD_MSG,8)#0X0190
    print("tx_reply_data: ", ' '.join( ['0x{:02X}'.format(x) for x in tx_reply_data]) )
    wlc98.wread16(I2CREG_RX_INTR_LATCH,4)#read int status
    wlc98.write16(I2CREG_RX_INTR_CLR,[0xFF,0xFF,0xFF,0xFF])#clear intr

wlc98_send_pp(STSC_RP24_Req)

# Open FT260 device OK
# [WR],@0x0x10 >> 0x00 0x34 0x31 0x30 0x32 0x35 0x30 0x51 0x14 0x00 0x00 0x00 0x19 0x00 0x19 0x00
# Device ID 0x: 00343130323530511400000019001900
# [WR],@0x0x0 >> 0x62 0x00 0x02 0x00 0x01 0x02 0x54 0x14 0x00 0x00 0x00 0x2C 0x06 0x00 0x02 0x51
# ChipID:0x0062 rev:2 patchid:0x1454 cfgid:0x2C00
# CHIPID_WLC98
# [W],@0x0x180 >> 0x48 0x24 0x52 0xC8 0x00
# [W],@0x90 >> 0x8
# read int and read buff
# [WR],@0x0x190 >> 0x1E 0x01 0x1F 0x00 0x00 0x00 0x00 0x00
# tx_reply_data:  0x1E 0x01 0x1F 0x00 0x00 0x00 0x00 0x00
# [WR],@0x0x88 >> 0xE4 0x0C 0x01 0x00
# [W],@0x0x84 >> 0xFF 0xFF 0xFF 0xFF
