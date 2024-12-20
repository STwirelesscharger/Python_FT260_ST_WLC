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
#config must work at bpp mode

Request_WFC_TX = [0x28,0x0C,0x00]#02 01
#Request_WFC_TX2 = [0x28,0x21,0x00]#set pp pwr bud 
Request_WFC_TXID = [0x28,0x01,0x00]#01 21
Request_WFC_PP_SET10V = [0x28,0x06,0x2C]#TX REPLY 0X0A
rx = driver_ft260.ft260_dongle()
rx.wlc89_rom3_info()
#rx.log1()
def wlc89_send_pkt(data =[0x28,0x0C,0x00]):
  rx.write16(0x004E,0x20)#clear intr cmd
  rx.write16(I2CREG_RCVD_MSG_CMD,[0]*3)#clear rcv buff
  rx.write16(I2CREG_SEND_MSG_HDR,data)#W 0X0050
  #rx.write16(I2CREG_CMD,1<<BIT_SEND_MSG)#W 0X004E 0X01
  rx.write16(0x004E,0x01)
  # for item in range(0,10):
  #   time.sleep(0.1)
  #   rx.wread16(0x00EC,2)
  time.sleep(1)
  buff = rx.wread16(I2CREG_RCVD_MSG_CMD,3)
  print(buff)
  #time.sleep(1)

def wlc89_rom3_vout_set(val = 5000):#unit is mV
  if(val > 20000):
    print("wlc89 only support max 20000mV")
    rx_vout_set_register = 828
  elif(val < 3460):
    print("wlc89 only support min 3460mV")
    rx_vout_set_register = 0
  else:
    rx_vout_set_register = int((val-3440)/20)#each bit mean 20mV

  Data16 = rx_vout_set_register.to_bytes(2, byteorder='big')
  send_buff = [Data16[1], Data16[0]]
  rx.write16(I2CREG_RX_VOUT_SET,send_buff)#ROM3 003E

#rx.write16(0x0117,0x04)#enable debug fail packet
#rx.write16(0x004E,0x02)#turn off vout
wlc89_send_pkt(Request_WFC_TX) #tx reply 02 01
time.sleep(1)
#wlc89_send_pkt(Request_WFC_TX2)
#wlc89_send_pkt(Request_WFC_TXID)#tx reply 01 21
wlc89_rom3_vout_set(10000)
wlc89_send_pkt(Request_WFC_PP_SET10V)

