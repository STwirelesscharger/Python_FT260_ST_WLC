import driver_ft260
import time
import os
from enum import Enum

HWREG_HW_CHIP_ID_ADDR            = 0x2001C000
HWREG_HW_VER_ADDR                = 0x2001C002
HWREG_RST_ADDR                   = 0x2001F200
HWREG_STICKY_ADDR                = 0x2001FC18
HWREG_SYSREG_RESET_ADDR 		 = 0x2001F200

HWREG_NVM_CTRL_ADDR             = 0x2001F300
HWREG_NVM_WR_BUFF_ADDR          = 0x00090000
HWREG_NVM_MAIN_MEM_START_ADDR   = 0x00080000
HWREG_NVM_INFO_MEM_START_ADDR   = 0x000A0000
HWREG_NVM_INFO_LOCK_NUM_ADDR    = 0x2001F306
HWREG_NVM_STAT_ADDR           	= 0x2001F314
HWREG_NVM_SECTOR_0_CMD_ADDR     = 0x00080000

FWREG_CHIP_REV_ADDR                    = 0x0002
FWREG_ROM_ID_ADDR                      = 0x0004
FWREG_OTP_PATCH_ID_ADDR                = 0x0006
FWREG_CFG_ID_ADDR                      = 0x000A
FWREG_PE_ID_ADDR                       = 0x000C
FWREG_OP_MODE_ADDR                     = 0x000E
FWREG_RX_INTR_EN                       = 0x0080
FWREG_RX_INTR_CLR                      = 0x0084
FWREG_RX_INTR_LATCH                    = 0x0088
FWREG_SYS_CMD_ADDR                     = 0x0020
CMD_SWITCH_2_RX = 0X02
CMD_FTP_WR = 0X04
CMD_FTP_RD = 0X08
CMD_FTP_RRAM_PU = 0X10 #RRAM power up
CMD_FTP_RRAM_PD = 0X20 #RRAM power down
CMD_FTP_RST_NVM_DIS = 0x40 #disable nvm after reset

FWREG_NVM_WR_PWD_ADDR                  = 0x0022
FWREG_NVM_SECTOR_INDEX_ADDR            = 0x0024
FWREG_NVM_ERR_ADDR                     = 0x002D
FWREG_AUX_DATA_00   		           = 0x0180
NVM_SECTOR_SIZE_BYTES                  = 256

class ERROR(Enum):
    OK = 0
    DONGLE = 1
    CHIPID = 2
    FILE_NOT_FIND = 3
    PATCH_FILE_SIZE = 4
    CFG_FILE_SIZE = 5
    PATCH_ID = 6
    CFG_ID = 7
    EXCEPTION = 8
    OPMODE = 9

i2c = None
CHIPID_WLC38 = 0X0026

def FtpPoll(address, cmd):
    """
    Polls the FTP command register until the command is cleared.
    """
    for _ in range(100):
        time.sleep(0.01)
        wr_cmd = i2c.wread16(address)
        if wr_cmd & cmd == 0:
            #print(f"[PASS] FtpPoll 0x{address:X} = 0x{cmd:X}")
            break
    else:
        print(f"[FAIL] FtpPoll 0x{address:X} = 0x{cmd:X}")

def FtpReadMemhFile(in_filename):
    memh_file = open(in_filename, 'r', encoding='utf-8')
    memh_lines = memh_file.read().splitlines()
    result = []
    memh_datas = [int(memh_line, 16) for memh_line in memh_lines]
    for memh_data in memh_datas:
        temp = memh_data.to_bytes(4, byteorder= 'little')
        result.extend(temp)
    return result

def GetPatchId(patch_file_name):
    index = patch_file_name.find(".memh")
    sub_str = patch_file_name[index-4:index]
    return int(sub_str,16)

def GetCfgId(cfg_file_name):
    index = cfg_file_name.find("cfg")
    sub_str = cfg_file_name[index+3:index+7]
    return int(sub_str,16)

def FtpMemhCheckSize(ftpData,isPatch = True):
    ftpData_len = len(ftpData)
    if(isPatch):
        if(ftpData_len <= 128*3):
            print(f"[ERR] ftpData_len {ftpData_len} is small than 128*3")
            return ERROR.PATCH_FILE_SIZE
        elif(ftpData_len >= 256*125):
            print(f"[ERR] ftpData_len {ftpData_len} is larger than 256*125")
            return ERROR.PATCH_FILE_SIZE
    else:
        if(ftpData_len > 128*3):
            print(f"[ERR] ftpData_len {ftpData_len} is large than 128*3")
            return ERROR.CFG_FILE_SIZE
    return ERROR.OK

def NvmSectorWriting(nvmsectorData,sectIndex):
    print(f"NvmSectorWriting {sectIndex}")
    i2c.write16(FWREG_NVM_SECTOR_INDEX_ADDR,sectIndex)#0024
    i2c.write16(FWREG_SYS_CMD_ADDR,CMD_FTP_RRAM_PU)#RRAM Power up
    i2c.write16(FWREG_AUX_DATA_00,nvmsectorData)
    i2c.write16(FWREG_SYS_CMD_ADDR,CMD_FTP_WR)
    FtpPoll(FWREG_SYS_CMD_ADDR,CMD_FTP_WR)
    i2c.write16(FWREG_SYS_CMD_ADDR,CMD_FTP_RRAM_PD)#0020 RRAM Power down
