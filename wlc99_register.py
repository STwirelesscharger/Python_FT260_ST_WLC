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
I2CREG_CHIP_ID	 = 0x0000 	# Len = 2
I2CREG_CHIP_REV	 = 0x0002 	# Len = 1
I2CREG_CUST_ID	 = 0x0003 	# Len = 1
I2CREG_ROM_ID	 = 0x0004 	# Len = 2
I2CREG_NVM_PATCH_ID	 = 0x0006 	# Len = 2
I2CREG_RAM_PATCH_ID	 = 0x0008 	# Len = 2
I2CREG_CFG_ID	 = 0x000A 	# Len = 2
I2CREG_PE_ID	 = 0x000C 	# Len = 1
I2CREG_PE_ADC_ID	 = 0x000D 	# Len = 1
I2CREG_CUST_INFO_ID	 = 0x000E 	# Len = 1
I2CREG_DEVICE_ID	 = 0x0010 	# Len = 16
I2CREG_SYS_CMD	 = 0x0020 	# Len = 1
BIT_SWITCH_2_TX	 = 0
#Switch to Qi TX commandWrite 1 to switch to Qi TX mode
BIT_SWITCH_2_RX	 = 1
#Switch to Qi RX commandWrite 1 to switch to Qi RX mode
BIT_FTP_WR	 = 2
#FTP write commandWrite 1 to write data to one sector. Each sector is 128bytes. The sector must be erased before writing. The ftp_wr_pwd must be filled with the password before setting this bit. The aux_addr register specifies the  FTP sector number. The aux_data_000 to aux_data_127 must be filled with the data to be written to the FTP sector. The ftp_wr_pwd and this register is self-cleared when the operation is completed.
BIT_FTP_RD	 = 3
#FTP read commandWrite 1 to read the data from one FTP sector into the aux_data_000 to  aux_data_127 registers. The aux_addr register specifies the FTP sector number. This bit is self-cleared when the operation is completed.
BIT_FTP_ERASE	 = 4
#FTP erase commandWrite 1 to erase one FTP sector. Each sector is 128bytes. The ftp_wr_pwd must be filled with the password before setting this bit. The aux_addr register specifies the  FTP sector number. The ftp_wr_pwd and this register is self-cleared when the operation is completed.
BIT_FTP_FULL_ERASE	 = 5
#FTP full erase commandWrite 1 to full erase FTP sector. The ftp_wr_pwd must be filled with the password before setting this bit. The ftp_wr_pwd and this register is self-cleared when the operation is completed.
BIT_RST_FTP_DIS	 = 6
#FTP disable Write 1 to perform device reset and stop any FTP loading or execution. This prepares the FTP for writing. This register is self-cleared when the operation is completed.
I2CREG_PWD	 = 0x0022 	# Len = 1
I2CREG_AUX_LEN	 = 0x0023 	# Len = 1
I2CREG_AUX_ADDR	 = 0x0024 	# Len = 4
I2CREG_SYS_ERR_LATCH	 = 0x002C 	# Len = 4
BIT_SYS_M0_HARDFAULT_ERR	 = 0
#0x0: No error0x1: Error present
BIT_HW_WDT_TRIGGER_ERR	 = 1
#0x0: Not triggered 0x1: Triggered
BIT_FTP_ERR	 = 2
#0x0: No error0x1: Error present
BIT_MI2C_ERR	 = 3
#0x0: No error0x1: Error present
BIT_FTP_BOOT_ERR	 = 4
#0x0: No error0x1: Error present
BIT_FTP_PE_ERR	 = 8
#0x0: No error0x1: Section header error0x2: Section CRC failed0x3: Reserved
BIT_FTP_CFG_ERR	 = 10
#0x0: No error0x1: Section header error0x2: Section CRC failed0x3: Reserved
BIT_FTP_PATCH_ERR	 = 12
#0x0: No error0x1: Section header error0x2: Section CRC failed0x3: Reserved
BIT_FTP_PI_ERR	 = 14
#0x0: No error0x1: Section header error0x2: Section CRC failed0x3: Reserved
BIT_FTP_PE_ADC_ERR	 = 16
#0x0: No error0x1: Section header error0x2: Section CRC failed0x3: Reserved
BIT_FTP_CUST_INFO_ERR	 = 18
#FTP customer info section error0: No error1: Section header error2: Section CRC failed3: Skipped
I2CREG_GPIO0_FUNC	 = 0x0030 	# Len = 1
I2CREG_GPIO1_FUNC	 = 0x0031 	# Len = 1
I2CREG_GPIO2_FUNC	 = 0x0032 	# Len = 1
I2CREG_GPIO3_FUNC	 = 0x0033 	# Len = 1
I2CREG_GPIO4_FUNC	 = 0x0034 	# Len = 1
I2CREG_GPIO5_FUNC	 = 0x0035 	# Len = 1
I2CREG_GPIO6_FUNC	 = 0x0036 	# Len = 1
GPIO_FUNC_IN_FL           = 0x00 # in_fl:  No function (GPIO will be configured as Input floating)
GPIO_FUNC_IN_PU           = 0x01 # in_pu:  No function (GPIO will be configured as Input pull-up)
GPIO_FUNC_IN_PD           = 0x02 # in_pd:  No function (GPIO will be configured as Input pull-down)
GPIO_FUNC_PP_LO           = 0x03 # out_pp: No function (GPIO will be configured as output drive low)
GPIO_FUNC_PP_HI           = 0x04 # out_pp: No function (GPIO will be configured as output drive high)
GPIO_FUNC_INTB_OD         = 0x05 # out_od: Interrupt (0=active, 1=inactive, internal pull up)
GPIO_FUNC_FW_RDY          = 0x06 # out_pp: High on FW ready (before main loop)
GPIO_FUNC_LDO_BLOCK       = 0x07 # in_fl:  LDO block (0=unblock, 1=block)
GPIO_FUNC_RX_DIS_COM      = 0x08 # out_od:  Rx stop ASK communication (0=unblock, 1=block)
GPIO_FUNC_RX_PWR_OUT      = 0x09 # out_od: Power output enabled (0=off, 1=on)


