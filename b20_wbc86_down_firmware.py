import driver_ft260
import time
import os
from enum import Enum
#SYSREG registers
HWREG_HW_CHIP_ID_ADDR            = 0x2001C000
HWREG_HW_VER_ADDR                = 0x2001C002
HWREG_RST_ADDR                   = 0x2001C00C

# FW registers
FWREG_OP_MODE_ADDR = 0x000E
FWREG_SYS_CMD_ADDR = 0x0020
CMD_FTP_WR = 0X04
CMD_FTP_RD = 0X08
CMD_FTP_FULL_ERASE = 0X20
CMD_FTP_DISABLE = 0x40  #Write 1 to perform device reset and stop any FTP loading or execution. This prepares the FTP for writing. This register is self-cleared when the operation is completed.
FWREG_NVM_WR_PWD_ADDR = 0x0022
FWREG_NVM_SECTOR_INDEX_ADDR = 0x0024
FWREG_TX_CMD_ADDR = 0x00D0
FWREG_AUX_DATA_00 = 0x0100

NVM_SECTOR_SIZE_BYTES = 128
NVM_PATCH_START_SECTOR_INDEX = 0
NVM_CFG_START_SECTOR_INDEX = 62
NVM_CFG_VERSION_ID = 0x121E
NVM_PATCH_VERSION_ID = 0x1260

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
CHIPID_WBC86 = 0x0056

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
        if ftpData_len <= 128 * 2:
            print(f"[ERR] ftpData_len {ftpData_len} is smaller than 128*2")
            return ERROR.PATCH_FILE_SIZE
        elif ftpData_len >= 128 * 62:
            print(f"[ERR] ftpData_len {ftpData_len} is larger than 128*62")
            return ERROR.PATCH_FILE_SIZE
    else:
        if ftpData_len > 128 * 2:
            print(f"[ERR] ftpData_len {ftpData_len} is larger than 128*2")
            return ERROR.CFG_FILE_SIZE
    return ERROR.OK

def NvmSectorWriting(nvmsectorData, sectIndex):
    """
    Writes a sector of NVM data.
    """
    print(f"NvmSectorWriting {sectIndex} ...")
    i2c.write16(FWREG_NVM_SECTOR_INDEX_ADDR, sectIndex)
    i2c.write16(FWREG_AUX_DATA_00, nvmsectorData)
    i2c.write16(FWREG_SYS_CMD_ADDR, CMD_FTP_WR)
    FtpPoll(FWREG_SYS_CMD_ADDR, CMD_FTP_WR)

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
    print("check op mode")
    opmode = i2c.wread16(FWREG_OP_MODE_ADDR)
    if(1 != opmode) | (3 != opmode):
        print("[ERR] opmode != 1 or !=3")
        return ERROR.OPMODE
    
    print("ftp disable")
    i2c.write16(FWREG_SYS_CMD_ADDR, CMD_FTP_DISABLE)
    time.sleep(0.1)
    print("Stop TX power")
    i2c.write16(FWREG_TX_CMD_ADDR, 0x02)
    print("Disable ILOAD Skip?")
    print("set password")
    i2c.write16(FWREG_NVM_WR_PWD_ADDR, 0xC5)
    print("fw erase")
    i2c.write16(FWREG_SYS_CMD_ADDR, CMD_FTP_FULL_ERASE)
    FtpPoll(FWREG_SYS_CMD_ADDR, CMD_FTP_FULL_ERASE)
    print("flash sector use 128 bytes")
    NvmPatchWriting(ftpPatchData)
    NvmSectorWriting(ftpCfgData[0:128], NVM_CFG_START_SECTOR_INDEX)
    NvmSectorWriting(ftpCfgData[128:], NVM_CFG_START_SECTOR_INDEX + 1)

    print("system hw reset")
    i2c.writeFA(HWREG_RST_ADDR, 0x01)
    time.sleep(0.1)
    print("[DONE] FtpPatchCfgWriting")
    return ERROR.OK