#/// @brief      Write patch data to NVM sector 0-125
#/// @param      nvmPatchData: byte array of patch data
def NvmPatchWriting(nvmPatchData):
    patch_data_len = len(nvmPatchData)
    div = int(patch_data_len/NVM_SECTOR_SIZE_BYTES);
    remainder = patch_data_len % NVM_SECTOR_SIZE_BYTES;
    print("NvmPatchWriting (div:{} remainder:{})".format(div, remainder))
    i = 0
    for sector_index in range(0,div):
        NvmSectorWriting(nvmPatchData[i:i+NVM_SECTOR_SIZE_BYTES],sector_index)
        i += NVM_SECTOR_SIZE_BYTES
    #last sector
    if(remainder != 0):
        sector_index += 1
        NvmSectorWriting(nvmPatchData[i:],sector_index)

#only write cfg
def FtpCfgWritingOnly(nvmCfgData):
    FtpMemhCheckSize(nvmCfgData,False)
    #check sa mode
    i2c.write16(FWREG_SYS_CMD_ADDR,CMD_FTP_RST_NVM_DIS)
    time.sleep(0.1)
    i2c.write16(FWREG_NVM_WR_PWD_ADDR,0xC5)#Fill Nvm Password
    NvmSectorWriting(nvmCfgData[0:256],126)
    NvmSectorWriting(nvmCfgData[256:],127)
    i2c.write16(FWREG_SYS_CMD_ADDR,0x02)
    time.sleep(0.1)
    print("[DONE] FtpCfgWritingOnly")

def FtpPatchCfgWriting(ftpPatchData,ftpCfgData):
    isok = FtpMemhCheckSize(ftpPatchData,True)
    if(isok != ERROR.OK):
        return isok
    isok = FtpMemhCheckSize(ftpCfgData,False)
    if(isok != ERROR.OK):
        return isok
    print("check op mode")
    opmode = i2c.wread16(FWREG_OP_MODE_ADDR)
    if(1 != opmode):
        print("[ERR] opmode != 1")
        return ERROR.OPMODE
    
    print("FW system reset")
    i2c.write16(FWREG_SYS_CMD_ADDR,CMD_FTP_RST_NVM_DIS)
    time.sleep(0.05)
    print("set password")
    i2c.write16(FWREG_NVM_WR_PWD_ADDR,0xC5)
    print("flash sector use 256bytes")
    NvmPatchWriting(ftpPatchData)
    NvmSectorWriting(ftpCfgData[0:256],126)
    NvmSectorWriting(ftpCfgData[256:],127)
    #i2c.write16(FWREG_SYS_CMD_ADDR,CMD_SWITCH_2_RX)#SKIP?
    print("SYSTEM reset")
    i2c.writeFA(HWREG_RST_ADDR,0x01)
    time.sleep(0.05)
    print("[DONE] FtpPatchCfgWriting")
    return ERROR.OK

def wlc38_update_patch_cfg(patch_file_name,cfg_file_name):
    print(patch_file_name)
    print(cfg_file_name)
    ftpPatchData = FtpReadMemhFile(patch_file_name)
    ftpCfgData = FtpReadMemhFile(cfg_file_name)

    patchID = GetPatchId(patch_file_name)
    cfgID = GetCfgId(cfg_file_name)

    isok = FtpPatchCfgWriting(ftpPatchData,ftpCfgData)
    if(isok != ERROR.OK):
        return isok
    (patchid,cfgid,chipid) = i2c.chip_info()
    if(patchid != patchID):
        print("Patch Error: 0x{:X} != 0x{:X}".format(patchid, patchID))
        return ERROR.PATCH_ID
    elif(cfgid != cfgID):
        print("CFG Error: 0x{:X} != 0x{:X}".format(cfgid, cfgID))
        return ERROR.CFG_ID
    else:
        print("[PASS] wlc38_update_patch_cfg")
        return ERROR.OK

def wlc38_main(patch_file_name,cfg_file_name):
    global i2c
    try:
        print("default I2C dongle speed is 100Kbps")
        i2c = driver_ft260.ft260_dongle(100)#default is 100khz
        if(i2c == None):
            return ERROR.DONGLE
        (patchid,cfgid,chipid) = i2c.chip_info()
        if(CHIPID_WLC38 != chipid):
            print(f"ERR CHIP 0x{chipid:X} NOT WLC38 0x0026")
            return ERROR.CHIPID
        if os.path.exists(patch_file_name) == False:
            return ERROR.FILE_NOT_FIND
        if os.path.exists(cfg_file_name) == False:
            return ERROR.FILE_NOT_FIND
        start_time = time.time()
        err = wlc38_update_patch_cfg(patch_file_name,cfg_file_name)
        end_time = time.time()
        print("cost: {:.2f}sec".format(end_time - start_time))
        return err
    except Exception as e:
        print("An exception occurred. | ", e)
        return ERROR.EXCEPTION

if __name__ == "__main__":
    input("change your patch and cfg file name")
    print("patch file name must xxx_1234.memh script use 1234 for patch version")
    print("cfg file name must cfg1234_xxx.memh script use 1234 for cfg version")
    #wlc38_main("STEVAL-xx.memh", "STEVAL-WLC38_config_XX.memh")
    wlc38_main("polaris_nvmpatch_rom1_rtx_1634.memh", "cfg1063_test.memh")
    
