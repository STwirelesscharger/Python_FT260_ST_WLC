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
import driver_ft260
from wlc98_register import *
import time
ser = None
wlc98 = None

def wbc2_read(add):
    ser.write([STWBC2_READ_HOST,add])
    buff = ser.read(2)
    if(buff[0] != STWBC2_READ_HOST):
        print("[WBC2_ERR] read buff[0] 0x{:02X} not equal to 0x72".format(buff[0]))
    return buff[1]

def wbc2_init(port_name = 'COM6'):
    global ser
    ser = serial.Serial(port_name, 115200, timeout = 1)
    print("uart write 0x70 0x05 to disable tx print uart log for better uart communication")
    ser.write([STWBC2_SET_PAGE,INDEX_PAGE_LOG_DISABLE,STWBC2_SET_PAGE,INDEX_PAGE_REGS])
    print("uart write 0x77 0x01 0x01 set enable response to rx data")
    ser.write([STWBC2_WRITE_HOST,HOST_IF_CTL2,1<<BIT_CTL2_RSP_ASKPP])

def wbc2_set_fskdata(fsk_head = 0x1E,data = [0x11,0x22,0x33,0x44,0x55]):
    print(f"[TX] wbc2_set_fskdata: fsk_head=0x{fsk_head:X}, Data=", ' '.join( ['0x{:02X}'.format(x) for x in data]) )
    if(FSK_PP_HEAD_0x1E == fsk_head):
      ser.write([STWBC2_WRITE_HOST,HOST_IF_TX_SEND_MSG_1E,data[0]])
    elif(FSK_PP_HEAD_0x1F == fsk_head):
      ser.write([STWBC2_WRITE_HOST,HOST_IF_TX_SEND_MSG_1F,data[0]])
    elif(FSK_PP_HEAD_0x2E == fsk_head):
      ser.write([STWBC2_WRITE_HOST,HOST_IF_TX_SEND_MSG_2E,data[0]])
      ser.write([STWBC2_WRITE_HOST,HOST_IF_TX_SEND_MSG_2E+1,data[1]])
    elif(FSK_PP_HEAD_0x2F == fsk_head):
      ser.write([STWBC2_WRITE_HOST,HOST_IF_TX_SEND_MSG_2F,data[0]])
      ser.write([STWBC2_WRITE_HOST,HOST_IF_TX_SEND_MSG_2F+1,data[1]])
    elif(FSK_PP_HEAD_0x3F == fsk_head):
      ser.write([STWBC2_WRITE_HOST,HOST_IF_TX_SEND_MSG_3F,data[0]])
      ser.write([STWBC2_WRITE_HOST,HOST_IF_TX_SEND_MSG_3F+1,data[1]])
      ser.write([STWBC2_WRITE_HOST,HOST_IF_TX_SEND_MSG_3F+2,data[2]])
    elif(FSK_PP_HEAD_0x4F == fsk_head):
      ser.write([STWBC2_WRITE_HOST,HOST_IF_TX_SEND_MSG_4F,data[0]])
      ser.write([STWBC2_WRITE_HOST,HOST_IF_TX_SEND_MSG_4F+1,data[1]])
      ser.write([STWBC2_WRITE_HOST,HOST_IF_TX_SEND_MSG_4F+2,data[2]])
      ser.write([STWBC2_WRITE_HOST,HOST_IF_TX_SEND_MSG_4F+3,data[3]])
    elif(FSK_PP_HEAD_0x5F == fsk_head):
      ser.write([STWBC2_WRITE_HOST,HOST_IF_TX_SEND_MSG_5F,data[0]])
      ser.write([STWBC2_WRITE_HOST,HOST_IF_TX_SEND_MSG_5F+1,data[1]])
      ser.write([STWBC2_WRITE_HOST,HOST_IF_TX_SEND_MSG_5F+2,data[2]])
      ser.write([STWBC2_WRITE_HOST,HOST_IF_TX_SEND_MSG_5F+3,data[3]])
      ser.write([STWBC2_WRITE_HOST,HOST_IF_TX_SEND_MSG_5F+4,data[4]])
    elif(FSK_PP_HEAD_0x6F == fsk_head):
      ser.write([STWBC2_WRITE_HOST,HOST_IF_TX_SEND_MSG_6F,data[0]])
      ser.write([STWBC2_WRITE_HOST,HOST_IF_TX_SEND_MSG_6F+1,data[1]])
      ser.write([STWBC2_WRITE_HOST,HOST_IF_TX_SEND_MSG_6F+2,data[2]])
      ser.write([STWBC2_WRITE_HOST,HOST_IF_TX_SEND_MSG_6F+3,data[3]])
      ser.write([STWBC2_WRITE_HOST,HOST_IF_TX_SEND_MSG_6F+4,data[4]])
      ser.write([STWBC2_WRITE_HOST,HOST_IF_TX_SEND_MSG_6F+5,data[5]])
    elif(FSK_PP_HEAD_0x7F == fsk_head):
      ser.write([STWBC2_WRITE_HOST,HOST_IF_TX_SEND_MSG_7F,data[0]])
      ser.write([STWBC2_WRITE_HOST,HOST_IF_TX_SEND_MSG_7F+1,data[1]])
      ser.write([STWBC2_WRITE_HOST,HOST_IF_TX_SEND_MSG_7F+2,data[2]])
      ser.write([STWBC2_WRITE_HOST,HOST_IF_TX_SEND_MSG_7F+3,data[3]])
      ser.write([STWBC2_WRITE_HOST,HOST_IF_TX_SEND_MSG_7F+4,data[4]])
      ser.write([STWBC2_WRITE_HOST,HOST_IF_TX_SEND_MSG_7F+5,data[5]])
      ser.write([STWBC2_WRITE_HOST,HOST_IF_TX_SEND_MSG_7F+6,data[6]])
    else:
      print(f"[ERR] fsk_head {fsk_head} not support")

