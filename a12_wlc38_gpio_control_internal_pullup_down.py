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
print("example code for control gpio internal pull up or down")

def wlc38_gpio_read_internal():
  #xx
  wlc38.wreadFA(HWREG_GPIO_PULL_EN_RegAddr)
  wlc38.wreadFA(HWREG_GPIO_PULL_UP_DN_RegAddr)

def wlc38_gpio_test1():
  print("example code set gpio1 internal pull disable")
  print('read and clear this bit')
  val = wlc38.wreadFA(HWREG_GPIO_PULL_EN_RegAddr)
  val &= ~(1<<GPIO_ID1);
  wlc38.writeFA(HWREG_GPIO_PULL_EN_RegAddr,val)

  wlc38.writeFA(HWREG_GPIO_PULL_EN_RegAddr,1<<GPIO_ID1)

  print("example code set gpio1 internal pull enable")
  wlc38.writeFA(HWREG_GPIO_PULL_EN_RegAddr,1<<GPIO_ID1)

  print("example code set gpio1 internal pull up enable")
  wlc38.writeFA(HWREG_GPIO_PULL_UP_DN_RegAddr,1<<GPIO_ID1)

  print("example code set gpio1 internal pull down enable")
  print('read and clear this bit')
  val = wlc38.wreadFA(HWREG_GPIO_PULL_UP_DN_RegAddr)
  val &= ~(1<<GPIO_ID1);
  wlc38.writeFA(HWREG_GPIO_PULL_UP_DN_RegAddr,val)

wlc38_gpio_read_internal()
wlc38_gpio_test1()

#test log
# example code for control gpio internal pull up or down
# R FA @0x2001A010 = 0x06
# R FA @0x2001A014 = 0x08

# example code set gpio1 internal pull disable
# read and clear this bit
# R FA @0x2001A010 = 0x06
# W @0x2001a010 = 0x04

# W @0x2001a010 = 0x02
# example code set gpio1 internal pull enable
# W @0x2001a010 = 0x02
# example code set gpio1 internal pull up enable
# W @0x2001a014 = 0x02
# example code set gpio1 internal pull down enable
# read and clear this bit
# R FA @0x2001A014 = 0x02
# W @0x2001a014 = 0x00
