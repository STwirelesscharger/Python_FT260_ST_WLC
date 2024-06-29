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
from wbc86_register import *
wbc86 = driver_ft260.ft260_dongle()
wbc86.chip_info()

BIT_TX_EPT_SRC_OVP	 = 0
#0x0: Did not appear0x1: appeared
BIT_TX_EPT_SRC_OCP	 = 1
#0x0: Did not appear0x1: appeared
BIT_TX_EPT_SRC_OVTP	 = 2
#0x0: Did not appear0x1: appeared
BIT_TX_EPT_SRC_FOD	 = 3
#0x0: Did not appear0x1: appeared
BIT_TX_EPT_SRC_CMD	 = 4
#0x0: Did not appear0x1: appeared
BIT_TX_EPT_SRC_RX	 = 5
#0x0: Did not appear0x1: appeared
BIT_TX_EPT_SRC_CE_TO	 = 6
#0x0: Did not appear0x1: appeared
BIT_TX_EPT_SRC_RP_TO	 = 7
#0x0: Did not appear0x1: appeared
BIT_TX_EPT_SRC_RX_RST	 = 8
#0x0: Did not appear0x1: appeared
BIT_TX_EPT_SRC_SYS_ERR	 = 9
#0x0: Did not appear0x1: appeared
BIT_TX_EPT_SRC_SS_TO	 = 10
#0x0: Did not appear0x1: appeared
BIT_TX_EPT_SRC_SS	 = 11
#0x0: Did not appear0x1: appeared
BIT_TX_EPT_SRC_ID	 = 12
#0x0: Did not appear0x1: appeared
BIT_TX_EPT_SRC_CFG	 = 13
#0x0: Did not appear0x1: appeared
BIT_TX_EPT_SRC_CFG_CNT_ERR	 = 14
#0x0: Did not appear0x1: appeared
BIT_TX_EPT_SRC_PCH	 = 15
#0x0: Did not appear0x1: appeared
BIT_TX_EPT_SRC_XID	 = 16
#0x0: Did not appear0x1: appeared
BIT_TX_EPT_SRC_NEGO	 = 17
#0x0: Did not appear0x1: appeared
BIT_TX_EPT_SRC_NEGO_TO	 = 18

buff = wbc86.wread16(I2CREG_TX_EPT_REASON_RCVD,3)
print("use buff data and bit_tx_ept to get infor")
print(f"TX_EPT_REASON 0x{buff[0]:02X} 0x{buff[1]:02X} 0x{buff[2]:02X}")
# Test log
# Open FT260 device OK
# [WR],@0x0x10 >> 0x00 0x31 0x36 0x30 0x31 0x53 0x36 0x47 0x0B 0x00 0x00 0x00 0x17 0x00 0x33 0x00
# Device ID 0x: 00313630315336470B00000017003300
# [WR],@0x0x0 >> 0x56 0x00 0x02 0x00 0x18 0x01 0x51 0x12 0x00 0x00 0x0D 0x12 0x01 0x04 0x03 0x41
# ChipID:0x0056 rev:2 patchid:0x1251 cfgid:0x120D
# CHIPID_WBC86
# [WR],@0x0xe6 >> 0x00 0x05 0x00
# TX_EPT_REASON 0x00 0x04 0x00