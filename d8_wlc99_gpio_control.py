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
wlc99 = driver_ft260.ft260_dongle(i2c_speed = 100,dev_addr_set = 0x2C)
wlc99.chip_info()

print("example code set gpio0 pin input float")
wlc99.write16(I2CREG_GPIO0_FUNC,GPIO_FUNC_IN_FL)
time.sleep(1)

print("example code set gpio0 pin pp high")
wlc99.write16(I2CREG_GPIO0_FUNC,GPIO_FUNC_PP_HI)
time.sleep(1)
print("example code set gpio0 pin pp low")
wlc99.write16(I2CREG_GPIO0_FUNC,GPIO_FUNC_PP_LO)
time.sleep(1)
print("example code set gpio0 pin as ask block feature")
wlc99.write16(I2CREG_GPIO0_FUNC,GPIO_FUNC_RX_DIS_COM)
print("extern use 1.8V to GPIO0 and will block ask communication")
print("if you want use other gpio, just set other gpio to this feature")
wlc99.write16(I2CREG_GPIO1_FUNC,GPIO_FUNC_RX_DIS_COM)
print("extern use 1.8V to GPIO0 and will block ask communication")

print("set gpio 0 as power good indicate")
wlc99.write16(I2CREG_GPIO0_FUNC,GPIO_FUNC_RX_PWR_OUT)

# Open FT260 device OK
# [WR],@0x0x10 >> 0x00 0x35 0x38 0x30 0x38 0x52 0x36 0x47 0x0D 0x00 0x00 0x00 0x1B 0x00 0x20 0x00
# Device ID 0x: 00353830385236470D0000001B002000
# [WR],@0x0x0 >> 0x63 0x00 0x02 0x00 0x55 0x01 0x60 0x12 0x00 0x00 0x00 0x2C 0x07 0x07 0x00 0x00
# ChipID:0x0063 rev:2 patchid:0x1260 cfgid:0x2C00
# CHIPID_WLC99
# example code set gpio0 pin input float
# [W],@0x30 >> 0x0
# example code set gpio0 pin pp high
# [W],@0x30 >> 0x4
# example code set gpio0 pin pp low
# [W],@0x30 >> 0x3
