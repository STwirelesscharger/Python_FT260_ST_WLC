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
print("example code for STWBC86 to control external GPIO/LED")
print("GPIO0 connect LED Red, GPIO1 connect LED Green")

def LED_RED_CTL(isOn = True):
    if(isOn):
        wbc86.write16(I2CREG_GPIO0_FUNC,GPIO_FUNC_PP_LO)
    else:
        wbc86.write16(I2CREG_GPIO0_FUNC,GPIO_FUNC_PP_HI)

def LED_GREEN_CTL(isOn = True):
    if(isOn):
        wbc86.write16(I2CREG_GPIO1_FUNC,GPIO_FUNC_PP_LO)
    else:
        wbc86.write16(I2CREG_GPIO1_FUNC,GPIO_FUNC_PP_HI)

def LED_CTL_Example1():
    print("MCU read tx ept reason")
    ept_reason = wbc86.wread16(I2CREG_TX_EPT_REASON_RCVD,3)
    if(ept_reason[0] != 0) | (ept_reason[1] != 0) | (ept_reason[2] != 0):
        print("tx have some error set LED RED ON")
        LED_RED_CTL(True)
    else:
        LED_RED_CTL(False)

def LED_CTL_Example2():
    print("when connecting the cable (1s or 2s) and then off")
    LED_GREEN_CTL(True)
    time.sleep(1)
    LED_GREEN_CTL(False)
