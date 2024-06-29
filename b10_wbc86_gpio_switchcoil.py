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
print("example code for STWBC86 to control external 5-coil use gpio0-4")
print("suppose gpio input or low, coil is not selected")
print("suppose gpio high, coil is selected")

print("set TX_PING_INTERVAL make tx ping faster")
wbc86.write16(I2CREG_TX_PING_INTERVAL,10)#unit 10ms set 10 mean 100ms interveral
list_rx_ss = []
for index in range(0,5):
    print(f"set gpio{index} set high to select")
    wbc86.write16(I2CREG_GPIO0_FUNC+index,GPIO_FUNC_PP_HI)
    wbc86.write16(I2CREG_TX_CMD,1<<BIT_TX_EN)
    time.sleep(0.2)
    print("read rx ss packet number")
    rx_ss_strength = wbc86.wread16(I2CREG_SIGNAL_STRENGTH,1)
    list_rx_ss.append(rx_ss_strength)
    print(f"set gpio{index} set low to dis-select")
    wbc86.write16(I2CREG_GPIO0_FUNC+index,GPIO_FUNC_PP_LO)

print("find the max vlaue of rx ss packet and choose to select coils")
max_value = max(list_rx_ss)
max_index = list_rx_ss.index(max_value)
wbc86.write16(I2CREG_GPIO0_FUNC+max_index,GPIO_FUNC_PP_HI)

