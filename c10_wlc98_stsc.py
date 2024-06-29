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

STSC_RP24_Req= [0x48, 0x24, 0x52, 0x64, 0x00]
STSC_9V_Req  = [0x48, 0x73, 0x00, 0x28, 0x23]
STSC_12V_Req = [0x48, 0x73, 0x00, 0xE0, 0x2E]
STSC_15V_Req = [0x48, 0x73, 0x00, 0x98, 0x3A]
STSC_18V_Req = [0x48, 0x73, 0x00, 0x50, 0x46]
STSC_20V_Req = [0x48, 0x73, 0x00, 0x20, 0x4E]
STSC_FIX_FREQ= [0x48, 0x68, 0x11, 140, 140]


wlc98 = driver_ft260.ft260_dongle()
wlc98.chip_info()

def wlc98_send_pp(packet = [0x48, 0x73, 0x00, 0x28, 0x23]):
    print("wlc99_send_pp:" +' '.join( ['0x{:02X},'.format(x) for x in packet]) )
    wlc98.write16(I2CREG_RCVD_MSG,[0x00]*4)
    wlc98.write16(I2CREG_SEND_MSG,packet)#rx send 0x38 0x3B 0x88 0x66 packet
    wlc98.write16(I2CREG_RX_CMD,(1<<BIT_RX_SEND_MSG_WAIT_REPLY))
    time.sleep(0.5)
    tx_reply_data = wlc98.wread16(I2CREG_RCVD_MSG,3)
    print("get tx fsk:" +' '.join( ['0x{:02X},'.format(x) for x in tx_reply_data]) )
    if(0x1E == tx_reply_data[0]):
        return True
    else:
        return False

def wlc98_send_pp_retry(packet = [0x48, 0x73, 0x00, 0x28, 0x23]):
    for item in range(0,3):
        isOk = wlc98_send_pp(packet)
        if(isOk):
            print("[PASS]")
            break
    if(False == isOk):
        print("[FAIL] wlc98_send_pp_retry")
    return isOk

def wlc98_getadc():#wlc98
    time.sleep(1)
    read_buff = wlc98.wread16(I2CREG_RX_VRECT,10)
    vrect = read_buff[0] + read_buff[1] * 256
    vout  = read_buff[2] + read_buff[3] * 256
    iin   = read_buff[4] + read_buff[5] * 256
    die   = read_buff[6] + read_buff[7] * 256
    die /= 10
    freq  = read_buff[8] + read_buff[9] * 256
    print(f"[ADC],vrect/mV,{vrect},vout/mV,{vout},cur/mA,{iin},die/C,{die},freq/khz,{freq}")

def wlc98_stsc_seq():
    wlc98_getadc()
    isOk = wlc98_send_pp_retry(STSC_RP24_Req)
    if(False == isOk):
        return
    wlc98.write16(I2CREG_SC_MAX_PWR,0x64)
    wlc98.write16(I2CREG_MAX_PWR_SWICH,1)

    print("[STEP] STSC_12V_Req")
    isOk = wlc98_send_pp_retry(STSC_12V_Req)
    if(False == isOk):
        return
    wlc98.wlc98_vout_set(12000)
    wlc98_getadc()
    print("[STEP] STSC_15V_Req")
    isOk = wlc98_send_pp_retry(STSC_15V_Req)
    if(False == isOk):
        return
    wlc98.wlc98_vout_set(15000)
    wlc98_getadc()
    print("[STEP] STSC_20V_Req")
    isOk = wlc98_send_pp_retry(STSC_20V_Req)
    if(False == isOk):
        return
    wlc98.wlc98_vout_set(20000)
    wlc98_getadc()

