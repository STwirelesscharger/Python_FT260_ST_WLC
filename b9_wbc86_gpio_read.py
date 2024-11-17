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
from wbc86_register import *
import time
wbc86 = driver_ft260.ft260_dongle()
wbc86.chip_info()
print("example code set gpio pin as input floating and read gpio status")
print("connect external 1.8V to GPIO1")
wbc86.write16(I2CREG_GPIO0_FUNC,GPIO_FUNC_IN_PD)
wbc86.write16(I2CREG_GPIO1_FUNC,GPIO_FUNC_IN_PD)

value = wbc86.wreadFA(HWREG_GPIO_INPUT_VAL_RegAddr)
print(f"gpio input value 0x{value:X}")
if(value & 0x01):
    print("gpio0 input high")
else:
    print("gpio0 input low")
if(value & 0x02):
    print("gpio1 input high")
else:
    print("gpio1 input low")

GPIO_PULL_UP_DN_RegAddr = 0x2001A014
# GPIO_PULL_UP_DN_RegAddr is 0x2001A014 
# set 1 mean internal pull up
# set 0 mean internal pull down
wbc86.writeFA(0x2001A014,0x00)#set all gpio internal pull down

# GPIO_PULL_EN_RegAddr is 0x2001A010 
# set 1 mean enable internal pull up or down
# set 0 mean disable
GPIO_PULL_EN_RegAddr = 0x2001A010
wbc86.writeFA(0x2001A010,0x00)#disable all gpio internal

#test log
# Open FT260 device OK
# [WR],@0x0x10 >> 0x00 0x31 0x36 0x30 0x31 0x53 0x36 0x47 0x0B 0x00 0x00 0x00 0x17 0x00 0x33 0x00
# Device ID 0x: 00313630315336470B00000017003300
# [WR],@0x0x0 >> 0x56 0x00 0x02 0x00 0x18 0x01 0x42 0x12 0x00 0x00 0x0D 0x12 0x01 0x04 0x03 0x01
# ChipID:0x0056 rev:2 patchid:0x1242 cfgid:0x120D
# CHIPID_WBC86
# example code set gpio pin as input floating and read gpio status
# connect external 1.8V to GPIO1
# R FA @0x2001A01C = 0x02
# gpio input value 0x2
# gpio0 input low
# gpio1 input high
