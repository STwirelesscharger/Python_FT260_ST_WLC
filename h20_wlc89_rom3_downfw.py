import driver_ft260
import time
import os
from enum import Enum
#SYSREG registers
HWREG_HW_CHIP_ID_ADDR            = 0x2001C000
HWREG_HW_VER_ADDR                = 0x2001C002
HWREG_RST_ADDR                   = 0x2001C138

# FW registers
FWREG_OP_MODE_ADDR				= 0x0102
FWREG_SYS_CMD_ADDR = 0x0108
CMD_FTP_WR = 0X04
CMD_FTP_RD = 0X08
CMD_FTP_FULL_ERASE = 0X20

FWREG_NVM_WR_PWD_ADDR = 0x010A
FWREG_NVM_SECTOR_INDEX_ADDR = 0x010C
FWREG_AUX_DATA_00 = 0x0180

NVM_SECTOR_SIZE_BYTES = 128
NVM_PATCH_START_SECTOR_INDEX = 0
NVM_CFG_START_SECTOR_INDEX = 124 #
#CHANGE with memh file name
NVM_CFG_VERSION_ID = 0x2304
NVM_PATCH_VERSION_ID = 0xC767
#define NVM_CFG_SIZE 512
#define NVM_CFG_VERSION_ID 0x2304
#define NVM_PATCH_SIZE 2880
#define NVM_PATCH_VERSION_ID 0xC767

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

def FtpPoll(address, cmd):
    """
    Polls the FTP command register until the command is cleared.
    """
    for _ in range(10):
        time.sleep(0.1)
        wr_cmd = i2c.wread16(address)
        if wr_cmd & cmd == 0:
            print(f"[PASS] FtpPoll 0x{address:X} = 0x{cmd:X}")
            break
    else:
        print(f"[FAIL] FtpPoll 0x{address:X} = 0x{cmd:X}")

def FtpReadMemhFile(in_filename):
    """
    Reads a .memh file and converts its contents to a byte array.
    """
    with open(in_filename, 'r', encoding='utf-8') as memh_file:
        memh_lines = memh_file.read().splitlines()
    result = []
    for memh_line in memh_lines:
        memh_data = int(memh_line, 16)
        temp = memh_data.to_bytes(4, byteorder='little')
        result.extend(temp)
    return result

def FtpMemhCheckSize(ftpData, isPatch=True):
    """
    Checks the size of the FTP data to ensure it is within valid limits.
    """
    ftpData_len = len(ftpData)
    if isPatch:
        if ftpData_len <= 128 * 4:
            print(f"[ERR] ftpData_len {ftpData_len} is smaller than 128*4")
            return ERROR.PATCH_FILE_SIZE
        elif ftpData_len >= 128 * 62:
            print(f"[ERR] ftpData_len {ftpData_len} is larger than 128*62")
            return ERROR.PATCH_FILE_SIZE
    else:
        if ftpData_len != 128 * 4:
            print(f"[ERR] ftpData_len {ftpData_len} is not equal to 128*4")
            return ERROR.CFG_FILE_SIZE
    return ERROR.OK

def NvmSectorWriting(nvmsectorData, sectIndex):
    """
    Writes a sector of NVM data.
    """
    print(f"[STEP] NvmSectorWriting {sectIndex} ...")
    i2c.write16(FWREG_NVM_SECTOR_INDEX_ADDR, sectIndex)
    print("Fill data")
    i2c.write16(FWREG_AUX_DATA_00, nvmsectorData)
    print("Set sys command write flash")
    i2c.write16(FWREG_SYS_CMD_ADDR, 0x04)
    print("Check comand is done or not")
    FtpPoll(FWREG_SYS_CMD_ADDR, 0x04)

def NvmPatchWriting(nvmPatchData):
    """
    Writes patch data to NVM sectors.
    """
    patch_data_len = len(nvmPatchData)
    div = patch_data_len // NVM_SECTOR_SIZE_BYTES
    remainder = patch_data_len % NVM_SECTOR_SIZE_BYTES
    print(f"NvmPatchWriting (div:{div} remainder:{remainder})")
    i = NVM_PATCH_START_SECTOR_INDEX
    for sector_index in range(NVM_PATCH_START_SECTOR_INDEX, div):
        NvmSectorWriting(nvmPatchData[i:i + NVM_SECTOR_SIZE_BYTES], sector_index)
        i += NVM_SECTOR_SIZE_BYTES
    if remainder != 0:
        sector_index += 1
        NvmSectorWriting(nvmPatchData[i:], sector_index)