wlc98_stsc_seq()
# test logs
# Open FT260 device OK
# [WR],@0x0x10 >> 0x00 0x34 0x31 0x30 0x32 0x35 0x30 0x51 0x14 0x00 0x00 0x00 0x19 0x00 0x19 0x00
# Device ID 0x: 00343130323530511400000019001900
# [WR],@0x0x0 >> 0x62 0x00 0x02 0x00 0x01 0x02 0x54 0x14 0x00 0x00 0x00 0x2C 0x06 0x00 0x02 0x52
# ChipID:0x0062 rev:2 patchid:0x1454 cfgid:0x2C00
# CHIPID_WLC98
# [WR],@0x0x92 >> 0xDD 0x23 0x56 0x23 0x76 0x00 0x3B 0x01 0x7A 0x00
# [ADC],vrect/mV,9181,vout/mV,9046,cur/mA,118,die/C,31.5,freq/khz,122
# wlc99_send_pp:0x48, 0x24, 0x52, 0x64, 0x00,
# [W],@0x0x190 >> 0x00 0x00 0x00 0x00
# [W],@0x0x180 >> 0x48 0x24 0x52 0x64 0x00
# [W],@0x90 >> 0x8
# [WR],@0x0x190 >> 0x1E 0x01 0x1F
# get tx fsk:0x1E, 0x01, 0x1F,
# [PASS]
# [W],@0xE2 >> 0x64
# [W],@0xE3 >> 0x1
# [STEP] STSC_12V_Req
# wlc99_send_pp:0x48, 0x73, 0x00, 0xE0, 0x2E,
# [W],@0x0x190 >> 0x00 0x00 0x00 0x00        
# [W],@0x0x180 >> 0x48 0x73 0x00 0xE0 0x2E   
# [W],@0x90 >> 0x8
# [WR],@0x0x190 >> 0x1E 0x01 0x1F
# get tx fsk:0x1E, 0x01, 0x1F,
# [PASS]
# [W],@0x0xb4 >> 0xE0 0x01
# [WR],@0x0x92 >> 0x6E 0x2C 0x6D 0x2C 0x76 0x00 0x3D 0x01 0x6E 0x00
# [ADC],vrect/mV,11374,vout/mV,11373,cur/mA,118,die/C,31.7,freq/khz,110
# [STEP] STSC_15V_Req
# wlc99_send_pp:0x48, 0x73, 0x00, 0x98, 0x3A,
# [W],@0x0x190 >> 0x00 0x00 0x00 0x00
# [W],@0x0x180 >> 0x48 0x73 0x00 0x98 0x3A
# [W],@0x90 >> 0x8
# [WR],@0x0x190 >> 0x00 0x00 0x00
# get tx fsk:0x00, 0x00, 0x00,
# wlc99_send_pp:0x48, 0x73, 0x00, 0x98, 0x3A,
# [W],@0x0x190 >> 0x00 0x00 0x00 0x00
# [W],@0x0x180 >> 0x48 0x73 0x00 0x98 0x3A
# [W],@0x90 >> 0x8
# [WR],@0x0x190 >> 0x1E 0x01 0x1F
# get tx fsk:0x1E, 0x01, 0x1F,
# [PASS]
# [W],@0x0xb4 >> 0x58 0x02
# [WR],@0x0x92 >> 0xE6 0x38 0xE8 0x38 0x77 0x00 0x41 0x01 0x6D 0x00
# [ADC],vrect/mV,14566,vout/mV,14568,cur/mA,119,die/C,32.1,freq/khz,109
# [STEP] STSC_20V_Req
# wlc99_send_pp:0x48, 0x73, 0x00, 0x20, 0x4E,
# [W],@0x0x190 >> 0x00 0x00 0x00 0x00
# [W],@0x0x180 >> 0x48 0x73 0x00 0x20 0x4E
# [W],@0x90 >> 0x8
# [WR],@0x0x190 >> 0x1E 0x01 0x1F
# get tx fsk:0x1E, 0x01, 0x1F,
# [PASS]
# [W],@0x0xb4 >> 0x20 0x03
# [WR],@0x0x92 >> 0x60 0x4B 0x56 0x4B 0x77 0x00 0x4B 0x01 0x6D 0x00
# [ADC],vrect/mV,19296,vout/mV,19286,cur/mA,119,die/C,33.1,freq/khz,109


