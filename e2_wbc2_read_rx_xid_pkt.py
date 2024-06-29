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

rx_xid_pkt = [0]*8
rx_xid_pkt[7]   =  wbc2_read(HOST_IF_EXT_ID_MSB)
rx_xid_pkt[6]   =  wbc2_read(HOST_IF_EXT_ID_7  )
rx_xid_pkt[5]   =  wbc2_read(HOST_IF_EXT_ID_6  )
rx_xid_pkt[4]   =  wbc2_read(HOST_IF_EXT_ID_5  )
rx_xid_pkt[3]   =  wbc2_read(HOST_IF_EXT_ID_4  )
rx_xid_pkt[2]   =  wbc2_read(HOST_IF_EXT_ID_3  )
rx_xid_pkt[1]   =  wbc2_read(HOST_IF_EXT_ID_2  )
rx_xid_pkt[0]   =  wbc2_read(HOST_IF_EXT_ID_LSB)

print("uart write 0x70 0x05 to disable tx print uart log for better uart communication")
ser.write([STWBC2_SET_PAGE,INDEX_PAGE_LOG_DISABLE,STWBC2_SET_PAGE,INDEX_PAGE_REGS])
print("if rx send xid pkt to TX, you can check data")
print("read rx xid pkt:", ' '.join( ['0x{:02X}'.format(x) for x in list(rx_xid_pkt)]) )
#read rx xid pkt: 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00
