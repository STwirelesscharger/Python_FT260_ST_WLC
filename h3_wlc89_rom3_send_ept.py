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

CODE_EPT_NUL     = 0x00,
CODE_EPT_CC      = 0x01,
CODE_EPT_IF      = 0x02,
CODE_EPT_OT      = 0x03,
CODE_EPT_OV      = 0x04,
CODE_EPT_OC      = 0x05,
CODE_EPT_BT      = 0x06,
CODE_EPT_RSVD0   = 0x07,
CODE_EPT_NR      = 0x08,
CODE_EPT_RSVD1   = 0x09,
CODE_EPT_AN      = 0x0A,
CODE_EPT_RST     = 0x0B,
CODE_EPT_REP     = 0x0C,
CODE_EPT_RFID    = 0x0D,

def wlc98_send_ept():
  print("rx send ept charge full")
  rx.write16(I2CREG_RX_EPT,CODE_EPT_CC)#charge full
  rx.write16(I2CREG_CMD,(1<<BIT_RX_SEND_EPT))

def wlc98_send_eptrst():
    rx.write16(0x003B,0x0B)
    rx.write16(0x004E,1<<3)
      
def test_charge_status():
    print("send charge status 99%")
    rx.write16(I2CREG_RX_CHS,99)
    rx.write16(I2CREG_CMD,1<<BIT_RX_SEND_CHS)

test_charge_status()
# Open FT260 device OK
# Open FT260 device OK
# send charge status 99%
# [W],@0x3A >> 0x63
# [W],@0x4E >> 0x10
