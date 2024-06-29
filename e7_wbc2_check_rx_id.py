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

def wbc2_read(add):
      ser.write([STWBC2_READ_HOST,add])
      buff = ser.read(2)
      if(buff[0] != STWBC2_READ_HOST):
          print("[ERR] read buff[0] 0x{:02X} not equal to 0x72".format(buff[0]))
      return buff[1]


def wbc2_check1():
  print("uart write 0x77 0x02 0x01 to enable check Manufacturer code")
  ser.write([STWBC2_WRITE_HOST,HOST_IF_CTL3,0x01])
  print("write CHECK_RX_MAN_CODE 0x0016 if rx is not ST Manufacturer ID,it will not give power")
  ser.write([STWBC2_WRITE_HOST,CHECK_RX_MAN_CODE_MSB,0x00])
  ser.write([STWBC2_WRITE_HOST,CHECK_RX_MAN_CODE_LSB,0x16])
  #input("put different RX to check")


def wbc2_read_settings1():
      bc2_ctl3 = wbc2_read(HOST_IF_CTL3)

      check_man_codem = wbc2_read(CHECK_RX_MAN_CODE_MSB)
      check_man_codel = wbc2_read(CHECK_RX_DEVICE_ID_3)

      rx_man_codem   =  wbc2_read(HOST_IF_MAN_CODE_MSB)
      rx_man_codel   =  wbc2_read(HOST_IF_MAN_CODE_LSB)
      print(f"bc2_ctl3,{bc2_ctl3},check_man_code,{check_man_codem:X},{check_man_codel:X},rx_man_code,{rx_man_codem:X},{rx_man_codel:X}")


def wbc2_check2():
  print("uart write 0x77 0x02 0x02 to enable check Basic Device id")
  ser.write([STWBC2_WRITE_HOST,HOST_IF_CTL3,0x02])
  print("write CHECK_RX_DEVICE_ID 0x11223344 if rx is not,it will not give power")
  ser.write([STWBC2_WRITE_HOST,CHECK_RX_DEVICE_ID_MSB,0x11])
  ser.write([STWBC2_WRITE_HOST,CHECK_RX_DEVICE_ID_3,0x22])
  ser.write([STWBC2_WRITE_HOST,CHECK_RX_DEVICE_ID_2,0x33])
  ser.write([STWBC2_WRITE_HOST,CHECK_RX_DEVICE_ID_LSB,0x44])
  #input("put different RX to check")

def wbc2_read_settings2():
      bc2_ctl3 = wbc2_read(HOST_IF_CTL3)

      rx_id_pkt = [0]*8
      rx_id_pkt[7]   =  wbc2_read(CHECK_RX_DEVICE_ID_MSB)
      rx_id_pkt[6]   =  wbc2_read(CHECK_RX_DEVICE_ID_3)
      rx_id_pkt[5]   =  wbc2_read(CHECK_RX_DEVICE_ID_2)
      rx_id_pkt[4]   =  wbc2_read(CHECK_RX_DEVICE_ID_LSB)

      rx_id_pkt[3]   =  wbc2_read(HOST_IF_DEVICE_ID_MSB)
      rx_id_pkt[2]   =  wbc2_read(HOST_IF_DEVICE_ID_3)
      rx_id_pkt[1]   =  wbc2_read(HOST_IF_DEVICE_ID_2)
      rx_id_pkt[0]   =  wbc2_read(HOST_IF_DEVICE_ID_LSB)
      print("bc2_ctl3={0} rx_id_pkt=".format(bc2_ctl3), ' '.join( ['0x{:02X}'.format(x) for x in rx_id_pkt]) )

def wbc2_check3():
  print("uart write 0x77 0x02 0x03 to enable check Manufacturer code AND Basic Device id")
  ser.write([STWBC2_WRITE_HOST,HOST_IF_CTL3,0x03])
  print("write CHECK_RX_MAN_CODE 0x0016 if rx is not ST Manufacturer ID,it will not give power")
  ser.write([STWBC2_WRITE_HOST,CHECK_RX_MAN_CODE_MSB,0x00])
  ser.write([STWBC2_WRITE_HOST,CHECK_RX_MAN_CODE_LSB,0x16])
  print("write CHECK_RX_DEVICE_ID 0x11223344 if rx is not,it will not give power")
  ser.write([STWBC2_WRITE_HOST,CHECK_RX_DEVICE_ID_MSB,0x11])
  ser.write([STWBC2_WRITE_HOST,CHECK_RX_DEVICE_ID_3,0x22])
  ser.write([STWBC2_WRITE_HOST,CHECK_RX_DEVICE_ID_2,0x33])
  ser.write([STWBC2_WRITE_HOST,CHECK_RX_DEVICE_ID_LSB,0x44])
  #input("put different RX to check")


print("example of check rx id infor")
print("uart write 0x70 0x05 to disable tx print uart log for better uart communication")
ser.write([STWBC2_SET_PAGE,INDEX_PAGE_LOG_DISABLE,STWBC2_SET_PAGE,INDEX_PAGE_REGS])

# wbc2_check1()
# wbc2_read_settings1()

wbc2_check2()
wbc2_read_settings2()

# wbc2_check3()
# wbc2_read_settings1()
# wbc2_read_settings2()