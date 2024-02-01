import driver_ft260
from wlc38_register import *
import time
#QI 1.3 define
QI13_Head_Digest_Response      = 0x11
QI13_Head_Certificate_Response = 0x12
QI13_Head_Challenge_Response   = 0x13
#QI 1.3 define
QI13_Head_Digest_Request      = 0x19
QI13_Head_Certificate_Request = 0x1A
QI13_Head_Challenge_Request   = 0x1B


wlc38 = driver_ft260.ft260_dongle()
wlc38.chip_info()
#rx put some type tx and this tx can qi 1.3 dts packet
def wlc38_dts_send(SendMsg):
    wlc38.write16(I2CREG_RX_DTS_SEND,len(SendMsg))#set dts length
    wlc38.write16(I2CREG_RX_DTS_SEND+2,0x02)#request see qi spec
    wlc38.write16(DTS_SEND_MSG_000,SendMsg)
    wlc38.write16(I2CREG_RX_CMD,(1<<BIT_RX_SEND_DTS))
    time.sleep(2)
    print("read int and read buff")
    wlc38.wread16(I2CREG_RX_INTR_LATCH,4)#read int status
    dts_rcv_cnt = wlc38.wread16(I2CREG_RX_DTS_RCVD,2)
    print(f"dts_rcv_cnt,{dts_rcv_cnt}")
    if(dts_rcv_cnt > 1):
        wlc38.wread16(DTS_RCVD_MSG_000,dts_rcv_cnt)

print("RX Send QIV13_GetDigest")
wlc38_dts_send([QI13_Head_Digest_Request,0x0F])
