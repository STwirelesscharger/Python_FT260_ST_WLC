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

EPT_UNKNOWN                 = 0x00,             #///< Unknown (No specific/appropriate code)
EPT_CHARGE_COMPLETE         = 0x01,             #///< Charge Complete (Charge full)
EPT_INTERNAL_FAULT          = 0x02,             #///< Internal Fault (Rx software or logic error)
EPT_OVER_TEMP               = 0x03,             #///< Over Temperature (Rx device over temperature)
EPT_OVER_VOLTAGE            = 0x04,             #///< Over Voltage (Rx device over voltage)
EPT_OVER_CURRENT            = 0x05,             #///< Over Current (Rx device over current)
EPT_BAT_FAILURE             = 0x06,             #///< Battery Failure (Rx device battery problem)
EPT_UNDER_VOLTAGE           = 0x07,             #///< Under Voltage (Rx device vout under voltage)
EPT_NO_RESPONSE             = 0x08,             #///< No Response (Tx not adjusting according to CE)
EPT_RESERVED1               = 0x09,             #///< Reserved
EPT_NEGO_FAIL               = 0x0A,             #///< Negotiation Failure (EPP, no suitable GP)
EPT_RESTART_POWER_TRANSFER  = 0x0B,             #///< Restart Power Transfer (EPP, start no power transfer FOD)

wlc38 = driver_ft260.ft260_dongle()
wlc38.chip_info()

wlc38.write16(I2CREG_RX_EPT_MSG,EPT_RESTART_POWER_TRANSFER)
wlc38.write16(I2CREG_RX_CMD,(1<<BIT_RX_SEND_EPT))#rx send ept