def FtpPatchCfgWriting(ftpPatchData, ftpCfgData):
    """
    Writes patch and configuration data to the device.
    """
    isok = FtpMemhCheckSize(ftpPatchData, True)
    if isok != ERROR.OK:
        return isok
    isok = FtpMemhCheckSize(ftpCfgData, False)
    if isok != ERROR.OK:
        return isok

    opmode = i2c.wread16(FWREG_OP_MODE_ADDR)
    if(1 != opmode):
        print("[ERR] opmode != 1")
        return ERROR.OPMODE
    print("[PASS] CHECK OP MODE = 1")
    print("[STEP] SET FTP PASSWORD")
    i2c.write16(FWREG_NVM_WR_PWD_ADDR, 0xC5)
    print("[STEP] FW FULL ERASE")
    i2c.write16(FWREG_SYS_CMD_ADDR, CMD_FTP_FULL_ERASE)
    FtpPoll(FWREG_SYS_CMD_ADDR, CMD_FTP_FULL_ERASE)

    print("[STEP] FLASH SECTOR USE 128 BYTES")
    NvmPatchWriting(ftpPatchData)

    NvmSectorWriting(ftpCfgData[0:128], NVM_CFG_START_SECTOR_INDEX)
    NvmSectorWriting(ftpCfgData[128:256], NVM_CFG_START_SECTOR_INDEX + 1)
    NvmSectorWriting(ftpCfgData[256:384], NVM_CFG_START_SECTOR_INDEX + 2)
    NvmSectorWriting(ftpCfgData[384:], NVM_CFG_START_SECTOR_INDEX + 3)

    print("[STEP] SYSTEM HW RESET")
    i2c.writeFA(HWREG_RST_ADDR, 0x01)#can be skip?
    time.sleep(1)
    print("[DONE] FtpPatchCfgWriting")
    return ERROR.OK

def WLC89_update_patch_cfg(patch_file_name, cfg_file_name):
    """
    Updates the patch and configuration of the WLC89 device.
    """
    print("patch_file_name:" + patch_file_name)
    print("cfg_file_name:" + cfg_file_name)
    ftpPatchData = FtpReadMemhFile(patch_file_name)
    ftpCfgData = FtpReadMemhFile(cfg_file_name)

    isok = FtpPatchCfgWriting(ftpPatchData, ftpCfgData)
    if isok != ERROR.OK:
        return isok
    print("[STEP] read patch/cfg id to check")
    (patchid,cfgid,chipid) = i2c.wlc89_rom3_info()
    if patchid != NVM_PATCH_VERSION_ID:
        print(f"Patch Error: 0x{patchid:X} != 0x{NVM_PATCH_VERSION_ID:X}")
        return ERROR.PATCH_ID
    elif cfgid != NVM_CFG_VERSION_ID:
        print(f"CFG Error: 0x{cfgid:X} != 0x{NVM_CFG_VERSION_ID:X}")
        return ERROR.CFG_ID
    else:
        print("[PASS] WLC89_update_patch_cfg")
        return ERROR.OK

def WLC89_main(patch_file_name, cfg_file_name):
    """
    Main function to update the WLC89 device with the given patch and configuration files.
    """
    global i2c
    try:
        CHIPID_WLC89 = 0x0159
        i2c = driver_ft260.ft260_dongle()
        i2c.log1()
        if i2c is None:
            return ERROR.DONGLE
        (patchid,cfgid,chipid) = i2c.wlc89_rom3_info()
        if CHIPID_WLC89 != chipid:
            print("ERR CHIP NOT WLC89")
            return ERROR.CHIPID
        print("[PASS] CHIP WLC89")
        if not os.path.exists(patch_file_name):
            return ERROR.FILE_NOT_FIND
        if not os.path.exists(cfg_file_name):
            return ERROR.FILE_NOT_FIND
        isok = WLC89_update_patch_cfg(patch_file_name, cfg_file_name)
        input("press any key to exit")
        return isok
    except Exception as e:
        print("An exception occurred. | ", e)
        return ERROR.EXCEPTION

