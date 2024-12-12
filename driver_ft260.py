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
from ft import *
import atexit
dev_addr = 0x61
CHIPID_WLC38 = 0X0026
CHIPID_WBC86 = 0X0056
CHIPID_WLC89 = 0x0159
CHIPID_WLC98 = 0x0062
CHIPID_WLC99 = 0x0063
class ft260_dongle():
    verbose = 0
    def __init__(self, i2c_speed = 100,dev_addr_set = 0x61):
        global dev_addr
        open_ftlib()
        self.i2c_handle = None
        if not find_device_in_paths(0x0403, 0x6030):
            print("1.0", """No FT260 Device found. Was looking USB devices by VID/PID combination and didn't find any. 
            Did you forget to connect FT260 chip to USB? Did you install the driver? Do you see FT260 in device list?""")
            exit()
        atexit.register(self.close)
        self.i2c_handle = openFtAsI2c(0x0403, 0x6030, i2c_speed)# 100 and 400 are mostly used in I2C devices
        dev_addr = dev_addr_set
        #time.sleep(0.1)
    def log1(self):
        self.verbose = 1
    def log0(self):
        self.verbose = 0
    def close(self):
        close_device(self.i2c_handle)
    def wread(self, RegisterAddr, ReadCount = 1):#16bit
        if self.i2c_handle is None:
            return None
        reg_addr_str = struct.pack("".join(['>', 'H']), RegisterAddr)
        #print(reg_addr_str)
        ftI2cWrite(self.i2c_handle,dev_addr,FT260_I2C_FLAG.FT260_I2C_START,reg_addr_str)
        (ft_status, data_real_read_len, read_buff, status) = ftI2cRead(self.i2c_handle,dev_addr,
                                                               FT260_I2C_FLAG.FT260_I2C_START_AND_STOP,ReadCount)
        if(self.verbose==1):
            print("[WR],@0x{0:04X} >>".format(RegisterAddr), ' '.join( ['0x{:02X}'.format(x) for x in read_buff]) )#hex(RegisterAddr)
        if(ReadCount == 1):
            return read_buff[0]
        elif(ReadCount == 2):
            return read_buff[0] + read_buff[1] * 256
        else:
            return read_buff
    def wreadbuff(self, RegisterAddr, ReadCount = 1):#16bit
        if self.i2c_handle is None:
            return None
        reg_addr_str = struct.pack("".join(['>', 'H']), RegisterAddr)
        #print(reg_addr_str)
        ftI2cWrite(self.i2c_handle,dev_addr,FT260_I2C_FLAG.FT260_I2C_START,reg_addr_str)
        (ft_status, data_real_read_len, read_buff, status) = ftI2cRead(self.i2c_handle,dev_addr,
                                                               FT260_I2C_FLAG.FT260_I2C_START_AND_STOP,ReadCount)
        if(self.verbose==1):
            print("[WR],@0x{0:04X} >>".format(RegisterAddr), ' '.join( ['0x{:02X}'.format(x) for x in read_buff]) )#hex(RegisterAddr)
        return list(read_buff)
    
    def write(self, RegisterAddr, WriteData):
        if self.i2c_handle is None:
            return None
        if(isinstance(WriteData,int)):
            reg_addr_str = struct.pack("".join(['>', 'H', 'B']), RegisterAddr,WriteData)
        else:
            data_list = [struct.pack("B", x) for x in WriteData]
            data = b"".join(data_list)
            reg_addr_str = struct.pack("".join(['>', 'H']), RegisterAddr) + data
            #print(reg_addr_str)
        (ftStatus) = ftI2cWrite(self.i2c_handle,dev_addr,FT260_I2C_FLAG.FT260_I2C_START_AND_STOP,reg_addr_str)
        if(self.verbose==1):
            if(isinstance(WriteData,int)):
                print("[W],@0x{0:04X} >> 0x{1:X}".format( RegisterAddr , WriteData))
            else:
                print("[W],@0x{0:04X} >>".format(RegisterAddr), ' '.join( ['0x{:02X}'.format(x) for x in WriteData]) )
    def write16(self, RegisterAddr, WriteData):
        self.write(RegisterAddr,WriteData)

    def wread16(self, RegisterAddr, ReadCount = 1):
        read_buff = self.wread(RegisterAddr,ReadCount)
        return read_buff
    
    def writeFA(self,add32,data):
        if(self.i2c_handle == None):
            return
        try:
            add32_bytes = add32.to_bytes(4, byteorder='big')
            if type(data) == list:
                wdata = [0xFA,add32_bytes[0],add32_bytes[1],add32_bytes[2],add32_bytes[3]] + data
                if(self.verbose):
                    print("W FA @0x{:08X} >>".format(add32), ' '.join( ['{:02X}'.format(x) for x in data]) )
            else:
                wdata = [0xFA,add32_bytes[0],add32_bytes[1],add32_bytes[2],add32_bytes[3], data]
                if(self.verbose):
                    print(f"W @0x{add32:08x} = 0x{data:02x}")
            data_list = [struct.pack("B", x) for x in wdata]
            data_str = b"".join(data_list)
            (ftStatus) = ftI2cWrite(self.i2c_handle,dev_addr,FT260_I2C_FLAG.FT260_I2C_START_AND_STOP,data_str)
        except OSError as err:
            print("OS error: {0}".format(err))

    def wreadFA(self,add32,size = 1):
        if(self.i2c_handle == None):
            return
        try:
            add32_bytes = add32.to_bytes(4, byteorder='big')
            wdata = [0xFA,add32_bytes[0],add32_bytes[1],add32_bytes[2],add32_bytes[3]]
            #result = bytearray(size)
            data_list = [struct.pack("B", x) for x in wdata]
            data_str = b"".join(data_list)
            ftI2cWrite(self.i2c_handle,dev_addr,FT260_I2C_FLAG.FT260_I2C_START,data_str)
            (ft_status, data_real_read_len, result, status) = ftI2cRead(self.i2c_handle,dev_addr,
                                                                FT260_I2C_FLAG.FT260_I2C_START_AND_STOP,size)
            if(size == 1):
                value = int(result.hex(),16)
                if(self.verbose):
                    print("R FA @0x{:08X} = 0x{:02X}".format(add32,value))
                return value
            elif(size == 2):
                result = list(result)
                #value = int(result[0].hex(),16) + int(result[1].hex(),16) * 256
                value = result[0] + result[1] * 256
                if(self.verbose):
                    print("R FA @0x{:08X} = 0x{:04X}".format(add32,value))
                return value
            else:
                if(self.verbose):#MSB LSB
                    print("R FA @0x{:08X} >>".format(add32), ' '.join( ['{:02X}'.format(x) for x in list(result)]) )
                return list(result)
        except OSError as err:
            print("OS error: {0}".format(err))

    def chip_info(self):#use for wlc38
        read_buff = self.wread16(0x0010,16)
        print("Device ID 0x:",''.join( ['{:02X}'.format(x) for x in read_buff]) )
        read_buff = self.wread(0x0000,16)
        chipid = read_buff[0] + read_buff[1] * 256
        chiprev = read_buff[2]
        patchid = read_buff[6] + read_buff[7] * 256
        cfgid = read_buff[10] + read_buff[11] * 256
        print("ChipID:0x{:04X} rev:{} patchid:0x{:04X} cfgid:0x{:04X}".format(chipid,chiprev,patchid,cfgid))
        if(chipid == 0x0000):
            print("[ERR] chipid 0 and use FA command to test again")
            #use fa to retry
            read_buff = self.wreadFA(0x2001C000,8)
            chipid = read_buff[0] + read_buff[1] * 256
            chiprev = read_buff[2]
            patchid = read_buff[5] + read_buff[4] * 256
            cfgid = read_buff[7] + read_buff[6] * 256
            print("ChipID:0x{:04X} rev:{} patchid:0x{:04X} cfgid:0x{:04X}".format(chipid,chiprev,patchid,cfgid))
            exit()
        elif(CHIPID_WLC38 == chipid):
            cut_version = chiprev - 1
            print(f"CHIPID_WLC38 Cut1.{cut_version}")
        elif(CHIPID_WBC86 == chipid):
            print("CHIPID_WBC86")
        elif(CHIPID_WLC98 == chipid):
            print("CHIPID_WLC98")
        elif(CHIPID_WLC99 == chipid):
            print("CHIPID_WLC99")
        return (patchid,cfgid,chipid)
    
    def wlc89_rom3_info(self):
        read_buff = self.wread16(0x0000,8)
        chipid = read_buff[0] + read_buff[1] * 256
        chiprev = read_buff[2]
        custid = read_buff[3]
        patchid = read_buff[4] + read_buff[5] * 256
        cfgid = read_buff[6] + read_buff[7] * 256
        print("ChipID:0x{:04X} rev:0x{:02X} patchid:0x{:04X} cfgid:0x{:04X}".format(chipid,chiprev,patchid,cfgid))
        if(chiprev == 0x20):
            print("CUT2.1")
        elif(chiprev == 0x30):
            print("CUT2.2")
        elif(chiprev == 0x40):
            print("CUT2.3")
        else:
            print("[ERR] Not ROM3")
        return (patchid,cfgid,chipid)
    
    def wlc38_vout_set(self,val = 5000):
        if(val > 12000):#not support
            return
        rx_vout_set_h = int((val - 500)/100)
        rx_vout_set_l = int(int((val - 500)%100)/25)
        print(f"rx_vout_set_l,{rx_vout_set_l},rx_vout_set_h,{rx_vout_set_h}")
        rx_vout_set_l = rx_vout_set_l << 6;
        self.write(0x00B1,rx_vout_set_l)#Cut 1.2 and newer. Program lower 2 bits of VOUT set, with 25mV resolution.
        # 0 - 0mV 1 - 25mV 2 - 50mV 3 - 75mV
        self.write(0x00B2,rx_vout_set_h)

    def wlc99_vout_set(self,val = 9000):#only support WLC99
        if(val > 20000):
            return
        rx_vout_set_register = int( val/25 )
        Data16 = rx_vout_set_register.to_bytes(2, byteorder='big')
        MSB = Data16[0]
        LSB = Data16[1]
        send_buff = [Data16[1], Data16[0]]
        self.write(0x00AA,send_buff)
        
    def wlc98_vout_set(self,val = 9000):#only support WLC98
        if(val > 20000):
            return
        rx_vout_set_register = int( val/25 )
        Data16 = rx_vout_set_register.to_bytes(2, byteorder='big')
        send_buff = [Data16[1], Data16[0]]
        self.write(0x00B4,send_buff)
