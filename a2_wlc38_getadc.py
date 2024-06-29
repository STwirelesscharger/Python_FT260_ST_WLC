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

wlc38 = driver_ft260.ft260_dongle()
wlc38.chip_info()

def wlc38_getadc():
    read_buff = wlc38.wread16(I2CREG_RX_VRECT,12)
    vrect = read_buff[0] + read_buff[1] * 256
    vout  = read_buff[2] + read_buff[3] * 256
    iin   = read_buff[4] + read_buff[5] * 256
    die   = read_buff[6] + read_buff[7] * 256
    die /= 10
    freq  = read_buff[8] + read_buff[9] * 256
    ntc   = read_buff[10] + read_buff[11] * 256
    if(ntc < 32768):
        ntc = (ntc*3600/16384)+1800
    else:
        ntc = 1800-((65536-ntc)*3600/16384)
    print(f"rx,vrect/mV,{vrect},vout/mV,{vout},cur/mA,{iin},die/C,{die},freq/khz,{freq},ntc/mV,{ntc}")

    RX_PTC_FSK_CFG = wlc38.wread16(I2CREG_RX_PTC_FSK_CFG,1)
    isEPP = (1 << BIT_RX_NEG) & RX_PTC_FSK_CFG
    if(0 == isEPP):
        print("BPP Mode")
    else:
        print("EPP Mode")

    read_buff = wlc38.wread16(I2CREG_RX_CTRL_ERR,5)
    rx_ctrl_err = read_buff[0] + read_buff[1] * 256
    if(rx_ctrl_err > 0x7FF):
        rx_ctrl_err = rx_ctrl_err - 0XFFFF
    rx_ctrl_err /= 256
    rx_rcvd_pwr = read_buff[2] + read_buff[3] * 256
    rx_signal_strength = read_buff[4]
    print(f"rx_ctrl_err/mV,{rx_ctrl_err},rx_rcvd_pwr/mW,{rx_rcvd_pwr},rx_signal_strength,{rx_signal_strength}")

wlc38_getadc()

#test log
# Open FT260 device OK
# [WR],@0x0x10 >> 0x00 0x5A 0x34 0x30 0x32 0x54 0x55 0xAA 0x02 0x53 0x3C 0x0F 0x55 0xAA 0x55 0xAA
# Device ID 0x: 005A3430325455AA02533C0F55AA55AA
# [WR],@0x0x0 >> 0x26 0x00 0x03 0x00 0x61 0x01 0x37 0x14 0x00 0x00 0x47 0x1F 0x07 0x00 0x02 0x51
# ChipID:0x0026 rev:3 patchid:0x1437 cfgid:0x1F47
# CHIPID_WLC38
# [WR],@0x0x92 >> 0xBE 0x14 0x7E 0x13 0x2B 0x00 0x14 0x01 0x92 0x00 0x8B 0xE7
# rx,vrect/mV,5310,vout/mV,4990,cur/mA,43,die/C,27.6,freq/khz,146,,ntc/mV,430.6640625
# [WR],@0x0xad >> 0x01
# BPP Mode
# [WR],@0x0xa4 >> 0x7E 0xFF 0xFF 0x01 0x94
# rx_ctrl_err/mV,-0.50390625,rx_rcvd_pwr/mW,511,rx_signal_strength,148
