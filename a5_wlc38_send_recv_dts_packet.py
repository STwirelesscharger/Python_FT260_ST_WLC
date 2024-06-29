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
#QI 1.3 define
QI13_Head_Digest_Response      = 0x11
QI13_Head_Certificate_Response = 0x12
QI13_Head_Challenge_Response   = 0x13
#QI 1.3 define
QI13_Head_Digest_Request      = 0x19
QI13_Head_Certificate_Request = 0x1A
QI13_Head_Challenge_Request   = 0x1B


wlc38 = driver_ft260.ft260_dongle()
wlc38.chip_info()
#rx put some type tx and this tx support qi 1.3 dts packet
#wlc38 must set to EPP mode
def wlc38_dts_send(SendMsg):
    wlc38.write16(I2CREG_RX_DTS_SEND,len(SendMsg))#set dts length
    wlc38.write16(I2CREG_RX_DTS_SEND+2,0x02)#request see qi spec
    wlc38.write16(DTS_SEND_MSG_000,SendMsg)
    wlc38.write16(I2CREG_RX_CMD,(1<<BIT_RX_SEND_DTS))
    time.sleep(2)
    print("read int and read buff")
    wlc38.wread16(I2CREG_RX_INTR_LATCH,4)#read int status
    dts_rcv_cnt = wlc38.wread16(I2CREG_RX_DTS_RCVD,2)
    print(f"dts_rcv_cnt,{dts_rcv_cnt}")
    if(dts_rcv_cnt > 1):
        wlc38.wread16(DTS_RCVD_MSG_000,dts_rcv_cnt)

print("RX Send QIV13_GetDigest")
wlc38_dts_send([QI13_Head_Digest_Request,0x0F])


