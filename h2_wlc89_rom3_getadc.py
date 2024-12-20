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
i2c = driver_ft260.ft260_dongle()
i2c.log1()

def wlc89_rom3_adc_data():
    vout_meas = i2c.wread16(I2CREG_VOUT_MEAS,2)
    vrect_meas = i2c.wread16(I2CREG_VRECT_MEAS,2)
    icur_meas = i2c.wread16(I2CREG_ICUR_MEAS,2)
    chip_temp = i2c.wread16(I2CREG_CHIP_TEMP_MEAS,2) / 10
    opfreq = i2c.wread16(I2CREG_OP_FREQ,2)
    rp_pwr = i2c.wread16(I2CREG_RX_RCVD_PWR,2)
    mode = i2c.wread16(I2CREG_RXOP_MODE)
    print(f"wlc89_rom3,vrect,{vrect_meas},vout,{vout_meas},curr,{icur_meas},die,{chip_temp}C,freq,{opfreq}khz,rp,{rp_pwr}")
    if(32 == mode):
        print("BPP")
    elif(64 == mode):
        print("EPP")
    elif(32*4 == mode):
        print("MPP")
wlc89_rom3_adc_data()

# Open FT260 device OK
# [WR],@0x0x3c >> 0x76 0x13
# [WR],@0x0x40 >> 0x57 0x16
# [WR],@0x0x44 >> 0x43 0x00
# [WR],@0x0x46 >> 0x7A 0x01
# [WR],@0x0x48 >> 0x92 0x00
# wlc89_rom3,vrect,5719,vout,4982,curr,67,die,37.8,freq,146khz
