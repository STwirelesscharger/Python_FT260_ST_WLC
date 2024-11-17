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
from wlc99_register import *
import time

STSC_RP24_Req= [0x48, 0x24, 0x52, 200, 0x00]
STSC_5V_Req  = [0x48, 0x73, 0x00, 0x88, 0x13] #0X1388 = 5000
STSC_9V_Req  = [0x48, 0x73, 0x00, 0x28, 0x23] #0X2328 = 9000
STSC_12V_Req = [0x48, 0x73, 0x00, 0xE0, 0x2E] #0X2EE0 = 12000
STSC_15V_Req = [0x48, 0x73, 0x00, 0x98, 0x3A] #0X3A98 = 15000
STSC_18V_Req = [0x48, 0x73, 0x00, 0x50, 0x46] #0X4650 = 18000
STSC_20V_Req = [0x48, 0x73, 0x00, 0x20, 0x4E] #0X4E20 = 20000
STSC_FIX_FREQ150K= [0x48, 0x68, 0x11, 150, 150]
STSC_FIX_FREQ140K= [0x48, 0x68, 0x11, 140, 140]

wlc99 = driver_ft260.ft260_dongle(i2c_speed = 100,dev_addr_set = 0x2C)
wlc99.chip_info()

def wlc99_send_pp(packet = [0x48, 0x73, 0x00, 0x28, 0x23]):
    print("[STEP],wlc99_send_pp:" +' '.join( ['0x{:02X},'.format(x) for x in packet]) )
    wlc99.write16(I2CREG_RCVD_MSG,[0x00]*4)
    wlc99.write16(I2CREG_SEND_MSG,packet)#rx send 0x38 0x3B 0x88 0x66 packet
    wlc99.write16(I2CREG_RX_CMD,(1<<BIT_RX_SEND_MSG_WAIT_REPLY))
    time.sleep(0.5)
    tx_reply_data = wlc99.wread16(I2CREG_RCVD_MSG,3)
    print("get tx fsk:" +' '.join( ['0x{:02X},'.format(x) for x in tx_reply_data]) )
    if(0x1E == tx_reply_data[0]):
        return True
    else:
        return False

def wlc99_send_pp_retry(packet = [0x48, 0x73, 0x00, 0x28, 0x23]):
    for item in range(0,3):
        isOk = wlc99_send_pp(packet)
        if(isOk):
            print("[PASS],TX_ACK")
            break
        else:
            print("[RETRY]")
    if(False == isOk):
        print("[FAIL],wlc99_send_pp_retry")
    return isOk

def wlc99_getadc():#wlc99
    time.sleep(1)
    freq = wlc99.wread16(I2CREG_OP_FREQ,2)
    iin = wlc99.wread16(I2CREG_MEAS_S32,2)
    read_buff = wlc99.wread16(I2CREG_MEAS_S16,12)
    vrect = read_buff[0] + read_buff[1] * 256
    vout  = read_buff[2] + read_buff[3] * 256
    die   = read_buff[4] + read_buff[5] * 256
    die /= 10
    ntc   = read_buff[8] + read_buff[9] * 256
    ntc *= 0.164795
    print(f"[ADC],vrect/mV,{vrect},vout/mV,{vout},cur/mA,{iin},die/C,{die},freq/khz,{freq},ntc,{ntc}mV")


def wlc99_stsc_seq():
    isOk = wlc99_send_pp_retry(STSC_RP24_Req)
    if(False == isOk):
        return
    wlc99.write16(I2CREG_RX_SC_RP24_MAX_PWR,200) #SET Ref power to 100W
    wlc99.write16(I2CREG_MAX_PWR_SWICH,1)
    wlc99_getadc()

    isOk = wlc99_send_pp_retry(STSC_12V_Req)
    if(False == isOk):
        return
    wlc99.wlc99_vout_set(12000)
    wlc99_getadc()

    isOk = wlc99_send_pp_retry(STSC_15V_Req)
    if(False == isOk):
        return
    wlc99.wlc99_vout_set(15000)
    wlc99_getadc()

    isOk = wlc99_send_pp_retry(STSC_20V_Req)
    if(False == isOk):
        return
    wlc99.wlc99_vout_set(20000)
    wlc99_getadc()

wlc99_stsc_seq()