def wbc2_read_rx_rcvd(data_size = 2):
    wbc2_read_rx_rcvd_buff = [0] * data_size
    for index in range(0,data_size):
      wbc2_read_rx_rcvd_buff[index] = wbc2_read(HOST_IF_RX_RCVD_MSG+index)
    return wbc2_read_rx_rcvd_buff

def wbc2_read_isgetaskpp():
    host_if_ctl2 = wbc2_read(HOST_IF_CTL2)
    if(host_if_ctl2 & 0x02):
        print("[TX] Get RX ASK PP packet")
        #clear this bit for next rx ask pp packet
        ser.write([STWBC2_WRITE_HOST,HOST_IF_CTL2,0x01])
    else:
        print("[ERR] TX Not Get RX ASK PP packet")

def wlc98_init():
    global wlc98
    wlc98 = driver_ft260.ft260_dongle()
    (patchid,cfgid,chipid) = wlc98.chip_info()
    if(chipid != 0x0062):
          print("[ERR] Rx chipid is not wlc98")
          wlc98 = None
    return wlc98

def wlc98_send_ask_pkt(rx_ask_pkt = [0x18,0x1E],rcv_size = 2):
      print(f"[RX] send ASK PP size {rcv_size} Data: ", ' '.join( ['0x{:02X}'.format(x) for x in rx_ask_pkt]) )
      wlc98.write16(I2CREG_RCVD_MSG,[0]*8)#clear fsk buff
      wlc98.write16(I2CREG_SEND_MSG,rx_ask_pkt)#rx send pp packet
      wlc98.write16(I2CREG_RX_CMD,(1<<BIT_RX_SEND_MSG_WAIT_REPLY))
      time.sleep(1)
      tx_reply_data = wlc98.wreadbuff(I2CREG_RCVD_MSG,rcv_size)#0X0190
      print("[RX] tx_reply_data: ", ' '.join( ['0x{:02X}'.format(x) for x in tx_reply_data]) )
      return tx_reply_data

def wlc98_wbc2_communitation(rx_send_pp=[0x18,0x1E],tx_rsp_pp=[0x1E,0x11],data_size = 8):
    fsk_data = tx_rsp_pp[1:]
    wbc2_set_fskdata(tx_rsp_pp[0],fsk_data)
    tx_reply_data = wlc98_send_ask_pkt(rx_send_pp,data_size)
    if(tx_reply_data != tx_rsp_pp):
        print("[ERR] rx get fsk data != tx fsk send data")
        print("tx_reply_data: ", ' '.join( ['0x{:02X}'.format(x) for x in tx_reply_data]) )
        print("tx_rsp_pp: ", ' '.join( ['0x{:02X}'.format(x) for x in tx_rsp_pp]) )
    else:
        print("[PASS] rx get fsk data = tx fsk send data")
    wbc2_read_isgetaskpp()
    wbc2_read_rx_rcvd_buff = wbc2_read_rx_rcvd(data_size)
    if(wbc2_read_rx_rcvd_buff != rx_send_pp):
        print("[ERR] tx get ask data != rx ask send data")
        print("wbc2_read_rx_rcvd_buff: ", ' '.join( ['0x{:02X}'.format(x) for x in wbc2_read_rx_rcvd_buff]) )
        print("rx_send_pp: ", ' '.join( ['0x{:02X}'.format(x) for x in rx_send_pp]) )
    else:
        print("[PASS] tx get ask data = rx ask send data")

