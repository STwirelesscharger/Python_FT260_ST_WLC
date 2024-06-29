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
import serial
from wbc2_register import *

ser = serial.Serial('COM6', 115200, timeout = 1)

def wbc2_read(add):
      ser.write([STWBC2_READ_HOST,add])
      buff = ser.read(2)
      if(buff[0] != STWBC2_READ_HOST):
          print("[ERR] read buff[0] 0x{:02X} not equal to 0x72".format(buff[0]))
      return buff[1]

print("uart write 0x70 0x05 to disable tx print uart log for better uart communication")
ser.write([STWBC2_SET_PAGE,INDEX_PAGE_LOG_DISABLE,STWBC2_SET_PAGE,INDEX_PAGE_REGS])

rx_ss      = wbc2_read(HOST_IF_SIGNAL_STRENGTH)
print(f"rx_ss {rx_ss}")
rx_version = wbc2_read(HOST_IF_RX_VERSION)
print(f"rx_version {rx_version}")
rx_chs     = wbc2_read(HOST_IF_CHARGE_STATUS)
print(f"rx_chs {rx_chs}")
rx_ref_q   = wbc2_read(HOST_IF_REF_Q_FACTOR)
rx_qfact   = wbc2_read(HOST_IF_Q_FACTOR)
print(f"rx qfact {rx_ref_q} {rx_qfact}")
rx_ce      = wbc2_read(HOST_IF_CE)
print(f"rx_ce {rx_ce}")
rx_rp8     = wbc2_read(HOST_IF_RP8)
print(f"rx_rp8 {rx_rp8}")#when rx work at BPP this have value
rx_ept     = wbc2_read(HOST_IF_EPT)#this need rx send ept packet
print(f"rx_ept {rx_ept}")
rx_rp24_b2 = wbc2_read(HOST_IF_RP24_B2)
rx_rp24_b1 = wbc2_read(HOST_IF_RP24_B1)
rx_rp24_b0 = wbc2_read(HOST_IF_RP24_B0)
print(f"rx rp24 {rx_rp24_b2} {rx_rp24_b1} {rx_rp24_b0}")#when rx work at EPP this have value

# test logs:
# rx_ss 180
# rx_version 3
# rx_chs 0 rx need to send chs pkt first
# rx qfact 0 247
# rx_ce 0
# rx_rp8 14 this is bpp mode
# rx_ept 11 this is rx send ept reping packet to rx
# rx rp24 0 0 0

# test logs:
# rx_ss 135
# rx_version 3
# rx_chs 0 rx need to send chs pkt first
# rx qfact 79 57
# rx_ce 240
# rx_rp8 0
# rx_ept 0
# rx rp24 80 5 2 this is epp mode