def WBC86_update_patch_cfg(patch_file_name, cfg_file_name):
    """
    Updates the patch and configuration of the WBC86 device.
    """
    print("patch_file_name:" + patch_file_name)
    print("cfg_file_name:" + cfg_file_name)
    ftpPatchData = FtpReadMemhFile(patch_file_name)
    ftpCfgData = FtpReadMemhFile(cfg_file_name)

    isok = FtpPatchCfgWriting(ftpPatchData, ftpCfgData)
    if isok != ERROR.OK:
        return isok

    (patchid,cfgid,chipid) = i2c.chip_info()
    if patchid != NVM_PATCH_VERSION_ID:
        print(f"Patch Error: 0x{patchid:X} != 0x{NVM_PATCH_VERSION_ID:X}")
        return ERROR.PATCH_ID
    elif cfgid != NVM_CFG_VERSION_ID:
        print(f"CFG Error: 0x{cfgid:X} != 0x{NVM_CFG_VERSION_ID:X}")
        return ERROR.CFG_ID
    else:
        print("[PASS] WBC86_update_patch_cfg")
        return ERROR.OK

def WBC86_main(patch_file_name, cfg_file_name):
    """
    Main function to update the WBC86 device with the given patch and configuration files.
    """
    global i2c
    try:
        i2c = driver_ft260.ft260_dongle()
        if i2c is None:
            return ERROR.DONGLE
        (patchid,cfgid,chipid) = i2c.chip_info()
        if CHIPID_WBC86 != chipid:
            print("ERR CHIP NOT WBC86")
            return ERROR.CHIPID
        if not os.path.exists(patch_file_name):
            return ERROR.FILE_NOT_FIND
        if not os.path.exists(cfg_file_name):
            return ERROR.FILE_NOT_FIND
        start_time = time.time()
        err = WBC86_update_patch_cfg(patch_file_name,cfg_file_name)
        end_time = time.time()
        print("cost: {:.2f}sec".format(end_time - start_time))
        return err
    except Exception as e:
        print("An exception occurred. | ", e)
        return ERROR.EXCEPTION

if __name__ == "__main__":
    input("change your patch and cfg file")
    print("patch file name must xxx_1234.memh script use 1234 for patch version")
    print("cfg file name must cfg1234_xxx.memh script use 1234 for cfg version")
    WBC86_main("STEVAL-WBC86TX_nvmpatch_1260.memh", "STEVAL-WBC86TX_config_121E_BPP.memh")

