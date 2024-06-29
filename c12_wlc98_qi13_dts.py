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
import time
import random
from wlc98_register import *

#WORK WITH stwbc2 1.3.0.0 fw
RX_DTS_ADC_SEND_LEN     = 0X00D8
RX_DTS_ADC_SEND_REQUEST = 0X00DA
RX_DTS_ADC_RCVD_LEN     = 0X00DC
DTS_SEND_MSG_000        = 0X0200
DTS_RCVD_MSG_000        = 0x0280
RX_CMD_ADDRESS = 0x0090
BIT_RX_SEND_DTS= 0X20
RX_INTR_LATCH  = 0x008A
RX_INTR_CLEAR  = 0x0086
#reg map 0X008A
rx_dts_send_success_intr_latch     = 0x01
rx_dts_send_end_timeout_intr_latch = 0x02
rx_dts_send_end_reset_intr_latch   = 0x04
rx_dts_rcvd_success_intr_latch     = 0x10
rx_dts_rcvd_end_timeout_intr_latch = 0x20
rx_dts_rcvd_end_reset_intr_latch   = 0x40
#QI 1.3 define
QI13_Head_Digest_Response      = 0x11
QI13_Head_Certificate_Response = 0x12
QI13_Head_Challenge_Response   = 0x13
#QI 1.3 define
QI13_Head_Digest_Request      = 0x19
QI13_Head_Certificate_Request = 0x1A
QI13_Head_Challenge_Request   = 0x1B


i2c = driver_ft260.ft260_dongle()
i2c.chip_info()
print("WLC98 QI1.3 DTS example, RX must work at EPP and TX use STWBC2")
def print_hex(title, _bytes, modulo=8):
    print(title)
    for i in range(0, len(_bytes)):
        print(' 0x{:02X},'.format(_bytes[i]), end='' )
        if(modulo != 0):
            if((i != 0) and ((i+1)%modulo) == 0):
                print()
    if(modulo == 0):
        print(" ... ...")
    elif(len(_bytes) % modulo != 0):
        print()

def QI13_Send(SendMsg):
    print_hex("QI13_Send:",SendMsg)
    i = 0; Timeout = 10;
    i2c.write16(RX_INTR_CLEAR,0xFF)#clear flag
    i2c.write16(RX_DTS_ADC_SEND_LEN,len(SendMsg))
    i2c.write16(RX_DTS_ADC_SEND_REQUEST,0x02)#fix 02
    i2c.write16(DTS_SEND_MSG_000,SendMsg)
    i2c.write16(RX_CMD_ADDRESS,BIT_RX_SEND_DTS)#dts send
    while(i < Timeout):
        time.sleep(0.1)
        status = i2c.wread16(RX_INTR_LATCH)
        if(status & rx_dts_send_success_intr_latch):
            print("[PASS] rx_dts_send_success_intr_latch")
            break
        elif(status & rx_dts_send_end_timeout_intr_latch):
            print("[ERR] rx_dts_send_success_intr_latch")
            return
        elif(status & rx_dts_send_end_reset_intr_latch):
            print("[ERR] rx_dts_send_end_reset_intr_latch")
            return
        elif(status != 0):
            print(f"int status 0x{status:X}")
        else:
            print('.',end='')
    i2c.write16(RX_INTR_CLEAR,0x0F)#clear flag
    if(i > Timeout):
        print("[ERR] send timeout")
        return
    print()
    print("DTS Recv ...")
    i = 0;
    while(i < Timeout):
        time.sleep(0.1)
        status = i2c.wread16(RX_INTR_LATCH)
        if(status & rx_dts_rcvd_success_intr_latch):
            print("[PASS] rx_dts_rcvd_success_intr_latch")
            break
        elif(status & rx_dts_rcvd_end_timeout_intr_latch):
            print("[ERR] rx_dts_rcvd_end_timeout_intr_latch")
            return
        elif(status & rx_dts_rcvd_end_reset_intr_latch):
            print("[ERR] rx_dts_rcvd_end_reset_intr_latch")
            return
        elif(status != 0):
            print(f"int status 0x{status:X}")
        else:
            print('.',end='')
    if(i > Timeout):
        print("[ERR] recv timeout")
        return
    read_buf = i2c.wread16(RX_DTS_ADC_RCVD_LEN,2)
    dts_rcv_cnt = read_buf[0] + read_buf[1] * 256
    print(f"dts_rcv_cnt {dts_rcv_cnt}")
    if(dts_rcv_cnt == 0):
        dts_rcv_cnt = 16
    i2c.write16(RX_INTR_CLEAR,0xFF)#clear flag
    read_buf = i2c.wread16(DTS_RCVD_MSG_000,dts_rcv_cnt)
    #print2.print2_hex(read_buf)
    print_hex("read_buf:",read_buf)
    return read_buf

def QIV13_GetDigest():
    print("QIV13_GetDigest")
    QI13_Send([QI13_Head_Digest_Request,0x0F])#19 0f
    # dts_rcv_cnt 34
#  0x11, 0x11, 0x62, 0xE4, 0x34, 0xE7, 0xE8, 0x14, 0xED, 0xAD, 0x6C, 0x60, 0xB6, 0x45, 0x7D, 0x2E,
#  0x49, 0x85, 0x42, 0x72, 0xF7, 0xC9, 0x77, 0x04, 0x7F, 0xEE, 0x96, 0x27, 0x6E, 0x4F, 0xD7, 0x26,
#  0x4E, 0x20,
    
def QIV13_Challenge():
    print("QIV13_Challenge")
    p_challrx = [QI13_Head_Challenge_Request,0x00]
    for i in range(16):#add 16byte random data
        p_challrx.append(random.randint(0,255))
    QI13_Send(p_challrx)

# dts_rcv_cnt 67
#  0x13, 0x11, 0x20, 0x73, 0xA7, 0x7D, 0xA4, 0x8D, 0xC9, 0xB6, 0x04, 0x34, 0xB5, 0x01, 0x85, 0x6A,
#  0x61, 0x75, 0xDD, 0x03, 0x2E, 0x17, 0x26, 0x81, 0xAE, 0xF9, 0x0B, 0x40, 0x93, 0xF7, 0x02, 0xFF,
#  0x34, 0xDE, 0x03, 0x2F, 0xC2, 0x92, 0x9D, 0x16, 0xE4, 0xE8, 0x86, 0x36, 0x22, 0x8D, 0x7B, 0x48,
#  0x79, 0x03, 0xED, 0x1A, 0xBD, 0x8E, 0x4B, 0x76, 0xD7, 0x53, 0xA7, 0x55, 0xB5, 0x7D, 0x57, 0xCC,
#  0xB3, 0xB9, 0xE2,
def QIV13_Certificate1():
    print("QIV13_Certificate1")
    #read first 127 byte
    #SendMsg = [QI13_Head_Certificate_Request,0x00,0x00,0x7F]
    SendMsg = [QI13_Head_Certificate_Request,0x00,0x00,15]
    QI13_Send(SendMsg)

    