if __name__ == "__main__":
    #folder_name = "C:\Users\zhouwill\Downloads\52Project\12.WLC89_JIgger\_Send2Cutsomer\FW_0927\"
    patch_file_name = "peony_nvmpatch_rom3_rtx_uart_C767.memh"
    cfg_file_name = "cfg2304_wlc89_rom3_BPP5V_EPP9V_MPP12V_gpio3_voutgd_uart_delay15ms.memh"
    WLC89_main(patch_file_name, cfg_file_name)

"""
Open FT260 device OK
ChipID:0x0159 rev:0x40 patchid:0xC767 cfgid:0x2304
CUT2.3
patch_file_name:peony_nvmpatch_rom3_rtx_uart_C767.memh
cfg_file_name:cfg2304_wlc89_rom3_BPP5V_EPP9V_MPP12V_gpio3_voutgd_uart_delay15ms.memh
check op mode
set ftp password
fw Full erase
[PASS] FtpPoll 0x108 = 0x20
flash sector use 128 bytes
NvmPatchWriting (div:22 remainder:64)
NvmSectorWriting 0 ...
[PASS] FtpPoll 0x108 = 0x4
NvmSectorWriting 1 ...
[PASS] FtpPoll 0x108 = 0x4
NvmSectorWriting 2 ...
[PASS] FtpPoll 0x108 = 0x4
NvmSectorWriting 3 ...
[PASS] FtpPoll 0x108 = 0x4
NvmSectorWriting 4 ...
[PASS] FtpPoll 0x108 = 0x4
NvmSectorWriting 5 ...
[PASS] FtpPoll 0x108 = 0x4
NvmSectorWriting 6 ...
[PASS] FtpPoll 0x108 = 0x4
NvmSectorWriting 7 ...
[PASS] FtpPoll 0x108 = 0x4
NvmSectorWriting 8 ...
[PASS] FtpPoll 0x108 = 0x4
NvmSectorWriting 9 ...
[PASS] FtpPoll 0x108 = 0x4
NvmSectorWriting 10 ...
[PASS] FtpPoll 0x108 = 0x4
NvmSectorWriting 11 ...
[PASS] FtpPoll 0x108 = 0x4
NvmSectorWriting 12 ...
[PASS] FtpPoll 0x108 = 0x4
NvmSectorWriting 13 ...
[PASS] FtpPoll 0x108 = 0x4
NvmSectorWriting 14 ...
[PASS] FtpPoll 0x108 = 0x4
NvmSectorWriting 15 ...
[PASS] FtpPoll 0x108 = 0x4
NvmSectorWriting 16 ...
[PASS] FtpPoll 0x108 = 0x4
NvmSectorWriting 17 ...
[PASS] FtpPoll 0x108 = 0x4
NvmSectorWriting 18 ...
[PASS] FtpPoll 0x108 = 0x4
NvmSectorWriting 19 ...
[PASS] FtpPoll 0x108 = 0x4
NvmSectorWriting 20 ...
[PASS] FtpPoll 0x108 = 0x4
NvmSectorWriting 21 ...
[PASS] FtpPoll 0x108 = 0x4
NvmSectorWriting 22 ...
[PASS] FtpPoll 0x108 = 0x4
NvmSectorWriting 124 ...
[PASS] FtpPoll 0x108 = 0x4
NvmSectorWriting 125 ...
[PASS] FtpPoll 0x108 = 0x4
NvmSectorWriting 126 ...
[PASS] FtpPoll 0x108 = 0x4
NvmSectorWriting 127 ...
[PASS] FtpPoll 0x108 = 0x4
system hw reset
[DONE] FtpPatchCfgWriting
ChipID:0x0159 rev:0x40 patchid:0xC767 cfgid:0x2304
CUT2.3
[PASS] WLC89_update_patch_cfg
"""