wbc2_init('COM6')
wlc98_init()
print("test case FSK_PP_HEAD_0x1E")
wlc98_wbc2_communitation(rx_send_pp = [ASK_PP_HEAD_0x18,FSK_PP_HEAD_0x1E],
                         tx_rsp_pp = [FSK_PP_HEAD_0x1E,0x11], data_size = 2)

print("test case FSK_PP_HEAD_0x1F")
wlc98_wbc2_communitation(rx_send_pp = [ASK_PP_HEAD_0x18,FSK_PP_HEAD_0x1F], 
                         tx_rsp_pp = [FSK_PP_HEAD_0x1F,0x22], data_size = 1+1)

print("test case FSK_PP_HEAD_0x2F")
wlc98_wbc2_communitation(rx_send_pp = [ASK_PP_HEAD_0x29,FSK_PP_HEAD_0x2F,0x01],
                          tx_rsp_pp = [FSK_PP_HEAD_0x2F,0x22,0x33], data_size = 1+2)


print("test case FSK_PP_HEAD_0x6F")
wlc98_wbc2_communitation(rx_send_pp = [ASK_PP_HEAD_0x68,FSK_PP_HEAD_0x6F,0x01,0x02,0x03,0x04,0x05],
                         tx_rsp_pp = [FSK_PP_HEAD_0x6F,0x22,0x33,0x44,0x55,0x66,0x77], data_size = 1+6)

print("test case FSK_PP_HEAD_0x7F")
wlc98_wbc2_communitation(rx_send_pp = [ASK_PP_HEAD_0x78,FSK_PP_HEAD_0x7F,0x01,0x02,0x03,0x04,0x05,0x06],
                         tx_rsp_pp = [FSK_PP_HEAD_0x7F,0x22,0x33,0x44,0x55,0x66,0x77,0x88], data_size = 1+7)


# test log
# uart write 0x70 0x05 to disable tx print uart log for better uart communication
# uart write 0x77 0x01 0x01 set enable response to rx data
# Composite FT260 device found on path \\?\hid#vid_0403&pid_6030&mi_00#a&19241153&0&0000#{4d1e55b2-f16f-11cf-88cb-001111000030}
# Open FT260 device OK
# Device ID 0x: 00343130323530511400000021003300
# ChipID:0x0062 rev:2 patchid:0x1454 cfgid:0x2C00 
# CHIPID_WLC98
# test case FSK_PP_HEAD_0x1E
# [TX] wbc2_set_fskdata: fsk_head=0x1E, Data= 0x11
# [RX] send ASK PP size 2 Data:  0x18 0x1E        
# [RX] tx_reply_data:  0x1E 0x11
# [PASS] rx get fsk data = tx fsk send data
# [TX] Get RX ASK PP packet
# [PASS] tx get ask data = rx ask send data
# test case FSK_PP_HEAD_0x1F
# [TX] wbc2_set_fskdata: fsk_head=0x1F, Data= 0x22
# [RX] send ASK PP size 2 Data:  0x18 0x1F
# [RX] tx_reply_data:  0x1F 0x22
# [PASS] rx get fsk data = tx fsk send data
# [TX] Get RX ASK PP packet
# [PASS] tx get ask data = rx ask send data
# test case FSK_PP_HEAD_0x2F
# [TX] wbc2_set_fskdata: fsk_head=0x2F, Data= 0x22 0x33
# [RX] send ASK PP size 3 Data:  0x29 0x2F 0x01
# [RX] tx_reply_data:  0x2F 0x22 0x33
# [PASS] rx get fsk data = tx fsk send data
# [TX] Get RX ASK PP packet
# [PASS] tx get ask data = rx ask send data
# test case FSK_PP_HEAD_0x6F
# [TX] wbc2_set_fskdata: fsk_head=0x6F, Data= 0x22 0x33 0x44 0x55 0x66 0x77
# [RX] send ASK PP size 7 Data:  0x68 0x6F 0x01 0x02 0x03 0x04 0x05
# [RX] tx_reply_data:  0x6F 0x22 0x33 0x44 0x55 0x66 0x77
# [PASS] rx get fsk data = tx fsk send data
# [TX] Get RX ASK PP packet
# [PASS] tx get ask data = rx ask send data
# test case FSK_PP_HEAD_0x7F
# [TX] wbc2_set_fskdata: fsk_head=0x7F, Data= 0x22 0x33 0x44 0x55 0x66 0x77 0x88
# [RX] send ASK PP size 8 Data:  0x78 0x7F 0x01 0x02 0x03 0x04 0x05 0x06
# [RX] tx_reply_data:  0x7F 0x22 0x33 0x44 0x55 0x66 0x77 0x88
# [PASS] rx get fsk data = tx fsk send data
# [TX] Get RX ASK PP packet
# [PASS] tx get ask data = rx ask send data