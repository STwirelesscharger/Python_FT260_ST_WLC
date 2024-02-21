from ft import *
import atexit
dev_addr = 0x61
CHIPID_WLC38 = 0X0026
CHIPID_WBC86 = 0X0056
class ft260_dongle():
    verbose = 1
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
            print("[WR],@0x{0} >>".format( hex(RegisterAddr) ), ' '.join( ['0x{:02X}'.format(x) for x in read_buff]) )
        if(ReadCount == 1):
            return read_buff[0]
        elif(ReadCount == 2):
            return read_buff[0] + read_buff[1] * 256
        else:
            return read_buff
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
                print("[W],@0x{0:X} >> 0x{1:X}".format( RegisterAddr , WriteData))
            else:
                print("[W],@0x{0} >>".format( hex(RegisterAddr) ), ' '.join( ['0x{:02X}'.format(x) for x in WriteData]) )
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

    def chip_info(self):
        read_buff = self.wread16(0x0010,16)
        print("Device ID 0x:",''.join( ['{:02X}'.format(x) for x in read_buff]) )
        read_buff = self.wread(0x0000,16)
        chipid = read_buff[0] + read_buff[1] * 256
        chiprev = read_buff[2]
        patchid = read_buff[6] + read_buff[7] * 256
        cfgid = read_buff[10] + read_buff[11] * 256
        print("ChipID:0x{:04X} rev:{} patchid:0x{:04X} cfgid:0x{:04X}".format(chipid,chiprev,patchid,cfgid))
        if(chipid == 0x0000):
            print("[ERR] chipid 0")
            exit()
        elif(CHIPID_WLC38 == chipid):
            print("CHIPID_WLC38")
        elif(CHIPID_WBC86 == chipid):
            print("CHIPID_WBC86")
        return (patchid,cfgid,chipid)
    def rx_data(self):#wlc38
        read_buff = self.wread(0x0092,10)
        vrect = read_buff[0] + read_buff[1] * 256
        vout  = read_buff[2] + read_buff[3] * 256
        iin   = read_buff[4] + read_buff[5] * 256
        die   = read_buff[6] + read_buff[7] * 256
        freq  = read_buff[8] + read_buff[9] * 256
        #print(f"rx,vrect,{vrect},vout,{vout},cur,{iin},die,{die},freq,{freq}")
        rx_pwr = vout * iin/1000/1000
        rx_ctrl_err = self.wread(0x00A4,2)
        if(0 == vrect):
            rx_ctrl_err = 0
        else:
            if(rx_ctrl_err > 0x7FF):
                rx_ctrl_err = rx_ctrl_err - 0XFFFF
            rx_ctrl_err /= 256
        str_data = f"{vrect},{vout},{iin},{die},{freq},{rx_ctrl_err:.1f},{rx_pwr:.2f}"
        return (str_data,rx_pwr)

    def wlc38_vout_set(self,val = 5000):
        if(val > 12000):#not support
            return
        rx_vout_set_h = int((val - 500)/100)
        rx_vout_set_l = int(int((val - 500)%100)/25)
        print(f"rx_vout_set_l,{rx_vout_set_l},rx_vout_set_h,{rx_vout_set_h}")
        rx_vout_set_l = rx_vout_set_l << 5;
        self.write(0x00B1,rx_vout_set_l)#Cut 1.2 and newer. Program lower 2 bits of VOUT set, with 25mV resolution.
        # 0 - 0mV
        # 1 - 25mV
        # 2 - 50mV
        # 3 - 75mV
        self.write(0x00B2,rx_vout_set_h)
