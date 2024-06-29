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
import serial
from wbc2_register import *

ser = serial.Serial('COM6', 115200, timeout = 1)

#/* tx adc data */
def wbc2_read(add):
      ser.write([STWBC2_READ_HOST,add])
      buff = ser.read(2)
      if(buff[0] != STWBC2_READ_HOST):
          print("[ERR] read buff[0] 0x{:02X} not equal to 0x72".format(buff[0]))
      return buff[1]

def wbc2_read_adc():
  tx_vin = wbc2_read(HOST_IF_ADC_VIN) + wbc2_read(HOST_IF_ADC_VIN+1) * 256
  tx_bridge_mode = wbc2_read(HOST_IF_TX_BRGMODE)
  if(tx_bridge_mode in dic_bridge_mode):
    tx_bridge_mode_info = dic_bridge_mode[tx_bridge_mode]
  else:
    tx_bridge_mode_info = tx_bridge_mode
  tx_duty = wbc2_read(HOST_IF_TX_DUTY)
  tx_vbridge = wbc2_read(HOST_IF_ADC_VBRG) + wbc2_read(HOST_IF_ADC_VBRG+1) * 256
  tx_ibridge = wbc2_read(HOST_IF_ADC_IBRG) + wbc2_read(HOST_IF_ADC_IBRG+1) * 256
  tx_ntc = wbc2_read(HOST_IF_ADC_NTC) + wbc2_read(HOST_IF_ADC_NTC+1) * 256
  tx_freq = wbc2_read(HOST_IF_ADC_FREQ) + wbc2_read(HOST_IF_ADC_FREQ+1) * 256
  tx_freq = tx_freq * 16
  print(f"STWBC2,Vin,{tx_vin},Vbridge,{tx_vbridge},Current,{tx_ibridge},freqHz,{tx_freq},duty,{tx_duty},Mode,{tx_bridge_mode_info},ntc,{tx_ntc}")

def wbc2_read_status():
    tx_status = wbc2_read(HOST_IF_STATUS)
    print(f"tx_status 0x{tx_status:X}")
    if(tx_status & STATUS_OBJECT_DETECTED):
          print("STATUS_OBJECT_DETECTED")
    elif(tx_status & STATUS_QI_POWER):
          print("STATUS_QI_POWER")
    elif(tx_status & STATUS_QI_DETECTED):
          print("STATUS_QI_DETECTED")
    elif(tx_status & STATUS_MEDIUM_POWER):
          print("STATUS_MEDIUM_POWER")
    wbc_qi_fsm = tx_status & 0xF0
    if(wbc_qi_fsm in dic_tx_status):
          wbc_qi_fsm_info = dic_tx_status[wbc_qi_fsm]
    else:
          wbc_qi_fsm_info = "Not find"
    print(wbc_qi_fsm_info)

print("uart write 0x70 0x05 to disable tx print uart log for better uart communication")
ser.write([STWBC2_SET_PAGE,INDEX_PAGE_LOG_DISABLE,STWBC2_SET_PAGE,INDEX_PAGE_REGS])
wbc2_read_adc()
wbc2_read_status()
# tx_status 0xB2
# STATUS_QI_POWER
# POWER_TRANSFER_STATE

# uart write 0x70 0x05 to disable tx print uart log for better uart communication
# STWBC2,Vin,9230,Vbridge,13619,Current,105,freqHz,110624,duty,50,Mode,HALF,ntc,30
# tx_status 0xB0
# POWER_TRANSFER_STATE
