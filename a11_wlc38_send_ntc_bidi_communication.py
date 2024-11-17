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

def wlc38_bidi_communication(send_buff = [0x19,0x38]):
  wlc38.write16(I2CREG_RX_INTR_CLR,[0xFF,0xFF,0xFF,0xFF])#clear intr
  wlc38.write16(I2CREG_RCVD_MSG,[0]*8)#clear read buff
  wlc38.write16(I2CREG_SEND_MSG,send_buff)
  wlc38.write16(I2CREG_RX_CMD,(1<<BIT_RX_SEND_MSG_WAIT_REPLY))
  time.sleep(1)
  print("read int and read buff")
  tx_reply_data = wlc38.wread16(I2CREG_RCVD_MSG,8)#0X0190
  print("tx_reply_data: ", ' '.join( ['0x{:02X}'.format(x) for x in tx_reply_data]) )
  intr_latch = wlc38.wread16(I2CREG_RX_INTR_LATCH,4)#read int status
  if(intr_latch[0] & (1<<BIT_RX_RCVD_MSG_INTR_LATCH) == (1<<BIT_RX_RCVD_MSG_INTR_LATCH)):
        print("BIT_RX_RCVD_MSG_INTR_LATCH")
  wlc38.write16(I2CREG_RX_INTR_CLR,[0xFF,0xFF,0xFF,0xFF])#clear intr

def wlc38_send_ntc():
    ntc = wlc38.wread16(I2CREG_RX_NTC,2)#0x009C
    if(ntc < 32768):
        ntc = (ntc*3600/16384)+1800
    else:
        ntc = 1800-((65536-ntc)*3600/16384)
    wlc38_bidi_communication([0x58,0x1F,ntc<<8,ntc&0xFF,0x00,0x00])#use 0x58 head packet to send

wlc38_send_ntc()