I2CREG_DTS_SEND	 = 0x0038 	# Len = 2
BIT_DTS_ADC_SEND_LEN	 = 0
BIT_DTS_ADC_SEND_REQUEST	 = 8
#0x00: ADC/end0x02: ADC/auth0x05: ADC/rst0x10: ADC/prop0x11: ADC/prop0x12: ADC/prop0x13: ADC/prop0x14: ADC/prop0x15: ADC/prop0x16: ADC/prop0x17: ADC/prop0x18: ADC/prop0x19: ADC/prop0x1a: ADC/prop0x1b: ADC/prop0x1c: ADC/prop0x1d: ADC/prop0x1e: ADC/prop0x1f: ADC/prop
I2CREG_DTS_RCVD	 = 0x003A 	# Len = 2
BIT_DTS_ADC_RCVD_LEN	 = 0
BIT_DTS_ADC_RCVD_REQUEST	 = 8
#0x00: ADC/end0x02: ADC/auth0x05: ADC/rst0x10: ADC/prop0x11: ADC/prop0x12: ADC/prop0x13: ADC/prop0x14: ADC/prop0x15: ADC/prop0x16: ADC/prop0x17: ADC/prop0x18: ADC/prop0x19: ADC/prop0x1a: ADC/prop0x1b: ADC/prop0x1c: ADC/prop0x1d: ADC/prop0x1e: ADC/prop0x1f: ADC/prop.
I2CREG_OP_FREQ	 = 0x003E 	# Len = 2
I2CREG_MEAS_S32	 = 0x0040 	# Len = 4
BIT_MEAS_ICUR	 = 0
I2CREG_MEAS_S16	 = 0x0044 	# Len = 10
BIT_MEAS_VRECT	 = 0
BIT_MEAS_VOUT	 = 16
BIT_MEAS_TVOUT	 = 32
BIT_MEAS_ADC_IN	 = 48
BIT_MEAS_NTC	 = 64
I2CREG_RX_RCVD_PWR	 = 0x0054 	# Len = 4
I2CREG_TX_TFRD_PWR	 = 0x0058 	# Len = 2
I2CREG_LAST_RP	 = 0x005A 	# Len = 2
I2CREG_LAST_CE	 = 0x005C 	# Len = 2
I2CREG_SIGNAL_STRENGTH	 = 0x005E 	# Len = 1
I2CREG_FOD_PARAM_U16	 = 0x0060 	# Len = 16
BIT_FOD_CUR_THRES1_10MA	 = 0
BIT_FOD_CUR_THRES2_10MA	 = 16
BIT_FOD_CUR_THRES3_10MA	 = 32
BIT_FOD_CUR_THRES4_10MA	 = 48
BIT_FOD_CUR_THRES5_10MA	 = 64
BIT_FOD_CUR_THRES6_10MA	 = 80
BIT_FOD_CUR_THRES7_10MA	 = 96
BIT_FOD_CUR_THRES8_10MA	 = 112
I2CREG_FOD_PARAM_S8	 = 0x0070 	# Len = 9
BIT_FOD_OFFSET0	 = 0
BIT_FOD_OFFSET1	 = 8
BIT_FOD_OFFSET2	 = 16
BIT_FOD_OFFSET3	 = 24
BIT_FOD_OFFSET4	 = 32
BIT_FOD_OFFSET5	 = 40
BIT_FOD_OFFSET6	 = 48
BIT_FOD_OFFSET7	 = 56
BIT_FOD_OFFSET8	 = 64
I2CREG_FOD_PARAM_U8	 = 0x0079 	# Len = 1
BIT_RSER_4MOHM	 = 0
I2CREG_FOD_PARAM_S8_END	 = 0x007A 	# Len = 1
BIT_FOD_GAIN_OFFSET	 = 0
I2CREG_PTC	 = 0x007B 	# Len = 7
BIT_MINOR_VER	 = 0
#Power Transfer Contract Qi spec minor version number.
BIT_OB	 = 6
#Qi Power transfer contract. Out-of-band communications functionality is supported (ONE) or not supported (ZERO).
BIT_AI	 = 7
#Qi Power transfer contract. Authentication functionality is supported (ONE) or not supported (ZERO).
BIT_PCH	 = 8
#Qi Power Transfer Contract. Power Control Hold-off Time (in ms)in the range of 5 ms up to (and including) 205 ms.
BIT_RPR_HDR	 = 16
#0x31: RP24 format0x04: RP8 format
BIT_REF_PWR	 = 24
BIT_WIN_OFFSET	 = 32
#Received Power window offset. Specified in uinits of 4ms. Keep default value (changing requires system level review).
BIT_WIN_SZ	 = 35
#Received Power window offset. Specified in uinits of 4ms. Keep default value (changing requires system level review).
BIT_DUP	 = 40
#Qi Power transfer contract. Simultaneous incoming and outgoing data streams are supported (ONE) or not supported (ZERO).
BIT_BUFF_SIZE	 = 41
#Qi Power Transfer Contract. The size of the transport-layer buffer for receiving a data transport stream. The number of bytes in the buffer is equal to 16*2^n, with n the value contained in the Buffer Size field.Range 16 to 2048 bytes
BIT_FSK_DEPTH	 = 44
#Qi Power Transfer contract.FSK modulation depth
BIT_FSK_POLARITY	 = 46
#Qi Power transfer contract. The requested FSK polarity is positive (ZERO) or negative (ONE).
BIT_NEG	 = 47
#0x0: BPP0x1: EPP
BIT_GUA_PWR	 = 48
#Qi 1.3 Guaranteed Power Field. This value should be 2x of power in watt.Qi spec max is 63/2 watt.
I2CREG_PTC_END	 = 0x0082 	# Len = 1
BIT_REPING_DELAY	 = 0
#Qi 1.3 Power Transfer Contract re-ping delay. In units of 200ms, Max is 12.6s
I2CREG_OP_SUB_MODE	 = 0x008E 	# Len = 1
I2CREG_OP_MODE	 = 0x008F 	# Len = 1
I2CREG_RX_INTR_LATCH	 = 0x0090 	# Len = 4
BIT_RX_OVTP_INTR_LATCH	 = 0
#0x0: Did not occur0x1: Occurred
BIT_RX_OCP_INTR_LATCH	 = 1
#0x0: Did not occur0x1: Occurred
BIT_RX_OVP_INTR_LATCH	 = 2
#0x0: Did not occur0x1: Occurred
BIT_RX_SYS_ERR_INTR_LATCH	 = 3
#0x0: Did not occur0x1: Occurred.
BIT_RX_UVLO_INTR_LATCH	 = 4
BIT_RX_RCVD_MSG_INTR_LATCH	 = 5
#0x0: Did not occur0x1: Occurred
BIT_RX_OUTPUT_ON_INTR_LATCH	 = 6
#0x0: Did not occur0x1: Occurred
BIT_RX_OUTPUT_OFF_INTR_LATCH	 = 7
#0x0: Did not occur0x1: Occurred
BIT_RX_SEND_PKT_SUCCESS_INTR_LATCH	 = 8
#0x0: Did not occur0x1: Occurred
BIT_RX_SEND_PKT_TIMEOUT_INTR_LATCH	 = 9
#0x0: Did not occur0x1: Occurred
BIT_RX_SIG_STR_INTR_LATCH	 = 10
#0x0: Did not occur0x1: Occurred
BIT_RX_VRECT_RDY_INTR_LATCH	 = 11
#0x0: Did not occur0x1: Occurred
BIT_RX_TX_REMOVAL_LATCH	 = 12
#0x0: Did not occur0x1: Occurred
BIT_RX_PWRTFR_RP24_NACK_LATCH	 = 13
#Interrupt pending latch status0: No pending interrupt1: Pending interruptSee xxx_intr_clr register for details.
BIT_RX_NTC_ADC_INTR_LATCH	 = 15
#0x0: Did not occur0x1: Occurred
BIT_RX_DTS_SEND_SUCCESS_INTR_LATCH	 = 16
#0x0: Did not occur0x1: Occurred
BIT_RX_DTS_SEND_END_TIMEOUT_INTR_LATCH	 = 17
#0x0: Did not occur0x1: Occurred
BIT_RX_DTS_RCVD_SUCCESS_INTR_LATCH	 = 18
#0x0: Did not occur0x1: Occurred
BIT_RX_DTS_RCVD_END_TIMEOUT_INTR_LATCH	 = 19
#0x0: Did not occur0x1: Occurred
BIT_RX_EXT5V_FAULT_INTR_LATCH	 = 20
#0x0: Did not occur0x1: Occured
BIT_RX_EXT5V_DISCONNECTED_INTR_LATCH	 = 21
#Interrupt pending latch status0: No pending interrupt1: Pending interruptSee xxx_intr_clr register for details.
I2CREG_RX_INTR_CLR	 = 0x0094 	# Len = 4
BIT_RX_OVTP_INTR_CLR	 = 0
#0x0: No change0x1: Will be cleared
BIT_RX_OCP_INTR_CLR	 = 1
#0x0: No change0x1: Will be cleared
BIT_RX_OVP_INTR_CLR	 = 2
#0x0: No change0x1: Will be cleared
BIT_RX_SYS_ERR_INTR_CLR	 = 3
#0x0: No change0x1: Will be cleared
BIT_RX_UVLO_INTR_CLR	 = 4
BIT_RX_RCVD_MSG_INTR_CLR	 = 5
#0x0: No change0x1: Will be cleared
BIT_RX_OUTPUT_ON_INTR_CLR	 = 6
#0x0: No change0x1: Will be cleared
BIT_RX_OUTPUT_OFF_INTR_CLR	 = 7
#0x0: No change0x1: Will be cleared
BIT_RX_SEND_PKT_SUCCESS_INTR_CLR	 = 8
#0x0: No change0x1: Will be cleared
BIT_RX_SEND_PKT_TIMEOUT_INTR_CLR	 = 9
#0x0: No change0x1: Will be cleared
BIT_RX_SIG_STR_INTR_CLR	 = 10
#0x0: No change0x1: Will be cleared
BIT_RX_VRECT_RDY_INTR_CLR	 = 11
#0x0: No change0x1: Will be cleared
BIT_RX_TX_REMOVAL_CLR	 = 12
#0x0: No change0x1: Will be cleared
BIT_RX_PWRTFR_RP24_NACK_CLR	 = 13
#Write 1 to clear corresponding interrupt latch (xxx_intr_latch)
BIT_RX_NTC_ADC_INTR_CLR	 = 15
#0x0: No change0x1: Will be cleared
BIT_RX_DTS_SEND_SUCCESS_INTR_CLR	 = 16
#0x0: No change0x1: Will be cleared
BIT_RX_DTS_SEND_END_TIMEOUT_INTR_CLR	 = 17
#0x0: No change0x1: Will be cleared
BIT_RX_DTS_RCVD_SUCCESS_INTR_CLR	 = 18
#0x0: No change0x1: Will be cleared
BIT_RX_DTS_RCVD_END_TIMEOUT_INTR_CLR	 = 19
#0x0: No change0x1: Will be cleared
BIT_RX_EXT5V_FAULT_INTR_CLR	 = 20
#0x0: No change0x1: Will be cleared
BIT_RX_EXT5V_DISCONNECTED_INTR_CLR	 = 21
#Write 1 to clear corresponding interrupt latch (xxx_intr_latch)
I2CREG_RX_INTR_EN	 = 0x0098 	# Len = 4
BIT_RX_OVTP_INTR_EN	 = 0
#0x0: Disabled0x1: Enabled
BIT_RX_OCP_INTR_EN	 = 1
#0x0: Disabled0x1: Enabled
BIT_RX_OVP_INTR_EN	 = 2
#0x0: Disabled0x1: Enabled
BIT_RX_SYS_ERR_INTR_EN	 = 3
#0x0: Disabled0x1: Enabled
BIT_RX_UVLO_INTR_EN	 = 4
#under voltage protection interrupt enable0: Disable1: Enable
BIT_RX_RCVD_MSG_INTR_EN	 = 5
#0x0: Disabled0x1: Enabled
BIT_RX_OUTPUT_ON_INTR_EN	 = 6
#0x0: Disabled0x1: Enabled
BIT_RX_OUTPUT_OFF_INTR_EN	 = 7
#0x0: Disabled0x1: Enabled
BIT_RX_SEND_PKT_SUCCESS_INTR_EN	 = 8
#0x0: Disabled0x1: Enabled
BIT_RX_SEND_PKT_TIMEOUT_INTR_EN	 = 9
#0x0: Disabled0x1: Enabled
BIT_RX_SIG_STR_INTR_EN	 = 10
#0x0: Disabled0x1: Enabled
BIT_RX_VRECT_RDY_INTR_EN	 = 11
#0x0: Disabled0x1: Enabled
BIT_RX_TX_REMOVAL_EN	 = 12
#0x0: Disabled0x1: Enabled
BIT_RX_PWRTFR_RP24_NACK_EN	 = 13
#Received NACK for normal mode RP24 during power transfer.0: Disable1: Enable
BIT_RX_NTC_ADC_INTR_EN	 = 15
#0x0: Disabled0x1: Enabled
BIT_RX_DTS_SEND_SUCCESS_INTR_EN	 = 16
#0x0: Disabled0x1: Enabled
BIT_RX_DTS_SEND_END_TIMEOUT_INTR_EN	 = 17
#0x0: Disabled0x1: Enabled
BIT_RX_DTS_RCVD_SUCCESS_INTR_EN	 = 18
#0x0: Disabled0x1: Enabled
BIT_RX_DTS_RCVD_END_TIMEOUT_INTR_EN	 = 19
#0x0: Disabled0x1: Enabled
BIT_RX_EXT5V_FAULT_INTR_EN	 = 20
#0x0: Disabled0x1: Enabled
BIT_RX_EXT5V_DISCONNECTED_INTR_EN	 = 21
#Internal5V LDO reverted back to 5V and enabled due to either Tx removal or Host disconnected the ext 5V interrupt enable0 - Disable1 - Enable
I2CREG_RX_STAT	 = 0x009C 	# Len = 4
BIT_RX_OVTP_STAT	 = 0
#0x0: Is not occuring0x1: Occurring
BIT_RX_OCP_STAT	 = 1
#0x0: Is not occuring0x1: Occurring
BIT_RX_OVP_STAT	 = 2
#0x0: Is not occuring0x1: Occurring
BIT_RX_SYS_ERR_STAT	 = 3
#0x0: Is not occuring0x1: Occurring
BIT_RX_UVLO_STAT	 = 4
BIT_RX_RCVD_MSG_STAT	 = 5
#0x0: Is not occuring0x1: Occurring
BIT_RX_OUTPUT_ON_STAT	 = 6
#0x0: Is not occuring0x1: Occurring
BIT_RX_OUTPUT_OFF_STAT	 = 7
#0x0: Is not occuring0x1: Occurring
BIT_RX_SEND_PKT_SUCCESS_INTR	 = 8
#0x0: Is not occuring0x1: Occurring
BIT_RX_SEND_PKT_TIMEOUT_INTR	 = 9
#0x0: Is not occuring0x1: Occurring
BIT_RX_SIG_STR_STAT	 = 10
#0x0: Is not occuring0x1: Occurring
BIT_RX_VRECT_RDY_STAT	 = 11
#0x0: Is not occuring0x1: Occurring
BIT_RX_TX_REMOVAL_STAT	 = 12
#0x0: Is not occuring0x1: Occurring
BIT_RX_PWRTFR_RP24_NACK_STAT	 = 13
#Live status of corresponding interrupt
BIT_RX_NTC_ADC_INTR_STAT	 = 15
#0x0: Is not occuring0x1: Occurring
BIT_RX_DTS_SEND_SUCCESS_STAT	 = 16
#0x0: Is not occuring0x1: Occurring
BIT_RX_DTS_SEND_END_TIMEOUT_STAT	 = 17
#0x0: Is not occuring0x1: Occurring
BIT_RX_DTS_RCVD_SUCCESS_STAT	 = 18
#0x0: Is not occuring0x1: Occurring
BIT_RX_DTS_RCVD_END_TIMEOUT_STAT	 = 19
#0x0: Is not occuring0x1: Occurring
BIT_RX_EXT5V_FAULT_INTR_STAT	 = 20
#0x0: Is not occuring0x1: Occuring
BIT_RX_EXT5V_DISCONNECTED_INTR_STAT	 = 21
#Jun Yi LEE:[RX]Live status of corresponding interrupt
I2CREG_RX_CMD	 = 0x00A0 	# Len = 2
BIT_RX_VOUT_ON	 = 0
#0x0: Do nothing0x1: Perform switch
BIT_RX_VOUT_OFF	 = 1
#0x0: Do nothing0x1: Perform switch
BIT_RX_SEND_MSG	 = 2
#0x0: Do nothing0x1: Perform action
BIT_RX_SEND_MSG_WAIT_REPLY	 = 3
#0x0: Do nothing0x1: Perform action
BIT_RX_SEND_EPT	 = 4
#0x0: Do nothing0x1: Perform action
BIT_RX_SEND_DTS	 = 5
#0x0: Do nothing0x1: Perform action
I2CREG_RX_CMD1	 = 0x00A1
BIT_RX_EXT5V_ON	 = 0
#0x0: Do nothing0x1: Perform command
BIT_RX_EXT5V_OFF	 = 1
#0x0: Do nothing0x1: Perform command
I2CREG_RX_LDO_CUR_THRES	 = 0x00A2 	# Len = 3
BIT_RX_LDO_CUR_THRES1_10MA	 = 0
BIT_RX_LDO_CUR_THRES2_10MA	 = 8
BIT_RX_LDO_CUR_THRES3_10MA	 = 16
I2CREG_RX_LDO_DROP	 = 0x00A5 	# Len = 4
BIT_RX_LDO_DROP0	 = 0
BIT_RX_LDO_DROP1	 = 8
BIT_RX_LDO_DROP2	 = 16
BIT_RX_LDO_DROP3	 = 24
I2CREG_RX_EPT_MSG	 = 0x00A9 	# Len = 1
I2CREG_RX_VOUT_SET	 = 0x00AA 	# Len = 2
I2CREG_RX_ILIM_SET	 = 0x00B2 	# Len = 1
I2CREG_RX_ARC_AUTO_OFF_THRES	 = 0x00B3 	# Len = 1
I2CREG_RX_SC_RP24_MAX_PWR = 0x00B4
I2CREG_MAX_PWR_SWICH = 0x00B5
I2CREG_TX_INTR_LATCH	 = 0x00C0 	# Len = 4
BIT_TX_OVTP_INTR_LATCH	 = 0
#Interrupt pending latch status0: No pending interrupt1: Pending interruptSee xxx_intr_clr register for details.
BIT_TX_OCP_INTR_LATCH	 = 1
#Interrupt pending latch status0: No pending interrupt1: Pending interruptSee xxx_intr_clr register for details.
BIT_TX_OVP_INTR_LATCH	 = 2
#Interrupt pending latch status0: No pending interrupt1: Pending interruptSee xxx_intr_clr register for details.
BIT_TX_SYS_ERR_INTR_LATCH	 = 3
#Interrupt pending latch status0: No pending interrupt1: Pending interruptSee xxx_intr_clr register for details.
BIT_TX_RP_PKT_RVCD_INTR_LATCH	 = 4
#Interrupt pending latch status0: No pending interrupt1: Pending interruptSee xxx_intr_clr register for details.
BIT_TX_CE_PKT_RVCD_INTR_LATCH	 = 5
#Interrupt pending latch status0: No pending interrupt1: Pending interruptSee xxx_intr_clr register for details.
BIT_TX_PKT_SENT_INTR_LATCH	 = 6
#Interrupt pending latch status0: No pending interrupt1: Pending interruptSee xxx_intr_clr register for details.
BIT_TX_EXT_MON_INTR_LATCH	 = 7
#Interrupt pending latch status0: No pending interrupt1: Pending interruptSee xxx_intr_clr register for details.
BIT_TX_CE_TO_INTR_LATCH	 = 8
#Interrupt pending latch status0: No pending interrupt1: Pending interruptSee xxx_intr_clr register for details.
BIT_TX_RP_TO_INTR_LATCH	 = 9
#Interrupt pending latch status0: No pending interrupt1: Pending interruptSee xxx_intr_clr register for details.
BIT_TX_EPT_INTR_LATCH	 = 10
#Interrupt pending latch status0: No pending interrupt1: Pending interruptSee xxx_intr_clr register for details.
BIT_TX_START_PING_INTR_LATCH	 = 11
#Interrupt pending latch status0: No pending interrupt1: Pending interruptSee xxx_intr_clr register for details.
BIT_TX_SS_PKT_RCVD_INTR_LATCH	 = 12
#Interrupt pending latch status0: No pending interrupt1: Pending interruptSee xxx_intr_clr register for details.
BIT_TX_ID_PKT_RVCD_INTR_LATCH	 = 13
#Interrupt pending latch status0: No pending interrupt1: Pending interruptSee xxx_intr_clr register for details.
BIT_TX_CFG_PKT_RCVD_INTR_LATCH	 = 14
#Interrupt pending latch status0: No pending interrupt1: Pending interruptSee xxx_intr_clr register for details.
BIT_TX_PP_PKT_RCVD_INTR_LATCH	 = 15
#Interrupt pending latch status0: No pending interrupt1: Pending interruptSee xxx_intr_clr register for details.
BIT_TX_BRDG_MD_INTR_LATCH	 = 16
#Interrupt pending latch status0: No pending interrupt1: Pending interruptSee xxx_intr_clr register for details.
BIT_TX_FOD_DET_INTR_LATCH	 = 17
#Interrupt pending latch status0: No pending interrupt1: Pending interruptSee xxx_intr_clr register for details.
BIT_TX_PTC_UPDATE_INT_LATCH	 = 18
#set when the power transfer contract is successfully updated after negotiation/renegotiation
BIT_TX_DTS_SEND_SUCCESS_INTR_LATCH	 = 19
#Interrupt pending latch status0: No pending interrupt1: Pending interruptSee xxx_intr_clr register for details.
BIT_TX_DTS_SEND_END_TIMEOUT_INTR_LATCH	 = 20
#Interrupt pending latch status0: No pending interrupt1: Pending interruptSee xxx_intr_clr register for details.
BIT_TX_DTS_SEND_END_RESET_INTR_LATCH	 = 21
#Interrupt pending latch status0: No pending interrupt1: Pending interruptSee xxx_intr_clr register for details.
BIT_TX_DTS_RCVD_SUCCESS_INTR_LATCH	 = 22
#Interrupt pending latch status0: No pending interrupt1: Pending interruptSee xxx_intr_clr register for details.
BIT_TX_DTS_RCVD_END_TIMEOUT_INTR_LATCH	 = 23
#Interrupt pending latch status0: No pending interrupt1: Pending interruptSee xxx_intr_clr register for details.
BIT_TX_DTS_RCVD_END_RESET_INTR_LATCH	 = 24
#Interrupt pending latch status0: No pending interrupt1: Pending interruptSee xxx_intr_clr register for details.
I2CREG_TX_INTR_CLR	 = 0x00C4 	# Len = 4
BIT_TX_OVTP_INTR_CLR	 = 0
#Write 1 to clear corresponding interrupt latch (xxx_intr_latch)
BIT_TX_OCP_INTR_CLR	 = 1
#Write 1 to clear corresponding interrupt latch (xxx_intr_latch)
BIT_TX_OVP_INTR_CLR	 = 2
#Write 1 to clear corresponding interrupt latch (xxx_intr_latch)
BIT_TX_SYS_ERR_INTR_CLR	 = 3
#Write 1 to clear corresponding interrupt latch (xxx_intr_latch)
BIT_TX_RP_PKT_RVCD_INTR_CLR	 = 4
#Write 1 to clear corresponding interrupt latch (xxx_intr_latch)
BIT_TX_CE_PKT_RVCD_INTR_CLR	 = 5
#Write 1 to clear corresponding interrupt latch (xxx_intr_latch)
BIT_TX_PKT_SENT_INTR_CLR	 = 6
#Write 1 to clear corresponding interrupt latch (xxx_intr_latch)
BIT_TX_EXT_MON_INTR_CLR	 = 7
#Write 1 to clear corresponding interrupt latch (xxx_intr_latch)
BIT_TX_CE_TO_INTR_CLR	 = 8
#Write 1 to clear corresponding interrupt latch (xxx_intr_latch)
BIT_TX_RP_TO_INTR_CLR	 = 9
#Write 1 to clear corresponding interrupt latch (xxx_intr_latch)
BIT_TX_EPT_INTR_CLR	 = 10
#Write 1 to clear corresponding interrupt latch (xxx_intr_latch)
BIT_TX_START_PING_INTR_CLR	 = 11
#Write 1 to clear corresponding interrupt latch (xxx_intr_latch)
BIT_TX_SS_PKT_RCVD_INTR_CLR	 = 12
#Write 1 to clear corresponding interrupt latch (xxx_intr_latch)
BIT_TX_ID_PKT_RVCD_INTR_CLR	 = 13
#Write 1 to clear corresponding interrupt latch (xxx_intr_latch)
BIT_TX_CFG_PKT_RCVD_INTR_CLR	 = 14
#Write 1 to clear corresponding interrupt latch (xxx_intr_latch)
BIT_TX_PP_PKT_RCVD_INTR_CLR	 = 15
#Write 1 to clear corresponding interrupt latch (xxx_intr_latch)
BIT_TX_BRDG_MD_INTR_CLR	 = 16
#Write 1 to clear corresponding interrupt latch (xxx_intr_latch)
BIT_TX_FOD_DET_INTR_CLR	 = 17
#Write 1 to clear corresponding interrupt latch (xxx_intr_latch)
BIT_TX_PTC_UPDATE_INT_CLR	 = 18
#write 1 to clear the interrupt
BIT_TX_DTS_SEND_SUCCESS_INTR_CLR	 = 19
#Write 1 to clear corresponding interrupt latch (xxx_intr_latch)
BIT_TX_DTS_SEND_END_TIMEOUT_INTR_CLR	 = 20
#Write 1 to clear corresponding interrupt latch (xxx_intr_latch)
BIT_TX_DTS_SEND_END_RESET_INTR_CLR	 = 21
#Write 1 to clear corresponding interrupt latch (xxx_intr_latch)
BIT_TX_DTS_RCVD_SUCCESS_INTR_CLR	 = 22
#Write 1 to clear corresponding interrupt latch (xxx_intr_latch)
BIT_TX_DTS_RCVD_END_TIMEOUT_INTR_CLR	 = 23
#Write 1 to clear corresponding interrupt latch (xxx_intr_latch)
BIT_TX_DTS_RCVD_END_RESET_INTR_CLR	 = 24
#Write 1 to clear corresponding interrupt latch (xxx_intr_latch)
I2CREG_TX_INTR_EN	 = 0x00C8 	# Len = 4
BIT_TX_OVTP_INTR_EN	 = 0
#Over temperature protection interrupt enable0: Disable1: Enable
BIT_TX_OCP_INTR_EN	 = 1
#Over current protection interrupt enable0: Disable1: Enable
BIT_TX_OVP_INTR_EN	 = 2
#Over voltage interrupt enable0: Disable1: Enable
BIT_TX_SYS_ERR_INTR_EN	 = 3
#System error interrupt enable0: Disable1: Enable
BIT_TX_RP_PKT_RVCD_INTR_EN	 = 4
#RP packet received interrupt enable0: Disable1: Enable
BIT_TX_CE_PKT_RVCD_INTR_EN	 = 5
#CE packet received interrupt enable0: Disable1: Enable
BIT_TX_PKT_SENT_INTR_EN	 = 6
#Packet sent interrupt enable0: Disable1: Enable
BIT_TX_EXT_MON_INTR_EN	 = 7
#Ext Tx Detect interrupt enable0: Disable1: Enable
BIT_TX_CE_TO_INTR_EN	 = 8
#CEP Timeout interrupt enable0 - Disable1 - Enable
BIT_TX_RP_TO_INTR_EN	 = 9
#RPP Timeout interrupt enable0 - Disable1 - Enable
BIT_TX_EPT_INTR_EN	 = 10
#AC powered down interrupt enable0: Disable1: Enable
BIT_TX_START_PING_INTR_EN	 = 11
#Ping started interrupt enable0: Disable1: Enable
BIT_TX_SS_PKT_RCVD_INTR_EN	 = 12
#ID packet received interrupt enable0: Disable1: Enable
BIT_TX_ID_PKT_RVCD_INTR_EN	 = 13
#ID packet received interrupt enable0: Disable1: Enable
BIT_TX_CFG_PKT_RCVD_INTR_EN	 = 14
#Configuration packet received interrupt enable0: Disable1: Enable
BIT_TX_PP_PKT_RCVD_INTR_EN	 = 15
#PP packet received interrupt enable0: Disable1: Enable
BIT_TX_BRDG_MD_INTR_EN	 = 16
#Bridge mode (half/full) changed interrupt enable0: Disable1: Enable
BIT_TX_FOD_DET_INTR_EN	 = 17
#Tx FOD detect interrupt enable0: Disable1: Enable
BIT_TX_PTC_UPDATE_INT_EN	 = 18
#the power transfer contract is successfully updated after negotiation/renegotiationo: Disable1: Enable
BIT_TX_DTS_SEND_SUCCESS_INTR_EN	 = 19
#DTS sending data stream successfully interrupt enable0: Disable1: Enable
BIT_TX_DTS_SEND_END_TIMEOUT_INTR_EN	 = 20
#DTS stopped sending due to timeout error interrupt enable0: Disable1: Enable
BIT_TX_DTS_SEND_END_RESET_INTR_EN	 = 21
#DTS stopped sending due to reset interrupt enable0: Disable1: Enable
BIT_TX_DTS_RCVD_SUCCESS_INTR_EN	 = 22
#DTS received data stream successfully interrupt enable0: Disable1: Enable
BIT_TX_DTS_RCVD_END_TIMEOUT_INTR_EN	 = 23
#DTS stopped receiving due to timeout error interrupt enable0: Disable1: Enable
BIT_TX_DTS_RCVD_END_RESET_INTR_EN	 = 24
#DTS stopped receiving due to reset interrupt enable0: Disable1: Enable
I2CREG_TX_STAT	 = 0x00CC 	# Len = 4
BIT_TX_OVTP_STAT	 = 0
#Live status of corresponding interrupt
BIT_TX_OCP_STAT	 = 1
#Live status of corresponding interrupt
BIT_TX_OVP_STAT	 = 2
#Live status of corresponding interrupt
BIT_TX_SYS_ERR_STAT	 = 3
#Live status of corresponding interrupt
BIT_TX_RP_PKT_RVCD_STAT	 = 4
#Live status of corresponding interrupt
BIT_TX_CE_PKT_RVCD_STAT	 = 5
#Live status of corresponding interrupt
BIT_TX_PKT_SENT_STAT	 = 6
#Live status of corresponding interrupt
BIT_TX_EXT_MON_INTR_STAT	 = 7
#Live status of corresponding interrupt
BIT_TX_CE_TO_INTR_STAT	 = 8
#Live status of corresponding interrupt
BIT_TX_RP_TO_INTR_STAT	 = 9
#Live status of corresponding interrupt
BIT_TX_EPT_STAT	 = 10
#Live status of corresponding interrupt
BIT_TX_START_PING_STAT	 = 11
#Live status of corresponding interrupt
BIT_TX_SS_PKT_RCVD_STAT	 = 12
#Live status of corresponding interrupt
BIT_TX_ID_PKT_RVCD_STAT	 = 13
#Live status of corresponding interrupt
BIT_TX_CFG_PKT_RCVD_STAT	 = 14
#Live status of corresponding interrupt
BIT_TX_PP_PKT_RCVD_STAT	 = 15
#Live status of corresponding interrupt
BIT_TX_BRDG_MD_INTR_STAT	 = 16
#Live status of corresponding interrupt
BIT_TX_FOD_DET_INTR_STAT	 = 17
#Live status of corresponding interrupt
BIT_TX_PTC_UPDATE_INT_STAT	 = 18
#Live status of power transfer contract update
BIT_TX_DTS_SEND_SUCCESS_STAT	 = 19
#Live status of corresponding interrupt
BIT_TX_DTS_SEND_END_TIMEOUT_STAT	 = 20
#Live status of corresponding interrupt
BIT_TX_DTS_SEND_END_RESET_STAT	 = 21
#Live status of corresponding interrupt
BIT_TX_DTS_RCVD_SUCCESS_STAT	 = 22
#Live status of corresponding interrupt
BIT_TX_DTS_RCVD_END_TIMEOUT_STAT	 = 23
#Live status of corresponding interrupt
BIT_TX_DTS_RCVD_END_RESET_STAT	 = 24
#Live status of corresponding interrupt
I2CREG_TX_CMD	 = 0x00D0 	# Len = 2
BIT_TX_EN	 = 0
#Enable the Tx. Write 1 to start Ping
BIT_TX_DIS	 = 1
#Disable the TX. Write 1 to stop the invertor and cut the power to Rx
BIT_TX_APING	 = 2
#Tx analog ping.
BIT_TX_SEND_MSG	 = 3
#Write 1 to send a packet to RX via FSK modulation. The message data is defined in aux_data_00 ~ aux_data_21 register. This bit is self-cleared when the command is handled.
BIT_TX_SEND_BC_MSG	 = 4
#Write 1 to send a backchannel packet to RX via FSK modulation. The message data is defined in aux_data_00 ~ aux_data_21 register. This bit is self-cleared when the command is completed.
BIT_TX_SEND_DTS	 = 5
#Write 1 to start DTS sending transactionThe aux_data_32 ~ aux_data_103 register specifies the data to be sent.
I2CREG_TX_MAX_FREQ	 = 0x00D2 	# Len = 2
I2CREG_TX_MIN_FREQ	 = 0x00D4 	# Len = 2
I2CREG_TX_PING_FREQ	 = 0x00D6 	# Len = 2
I2CREG_TX_MAX_DC	 = 0x00D8 	# Len = 1
I2CREG_TX_MIN_DC	 = 0x00D9 	# Len = 1
I2CREG_TX_PING_DC	 = 0x00DA 	# Len = 1
I2CREG_TX_PING_INTERVAL	 = 0x00DB 	# Len = 1
I2CREG_TX_PING_DUR	 = 0x00DC 	# Len = 1
I2CREG_TX_OVP_THRES	 = 0x00DD 	# Len = 1
I2CREG_TX_OCP_THRES	 = 0x00DE 	# Len = 1
I2CREG_TX_OVTP_THRES	 = 0x00DF 	# Len = 1
I2CREG_TX_FOD_PLOSS_THRES	 = 0x00E0 	# Len = 1
I2CREG_TX_FOD_DBNC_CNT	 = 0x00E1 	# Len = 1
I2CREG_TX_CE_TO_MAX_CNT	 = 0x00E2 	# Len = 1
I2CREG_TX_RP_TO_MAX_CNT	 = 0x00E3 	# Len = 1
I2CREG_TX_FHOP_STEP	 = 0x00E4 	# Len = 1
I2CREG_TX_PID_MAX_CUR	 = 0x00E5 	# Len = 1
I2CREG_TX_BRDG_MODE_CUR_THRES	 = 0x00E6 	# Len = 1
I2CREG_TX_EPT_REASON_RCVD	 = 0x00E7 	# Len = 3
BIT_TX_EPT_SRC_OVP	 = 0
#Over voltage protection triggered
BIT_TX_EPT_SRC_OCP	 = 1
#Over current protection triggered
BIT_TX_EPT_SRC_OVTP	 = 2
#Over temperature protection triggered
BIT_TX_EPT_SRC_FOD	 = 3
#Foreign object detected
BIT_TX_EPT_SRC_CMD	 = 4
#Host issued EPT command
BIT_TX_EPT_SRC_RX	 = 5
#EPT Source Rx EPT packet
BIT_TX_EPT_SRC_CE_TO	 = 6
#Control error packet timeout
BIT_TX_EPT_SRC_RP_TO	 = 7
#Received power packet timeout
BIT_TX_EPT_SRC_RX_RST	 = 8
#Rx send SS/ID/CFG
BIT_TX_EPT_SRC_SYS_ERR	 = 9
BIT_TX_EPT_SRC_SS_TO	 = 10
#Ping timeout
BIT_TX_EPT_SRC_SS	 = 11
#Signal strength packet error
BIT_TX_EPT_SRC_ID	 = 12
#Identification packet error
BIT_TX_EPT_SRC_CFG	 = 13
#Number optional packets received doesn't match with number in configuration packet
BIT_TX_EPT_SRC_CFG_CNT_ERR	 = 14
#Number optional packets received doesn't match with number in configuration packet
BIT_TX_EPT_SRC_PCH	 = 15
#Power control hold-off packet error
BIT_TX_EPT_SRC_XID	 = 16
#Extended identification packet error
BIT_TX_EPT_SRC_NEGO	 = 17
BIT_TX_EPT_SRC_NEGO_TO	 = 18
I2CREG_TX_OP_DC	 = 0x00EA 	# Len = 1
I2CREG_TX_CTRL	 = 0x00EB 	# Len = 1
BIT_TX_BRDG_MD	 = 0
#Tx power transfer half bridge / full bridge mode control.0 - No change (same as ping)1 - Manual half bridge mode2 - Manual full bridge mode3 - Auto switch
BIT_TX_PING_HALF_BRDG	 = 2
#Tx ping in half bridge mode.0 - Disable (Start ping in full bridge mode)1 - Enable (Start ping in half bridge mode)
I2CREG_Q_EXCITATION_PERIOD	 = 0x00EC 	# Len = 2
I2CREG_Q_MEAS_RESONANT_FREQ	 = 0x00EE 	# Len = 2
I2CREG_Q_MEAS_QFACTOR	 = 0x00F0 	# Len = 2
I2CREG_Q_MEAS_ADC	 = 0x00F2 	# Len = 2
I2CREG_AUX_DATA	 = 0x0100
I2CREG_SEND_MSG	 = 0x0200
I2CREG_RCVD_MSG  = 0x0216
DTS_SEND_MSG_000        = 0X0100
DTS_RCVD_MSG_000        = 0x0180
#HW reg address
HWREG_GPIO_INPUT_VAL_RegAddr = 0x2001A01C