"""
Test logs
Open FT260 device OK
Device ID 0x: 0050315634313243190000000F002B00
ChipID:0x0056 rev:2 patchid:0x1242 cfgid:0x120D
CHIPID_WBC86
patch_file_name:STEVAL-WBC86TX_nvmpatch_1260.memh
cfg_file_name:STEVAL-WBC86TX_config_121E_BPP.memh
FW system reset
Stop TX power
Disable ILOAD Skip?
set password
fw erase
[PASS] FtpPoll 0x20 = 0x20
NvmPatchWriting (div:53 remainder:60)
NvmSectorWriting 0 ...
[PASS] FtpPoll 0x20 = 0x4
NvmSectorWriting 1 ...
[PASS] FtpPoll 0x20 = 0x4
NvmSectorWriting 2 ...
[PASS] FtpPoll 0x20 = 0x4
NvmSectorWriting 3 ...
[PASS] FtpPoll 0x20 = 0x4
NvmSectorWriting 4 ...
[PASS] FtpPoll 0x20 = 0x4
NvmSectorWriting 5 ...
[PASS] FtpPoll 0x20 = 0x4
NvmSectorWriting 6 ...
[PASS] FtpPoll 0x20 = 0x4
NvmSectorWriting 7 ...
[PASS] FtpPoll 0x20 = 0x4
NvmSectorWriting 8 ...
[PASS] FtpPoll 0x20 = 0x4
NvmSectorWriting 9 ...
[PASS] FtpPoll 0x20 = 0x4
NvmSectorWriting 10 ...
[PASS] FtpPoll 0x20 = 0x4
NvmSectorWriting 11 ...
[PASS] FtpPoll 0x20 = 0x4
NvmSectorWriting 12 ...
[PASS] FtpPoll 0x20 = 0x4
NvmSectorWriting 13 ...
[PASS] FtpPoll 0x20 = 0x4
NvmSectorWriting 14 ...
[PASS] FtpPoll 0x20 = 0x4
NvmSectorWriting 15 ...
[PASS] FtpPoll 0x20 = 0x4
NvmSectorWriting 16 ...
[PASS] FtpPoll 0x20 = 0x4
NvmSectorWriting 17 ...
[PASS] FtpPoll 0x20 = 0x4
NvmSectorWriting 18 ...
[PASS] FtpPoll 0x20 = 0x4
NvmSectorWriting 19 ...
[PASS] FtpPoll 0x20 = 0x4
NvmSectorWriting 20 ...
[PASS] FtpPoll 0x20 = 0x4
NvmSectorWriting 21 ...
[PASS] FtpPoll 0x20 = 0x4
NvmSectorWriting 22 ...
[PASS] FtpPoll 0x20 = 0x4
NvmSectorWriting 23 ...
[PASS] FtpPoll 0x20 = 0x4
NvmSectorWriting 24 ...
[PASS] FtpPoll 0x20 = 0x4
NvmSectorWriting 25 ...
[PASS] FtpPoll 0x20 = 0x4
NvmSectorWriting 26 ...
[PASS] FtpPoll 0x20 = 0x4
NvmSectorWriting 27 ...
[PASS] FtpPoll 0x20 = 0x4
NvmSectorWriting 28 ...
[PASS] FtpPoll 0x20 = 0x4
NvmSectorWriting 29 ...
[PASS] FtpPoll 0x20 = 0x4
NvmSectorWriting 30 ...
[PASS] FtpPoll 0x20 = 0x4
NvmSectorWriting 31 ...
[PASS] FtpPoll 0x20 = 0x4
NvmSectorWriting 32 ...
[PASS] FtpPoll 0x20 = 0x4
NvmSectorWriting 33 ...
[PASS] FtpPoll 0x20 = 0x4
NvmSectorWriting 34 ...
[PASS] FtpPoll 0x20 = 0x4
NvmSectorWriting 35 ...
[PASS] FtpPoll 0x20 = 0x4
NvmSectorWriting 36 ...
[PASS] FtpPoll 0x20 = 0x4
NvmSectorWriting 37 ...
[PASS] FtpPoll 0x20 = 0x4
NvmSectorWriting 38 ...
[PASS] FtpPoll 0x20 = 0x4
NvmSectorWriting 39 ...
[PASS] FtpPoll 0x20 = 0x4
NvmSectorWriting 40 ...
[PASS] FtpPoll 0x20 = 0x4
NvmSectorWriting 41 ...
[PASS] FtpPoll 0x20 = 0x4
NvmSectorWriting 42 ...
[PASS] FtpPoll 0x20 = 0x4
NvmSectorWriting 43 ...
[PASS] FtpPoll 0x20 = 0x4
NvmSectorWriting 44 ...
[PASS] FtpPoll 0x20 = 0x4
NvmSectorWriting 45 ...
[PASS] FtpPoll 0x20 = 0x4
NvmSectorWriting 46 ...
[PASS] FtpPoll 0x20 = 0x4
NvmSectorWriting 47 ...
[PASS] FtpPoll 0x20 = 0x4
NvmSectorWriting 48 ...
[PASS] FtpPoll 0x20 = 0x4
NvmSectorWriting 49 ...
[PASS] FtpPoll 0x20 = 0x4
NvmSectorWriting 50 ...
[PASS] FtpPoll 0x20 = 0x4
NvmSectorWriting 51 ...
[PASS] FtpPoll 0x20 = 0x4
NvmSectorWriting 52 ...
[PASS] FtpPoll 0x20 = 0x4
NvmSectorWriting 53 ...
[PASS] FtpPoll 0x20 = 0x4
NvmSectorWriting 62 ...
[PASS] FtpPoll 0x20 = 0x4
NvmSectorWriting 63 ...
[PASS] FtpPoll 0x20 = 0x4
system hw reset
[DONE] FtpPatchCfgWriting
Device ID 0x: 0050315634313243190000000F002B00
ChipID:0x0056 rev:2 patchid:0x1260 cfgid:0x121E
CHIPID_WBC86
[PASS] WBC86_update_patch_cfg
"""