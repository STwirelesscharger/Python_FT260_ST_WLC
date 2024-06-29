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

INDEX_FW_VERSION_MAJ1                   = 0x0A
INDEX_FW_VERSION_MAJ2                   = 0x0B
INDEX_FW_VERSION_MIN1                   = 0x0C
INDEX_FW_VERSION_MIN2                   = 0x0D

ser = serial.Serial('COM6', 115200, timeout = 1)

def wbc2_read_fwversion():
  uart_cmd_fwversion = [STWBC2_SET_PAGE,INDEX_PAGE_PARAM,
                        STWBC2_READ_HOST,INDEX_FW_VERSION_MAJ2,
                        STWBC2_READ_HOST,INDEX_FW_VERSION_MAJ1,
                        STWBC2_READ_HOST,INDEX_FW_VERSION_MIN2,
                        STWBC2_READ_HOST,INDEX_FW_VERSION_MIN1]
  #set page2
  ser.write(uart_cmd_fwversion)
  print("uart write: 0x70 0x02 0x72 0x0B 0x72 0x0A 0x72 0x0D 0x72 0x0C")
  buff = ser.read(8)
  print("uart read: " +' '.join( ['0x{:02X}'.format(x) for x in buff]))
  print("FW Version, {}.{}.{}.{}".format(buff[1],buff[3],buff[5],buff[7]))
  #set back to page0
  ser.write([STWBC2_SET_PAGE,INDEX_PAGE_REGS])

print("put rx on tx and will enter to power transfer")

print("uart write 0x70 0x05 to disable tx print uart log for better uart communication")
ser.write([STWBC2_SET_PAGE,INDEX_PAGE_LOG_DISABLE,STWBC2_SET_PAGE,INDEX_PAGE_REGS])

wbc2_read_fwversion()

print("uart write 0x77 0x00 0x01")
ser.write([STWBC2_WRITE_HOST,HOST_IF_CTL1,1<<BIT_CTL1_TX_DIS])
input("check tx is stop working")

print("set tx resume to give power to rx")
print("uart write 0x77 0x00 0x00")
ser.write([STWBC2_WRITE_HOST,HOST_IF_CTL1,0])
input("check tx is working again")

print("uart write 0x70 0x07")
ser.write([STWBC2_SET_PAGE,INDEX_PAGE_TXPWR_DIS])
input("check tx is stop working")

print("uart write 0x70 0x06")
ser.write([STWBC2_SET_PAGE,INDEX_PAGE_TXPWR_EN])
input("check tx is working again")

