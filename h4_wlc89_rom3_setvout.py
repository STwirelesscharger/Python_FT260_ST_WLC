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


def wlc89_rom3_vout_set(val = 5000):#unit is mV
  if(val > 20000):
    print("wlc89 only support max 20000mV")
    rx_vout_set_register = 828
  elif(val < 3460):
    print("wlc89 only support min 3460mV")
    rx_vout_set_register = 0
  else:
    rx_vout_set_register = int((val-3440)/20)#each bit mean 20mV

  Data16 = rx_vout_set_register.to_bytes(2, byteorder='big')
  send_buff = [Data16[1], Data16[0]]
  rx.write16(I2CREG_RX_VOUT_SET,send_buff)#ROM3

print("set vout off")
rx.write16(I2CREG_CMD,(1<<BIT_LDO_TOGGLE))//1
time.sleep(1)

print("set vout on")
rx.write16(I2CREG_CMD,(1<<BIT_LDO_TOGGLE))
time.sleep(1)

print("set vout 6000")
wlc89_rom3_vout_set(6000)
time.sleep(1)

print("set vout 5000")
wlc89_rom3_vout_set(5000)
time.sleep(1)

# Open FT260 device OK
# set vout off
# [W],@0x4E >> 0x2
# set vout on
# [W],@0x4E >> 0x2
# set vout 6000
# [W],@0x0x3e >> 0x80 0x00
# set vout 5000
# [W],@0x0x3e >> 0x4E 0x00