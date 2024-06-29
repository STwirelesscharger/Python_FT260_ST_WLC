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
I2CREG_FTP_PATCH_ID	 = 0x0006 	# Len = 2
I2CREG_RAM_PATCH_ID	 = 0x0008 	# Len = 2
I2CREG_CFG_ID	 = 0x000A 	# Len = 2
I2CREG_PE_ID	 = 0x000C 	# Len = 2
I2CREG_OP_MODE	 = 0x000E 	# Len = 1
I2CREG_OP_SUB_MODE	 = 0x000F 	# Len = 1
I2CREG_DEVICE_ID	 = 0x0010 	# Len = 16
I2CREG_SYS_CMD	 = 0x0020 	# Len = 2
BIT_SWITCH_2_TX	 = 0
#0x0: Do nothing0x1: Perform switch
BIT_SWITCH_2_RX	 = 1
#0x0: Do nothing0x1: Perform switch
BIT_FTP_WR	 = 2
#FTP write commandWrite 1 to write data to one sector. Each sector is 128bytes. The sector must be erased before writing. The ftp_wr_pwd must be filled with the password before setting this bit. The aux_addr register specifies the  FTP sector number. The aux_data_000 to aux_data_127 must be filled with the data to be written to the FTP sector. The ftp_wr_pwd and this register is self-cleared when the operation is completed.
BIT_FTP_RD	 = 3
#FTP read commandWrite 1 to read the data from one FTP sector into the aux_data_000 to  aux_data_127 registers. The aux_addr register specifies the FTP sector number. This bit is self-cleared when the operation is completed.
BIT_FTP_ERASE	 = 4
#FTP erase commandWrite 1 to erase one FTP sector. Each sector is 128bytes. The ftp_wr_pwd must be filled with the password before setting this bit. The aux_addr register specifies the  FTP sector number. The ftp_wr_pwd and this register is self-cleared when the operation is completed.
BIT_FTP_FULL_ERASE	 = 5
#FTP full erase commandWrite 1 to full erase FTP sector. The ftp_wr_pwd must be filled with the password before setting this bit. The ftp_wr_pwd and this register is self-cleared when the operation is completed.
BIT_RST_FTP_DIS	 = 6
#disbale FTP after resetwrite 1 to disable write 0 to enable
I2CREG_AUX_LEN	 = 0x0023 	# Len = 1
I2CREG_AUX_ADDR	 = 0x0024 	# Len = 4
I2CREG_SYS_ERR_LATCH	 = 0x002C 	# Len = 4
BIT_SYS_M3_HARDFAULT_ERR	 = 0
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
I2CREG_GPIO0_FUNC	 = 0x0030 	# Len = 1
I2CREG_GPIO1_FUNC	 = 0x0031 	# Len = 1
I2CREG_GPIO2_FUNC	 = 0x0032 	# Len = 1
I2CREG_GPIO3_FUNC	 = 0x0033 	# Len = 1
I2CREG_GPIO4_FUNC	 = 0x0034 	# Len = 1
I2CREG_GPIO5_FUNC	 = 0x0035 	# Len = 1
I2CREG_GPIO6_FUNC	 = 0x0036 	# Len = 1
I2CREG_RX_INTR_EN	 = 0x0080 	# Len = 4

GPIO_FUNC_IN_FL           = 0x00 # in_fl:  No function (GPIO will be configured as Input floating)
GPIO_FUNC_IN_PU           = 0x01 # in_pu:  No function (GPIO will be configured as Input pull-up)
GPIO_FUNC_IN_PD           = 0x02 # in_pd:  No function (GPIO will be configured as Input pull-down)
GPIO_FUNC_PP_LO           = 0x03 # out_pp: No function (GPIO will be configured as output drive low)
GPIO_FUNC_PP_HI           = 0x04 # out_pp: No function (GPIO will be configured as output drive high)
GPIO_FUNC_INTB_OD         = 0x05 # out_od: Interrupt (0=active, 1=inactive, internal pull up)
GPIO_FUNC_INTB_PP         = 0x06 # out_pp: Interrupt (0=active, 1=inactive, useful with long wires)
GPIO_FUNC_FW_RDY          = 0x07 # out_pp: High on FW ready (before main loop)
GPIO_FUNC_LDO_BLOCK       = 0x08 # in_pd:  LDO block (0=unblock, 1=block)
GPIO_FUNC_RX_DIS_COM      = 0x09 # in_pd:  Rx stop ASK communication (0=unblock, 1=block)
GPIO_FUNC_RX_PWR_OUT      = 0x0A # out_pp: Power output enabled (0=off, 1=on)
GPIO_FUNC_RX_PWR_OUT_OD   = 0x0B # out_od: Power output enabled (0=on, 1=off)

BIT_RX_OVTP_INTR_EN	 = 0
#0x0: Disabled0x1: Enabled
BIT_RX_OCP_INTR_EN	 = 1
#0x0: Disabled0x1: Enabled
BIT_RX_OVP_INTR_EN	 = 2
#0x0: Disabled0x1: Enabled
BIT_RX_SYS_ERR_INTR_EN	 = 3
#0x0: Disabled0x1: Enabled
BIT_RX_EXT5V_TX_REMOVAL_EN	 = 4
#0x0: Disabled0x1: Enabled
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
BIT_RX_SCP_INTR_EN	 = 12
#0x0: Disabled0x1: Enabled
BIT_RX_VOUT_LOW_EN	 = 13
#0x0: Disabled0x1: Enabled
BIT_RX_DTS_SEND_SUCCESS_INTR_EN	 = 16
#0x0: Disabled0x1: Enabled
BIT_RX_DTS_SEND_END_TIMEOUT_INTR_EN	 = 17
#0x0: Disabled0x1: Enabled
BIT_RX_DTS_SEND_END_RESET_INTR_EN	 = 18
#0x0: Disabled0x1: Enabled
BIT_RX_DTS_RCVD_SUCCESS_INTR_EN	 = 20
#0x0: Disabled0x1: Enabled
BIT_RX_DTS_RCVD_END_TIMEOUT_INTR_EN	 = 21
#0x0: Disabled0x1: Enabled
BIT_RX_DTS_RCVD_END_RESET_INTR_EN	 = 22
#0x0: Disabled0x1: Enabled
BIT_RX_AUTH_END_INTR_EN	 = 23
#0x0: Disabled0x1: Enabled
I2CREG_RX_INTR_CLR	 = 0x0084 	# Len = 4
BIT_RX_OVTP_INTR_CLR	 = 0
#0x0: No change0x1: Will be cleared
BIT_RX_OCP_INTR_CLR	 = 1
#0x0: No change0x1: Will be cleared
BIT_RX_OVP_INTR_CLR	 = 2
#0x0: No change0x1: Will be cleared
BIT_RX_SYS_ERR_INTR_CLR	 = 3
#0x0: No change0x1: Will be cleared
BIT_RX_EXT5V_TX_REMOVAL_CLR	 = 4
#0x0: No change0x1: Will be cleared
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
BIT_RX_SCP_INTR_CLR	 = 12
#0x0: No change0x1: Will be cleared
BIT_RX_VOUT_LOW_CLR	 = 13
#0x0: No change0x1: Will be cleared
BIT_RX_DTS_SEND_SUCCESS_INTR_CLR	 = 16
#0x0: No change0x1: Will be cleared
BIT_RX_DTS_SEND_END_TIMEOUT_INTR_CLR	 = 17
#0x0: No change0x1: Will be cleared
BIT_RX_DTS_SEND_END_RESET_INTR_CLR	 = 18
#0x0: No change0x1: Will be cleared
BIT_RX_DTS_RCVD_SUCCESS_INTR_CLR	 = 20
#0x0: No change0x1: Will be cleared
BIT_RX_DTS_RCVD_END_TIMEOUT_INTR_CLR	 = 21
#0x0: No change0x1: Will be cleared
BIT_RX_DTS_RCVD_END_RESET_INTR_CLR	 = 22
#0x0: No change0x1: Will be cleared
BIT_RX_AUTH_END_INTR_CLR	 = 23
#0x0: No change0x1: Will be cleared
I2CREG_RX_INTR_LATCH	 = 0x0088 	# Len = 4
BIT_RX_OVTP_INTR_LATCH	 = 0
#0x0: Did not occur0x1: Occurred
BIT_RX_OCP_INTR_LATCH	 = 1
#0x0: Did not occur0x1: Occurred
BIT_RX_OVP_INTR_LATCH	 = 2
#0x0: Did not occur0x1: Occurred
BIT_RX_SYS_ERR_INTR_LATCH	 = 3
#0x0: Did not occur0x1: Occurred
BIT_RX_EXT5V_TX_REMOVAL_LATCH	 = 4
#0x0: Did not occur0x1: Occurred
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
BIT_RX_SCP_INTR_LATCH	 = 12
#0x0: Did not occur0x1: Occurred
BIT_RX_VOUT_LOW_LATCH	 = 13
#0x0: Did not occur0x1: Occurred
BIT_RX_DTS_SEND_SUCCESS_INTR_LATCH	 = 16
#0x0: Did not occur0x1: Occurred
BIT_RX_DTS_SEND_END_TIMEOUT_INTR_LATCH	 = 17
#0x0: Did not occur0x1: Occurred
BIT_RX_DTS_SEND_END_RESET_INTR_LATCH	 = 18
#0x0: Did not occur0x1: Occurred
BIT_RX_DTS_RCVD_SUCCESS_INTR_LATCH	 = 20
#0x0: Did not occur0x1: Occurred
BIT_RX_DTS_RCVD_END_TIMEOUT_INTR_LATCH	 = 21
#0x0: Did not occur0x1: Occurred
BIT_RX_DTS_RCVD_END_RESET_INTR_LATCH	 = 22
#0x0: Did not occur0x1: Occurred
BIT_RX_AUTH_END_INTR_LATCH	 = 23
#0x0: Did not occur0x1: Occurred
I2CREG_RX_STAT	 = 0x008C 	# Len = 4
BIT_RX_OVTP_STAT	 = 0
#0x0: Is not occuring0x1: Occurring
BIT_RX_OCP_STAT	 = 1
#0x0: Is not occuring0x1: Occurring
BIT_RX_OVP_STAT	 = 2
#0x0: Is not occuring0x1: Occurring
BIT_RX_SYS_ERR_STAT	 = 3
#0x0: Is not occuring0x1: Occurring
BIT_RX_EXT5V_TX_REMOVAL_STAT	 = 4
#0x0: Is not occuring0x1: Occurring
BIT_RX_RCVD_MSG_STAT	 = 5
#0x0: Is not occuring0x1: Occurring
BIT_RX_OUTPUT_ON_STAT	 = 6
#0x0: Is not occuring0x1: Occurring
BIT_RX_OUTPUT_OFF_STAT	 = 7
#0x0: Is not occuring0x1: Occurring
BIT_RX_SEND_PKT_SUCCESS_INTR_STAT	 = 8
#0x0: Is not occuring0x1: Occurring
BIT_RX_SEND_PKT_TIMEOUT_INTR_STAT	 = 9
#0x0: Is not occuring0x1: Occurring
BIT_RX_SIG_STR_STAT	 = 10
#0x0: Is not occuring0x1: Occurring
BIT_RX_VRECT_RDY_STAT	 = 11
#0x0: Is not occuring0x1: Occurring
BIT_RX_SCP_STAT	 = 12
#0x0: Is not occuring0x1: Occurring
BIT_RX_VOUT_LOW_STAT	 = 13
#0x0: Is not occuring0x1: Occurring
BIT_RX_DTS_SEND_SUCCESS_STAT	 = 16
#0x0: Is not occuring0x1: Occurring
BIT_RX_DTS_SEND_END_TIMEOUT_STAT	 = 17
#0x0: Is not occuring0x1: Occurring
BIT_RX_DTS_SEND_END_RESET_STAT	 = 18
#0x0: Is not occuring0x1: Occurring
BIT_RX_DTS_RCVD_SUCCESS_STAT	 = 20
#0x0: Is not occuring0x1: Occurring
BIT_RX_DTS_RCVD_END_TIMEOUT_STAT	 = 21
#0x0: Is not occuring0x1: Occurring
BIT_RX_DTS_RCVD_END_RESET_STAT	 = 22
#0x0: Is not occuring0x1: Occurring
BIT_RX_AUTH_END_STAT	 = 23
#0x0: Is not occuring0x1: Occurring
I2CREG_RX_CMD	 = 0x0090 	# Len = 2
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
I2CREG_RX_VRECT	 = 0x0092 	# Len = 2
I2CREG_RX_VOUT	 = 0x0094 	# Len = 2
I2CREG_RX_IIN	 = 0x0096 	# Len = 2
I2CREG_RX_CHIP_TEMP	 = 0x0098 	# Len = 2
I2CREG_RX_OP_FREQ	 = 0x009A 	# Len = 2
I2CREG_RX_NTC	 = 0x009C 	# Len = 2
I2CREG_RX_ADC_IN	 = 0x00A2 	# Len = 2
BIT_RX_ADC_IN3	 = 0
I2CREG_RX_RCVD_PWR	 = 0x00A4 	# Len = 2
I2CREG_QI_RP_VALUE	 = 0x00A6 	# Len = 2
BIT_RX_RP_VALUE	 = 0
I2CREG_RX_CTRL_ERR	 = 0x00A8 	# Len = 2
I2CREG_QI_CE_VALUE	 = 0x00AA 	# Len = 1
BIT_RX_CE_VALUE	 = 0
I2CREG_RX_SIGNAL_STRENGTH	 = 0x00AB 	# Len = 1
I2CREG_RX_PTC	 = 0x00AC 	# Len = 7
BIT_RX_GUA_PWR	 = 0
BIT_RX_FSK_DEPTH	 = 6
#0x0: -282~-249 / 30.25~63.250x1: -157~-124 / 61.5~94.50x2: -94.5~-61.5 / 124~1570x3: -63.25~-30.25 / 249~282
BIT_RX_RPR_HDR	 = 8
#0x31: RP24 format0x04: RP8 format
BIT_RX_PCH	 = 16
BIT_RX_REF_PWR	 = 24
BIT_RX_OB	 = 30
#0x0: not supported0x1: supported
BIT_RX_AI	 = 31
#0x0: not supported0x1: supported
BIT_RX_REPING_DELAY	 = 32
BIT_RX_FSK_POLARITY	 = 38
#0x0: Positive0x1: Negative
BIT_RX_NEG	 = 39
#0x0: BPP0x1: EPP
BIT_RX_WIN_OFFSET	 = 40
BIT_RX_WIN_SZ	 = 43
BIT_RX_DUP	 = 48
#0x0: not supported0x1: supported
BIT_RX_BUFF_SIZE	 = 49
#0x0: 16 bytes0x1: 32 bytes0x2: 64 bytes0x3: 128 bytes0x4: 256 bytes0x5: 512 bytes0x6: 1024 bytes0x7: 2048 bytes
BIT_RX_MINOR_VER	 = 52
I2CREG_RX_ILIM_SET	 = 0x00B3 	# Len = 1
I2CREG_RX_VOUT_SET	 = 0x00B4 	# Len = 2
I2CREG_RX_FOD_CUR_THRES	 = 0x00B6 	# Len = 5
BIT_RX_FOD_CUR_THRES1	 = 0
BIT_RX_FOD_CUR_THRES2	 = 8
BIT_RX_FOD_CUR_THRES3	 = 16
BIT_RX_FOD_CUR_THRES4	 = 24
BIT_RX_FOD_CUR_THRES5	 = 32
I2CREG_RX_FOD_GAIN	 = 0x00BB 	# Len = 6
BIT_RX_FOD_GAIN_OFFSET0	 = 0
BIT_RX_FOD_GAIN_OFFSET1	 = 8
BIT_RX_FOD_GAIN_OFFSET2	 = 16
BIT_RX_FOD_GAIN_OFFSET3	 = 24
BIT_RX_FOD_GAIN_OFFSET4	 = 32
BIT_RX_FOD_GAIN_OFFSET5	 = 40
I2CREG_RX_FOD_OFFSET	 = 0x00C1 	# Len = 6
BIT_RX_FOD_OFFSET0	 = 0
BIT_RX_FOD_OFFSET1	 = 8
BIT_RX_FOD_OFFSET2	 = 16
BIT_RX_FOD_OFFSET3	 = 24
BIT_RX_FOD_OFFSET4	 = 32
BIT_RX_FOD_OFFSET5	 = 40
I2CREG_RX_RSER	 = 0x00C7 	# Len = 1
I2CREG_RX_LDO_DROP	 = 0x00C8 	# Len = 4
BIT_RX_LDO_DROP0	 = 0
BIT_RX_LDO_DROP1	 = 8
BIT_RX_LDO_DROP2	 = 16
BIT_RX_LDO_DROP3	 = 24
I2CREG_RX_LDO_CUR_THRES	 = 0x00CC 	# Len = 3
BIT_RX_LDO_CUR_THRES1	 = 0
BIT_RX_LDO_CUR_THRES2	 = 8
BIT_RX_LDO_CUR_THRES3	 = 16
I2CREG_RX_EPT_MSG	 = 0x00CF 	# Len = 1
I2CREG_RX_RP_CTRL	 = 0x00D5 	# Len = 1
BIT_RP24_MAX_PWR	 = 0
BIT_RX_RP_FMT	 = 6
#0x0: No change0x1: RP8 (default)0x2: RP24 (No reply)0x3: RP24 (Req reply)
I2CREG_RX_DTS_SEND	 = 0x00D8 	# Len = 4
BIT_RX_DTS_ADC_SEND_LEN	 = 0
BIT_RX_DTS_ADC_SEND_REQUEST	 = 16
#0x00: ADC/end0x02: ADC/auth0x05: ADC/rst0x10: ADC/prop0x11: ADC/prop0x12: ADC/prop0x13: ADC/prop0x14: ADC/prop0x15: ADC/prop0x16: ADC/prop0x17: ADC/prop0x18: ADC/prop0x19: ADC/prop0x1a: ADC/prop0x1b: ADC/prop0x1c: ADC/prop0x1d: ADC/prop0x1e: ADC/prop0x1f: ADC/prop
I2CREG_RX_DTS_RCVD	 = 0x00DC 	# Len = 4
BIT_RX_DTS_ADC_RCVD_LEN	 = 0
BIT_RX_DTS_ADC_RCVD_REQUEST	 = 16
#0x00: ADC/end0x02: ADC/auth0x05: ADC/rst0x10: ADC/prop0x11: ADC/prop0x12: ADC/prop0x13: ADC/prop0x14: ADC/prop0x15: ADC/prop0x16: ADC/prop0x17: ADC/prop0x18: ADC/prop0x19: ADC/prop0x1a: ADC/prop0x1b: ADC/prop0x1c: ADC/prop0x1d: ADC/prop0x1e: ADC/prop0x1f: ADC/prop
I2CREG_ARC_AUTO_OFF_THRES	 = 0x00E0 	# Len = 2
I2CREG_SC_MAX_PWR	 = 0x00E2 	# Len = 1
BIT_SC_RP24_MAX_PWR	 = 0
I2CREG_MAX_PWR_SWICH	 = 0x00E3 	# Len = 1
BIT_MAX_PWR_SW	 = 0
#0x0: rp24 0x1: sc rp24
I2CREG_RX_EPP_FOD_CUR_THRES	 = 0x00E4 	# Len = 5
BIT_RX_EPP_FOD_CUR_THRES1	 = 0
BIT_RX_EPP_FOD_CUR_THRES2	 = 8
BIT_RX_EPP_FOD_CUR_THRES3	 = 16
BIT_RX_EPP_FOD_CUR_THRES4	 = 24
BIT_RX_EPP_FOD_CUR_THRES5	 = 32
I2CREG_RX_EPP_FOD_GAIN	 = 0x00E9 	# Len = 6
BIT_RX_EPP_FOD_GAIN_OFFSET0	 = 0
BIT_RX_EPP_FOD_GAIN_OFFSET1	 = 8
BIT_RX_EPP_FOD_GAIN_OFFSET2	 = 16
BIT_RX_EPP_FOD_GAIN_OFFSET3	 = 24
BIT_RX_EPP_FOD_GAIN_OFFSET4	 = 32
BIT_RX_EPP_FOD_GAIN_OFFSET5	 = 40
I2CREG_RX_EPP_FOD_OFFSET	 = 0x00EF 	# Len = 6
BIT_RX_EPP_FOD_OFFSET0	 = 0
BIT_RX_EPP_FOD_OFFSET1	 = 8
BIT_RX_EPP_FOD_OFFSET2	 = 16
BIT_RX_EPP_FOD_OFFSET3	 = 24
BIT_RX_EPP_FOD_OFFSET4	 = 32
BIT_RX_EPP_FOD_OFFSET5	 = 40
I2CREG_RX_EPP_RSER	 = 0x00F5 	# Len = 1
I2CREG_TX_INTR_EN	 = 0x0100 	# Len = 4
BIT_TX_OVTP_INTR_EN	 = 0
#0x0: Disabled0x1: Enabled
BIT_TX_OCP_INTR_EN	 = 1
#0x0: Disabled0x1: Enabled
BIT_TX_OVP_INTR_EN	 = 2
#0x0: Disabled0x1: Enabled
BIT_TX_SYS_ERR_INTR_EN	 = 3
#0x0: Disabled0x1: Enabled
BIT_TX_RP_PKT_RVCD_INTR_EN	 = 4
#0x0: Disabled0x1: Enabled
BIT_TX_CE_PKT_RVCD_INTR_EN	 = 5
#0x0: Disabled0x1: Enabled
BIT_TX_SEND_PKT_SUCCESS_INTR_EN	 = 6
#0x0: Disabled0x1: Enabled
BIT_TX_EXT_MON_INTR_EN	 = 7
#0x0: Disabled0x1: Enabled
BIT_TX_CEP_TO_INTR_EN	 = 8
#0x0: Disabled0x1: Enabled
BIT_TX_RPP_TO_INTR_EN	 = 9
#0x0: Disabled0x1: Enabled
BIT_TX_EPT_INTR_EN	 = 10
#0x0: Disabled0x1: Enabled
BIT_TX_START_PING_INTR_EN	 = 11
#0x0: Disabled0x1: Enabled
BIT_TX_SS_PKT_RCVD_INTR_EN	 = 12
#0x0: Disabled0x1: Enabled
BIT_TX_ID_PKT_RVCD_INTR_EN	 = 13
#0x0: Disabled0x1: Enabled
BIT_TX_CFG_PKT_RCVD_INTR_EN	 = 14
#0x0: Disabled0x1: Enabled
BIT_TX_PP_PKT_RCVD_INTR_EN	 = 15
#0x0: Disabled0x1: Enabled
BIT_TX_DTS_SEND_SUCCESS_INTR_EN	 = 16
#0x0: Disabled0x1: Enabled
BIT_TX_DTS_SEND_END_TIMEOUT_INTR_EN	 = 17
#0x0: Disabled0x1: Enabled
BIT_TX_DTS_SEND_END_RESET_INTR_EN	 = 18
#0x0: Disabled0x1: Enabled
BIT_TX_FOD_DET_INTR_EN	 = 19
#0x0: Disabled0x1: Enabled
BIT_TX_DTS_RCVD_SUCCESS_INTR_EN	 = 20
#0x0: Disabled0x1: Enabled
BIT_TX_DTS_RCVD_END_TIMEOUT_INTR_EN	 = 21
#0x0: Disabled0x1: Enabled
BIT_TX_DTS_RCVD_END_RESET_INTR_EN	 = 22
#0x0: Disabled0x1: Enabled
BIT_TX_PTC_UPDATE_INT_EN	 = 23
#0x0: Disabled0x1: Enabled
BIT_TX_BRIDGE_MD_INTR_EN	 = 24
#0x0: Disabled0x1: Enabled
I2CREG_TX_INTR_CLR	 = 0x0104 	# Len = 4
BIT_TX_OVTP_INTR_CLR	 = 0
#0x0: No change0x1: Will be cleared
BIT_TX_OCP_INTR_CLR	 = 1
#0x0: No change0x1: Will be cleared
BIT_TX_OVP_INTR_CLR	 = 2
#0x0: No change0x1: Will be cleared
BIT_TX_SYS_ERR_INTR_CLR	 = 3
#0x0: No change0x1: Will be cleared
BIT_TX_RP_PKT_RVCD_INTR_CLR	 = 4
#0x0: No change0x1: Will be cleared
BIT_TX_CE_PKT_RVCD_INTR_CLR	 = 5
#0x0: No change0x1: Will be cleared
BIT_TX_SEND_PKT_SUCCESS_INTR_CLR	 = 6
#0x0: No change0x1: Will be cleared
BIT_TX_EXT_MON_INTR_CLR	 = 7
#0x0: No change0x1: Will be cleared
BIT_TX_CEP_TO_INTR_CLR	 = 8
#0x0: No change0x1: Will be cleared
BIT_TX_RPP_TO_INTR_CLR	 = 9
#0x0: No change0x1: Will be cleared
BIT_TX_EPT_INTR_CLR	 = 10
#0x0: No change0x1: Will be cleared
BIT_TX_START_PING_INTR_CLR	 = 11
#0x0: No change0x1: Will be cleared
BIT_TX_SS_PKT_RCVD_INTR_CLR	 = 12
#0x0: No change0x1: Will be cleared
BIT_TX_ID_PKT_RVCD_INTR_CLR	 = 13
#0x0: No change0x1: Will be cleared
BIT_TX_CFG_PKT_RCVD_INTR_CLR	 = 14
#0x0: No change0x1: Will be cleared
BIT_TX_PP_PKT_RCVD_INTR_CLR	 = 15
#0x0: No change0x1: Will be cleared
BIT_TX_DTS_SEND_SUCCESS_INTR_CLR	 = 16
#0x0: No change0x1: Will be cleared
BIT_TX_DTS_SEND_END_TIMEOUT_INTR_CLR	 = 17
#0x0: No change0x1: Will be cleared
BIT_TX_DTS_SEND_END_RESET_INTR_CLR	 = 18
#0x0: No change0x1: Will be cleared
BIT_TX_FOD_DET_INTR_CLR	 = 19
#0x0: No change0x1: Will be cleared
BIT_TX_DTS_RCVD_SUCCESS_INTR_CLR	 = 20
#0x0: No change0x1: Will be cleared
BIT_TX_DTS_RCVD_END_TIMEOUT_INTR_CLR	 = 21
#0x0: No change0x1: Will be cleared
BIT_TX_DTS_RCVD_END_RESET_INTR_CLR	 = 22
#0x0: No change0x1: Will be cleared
BIT_TX_PTC_UPDATE_INT_CLR	 = 23
#0x0: No change0x1: Will be cleared
BIT_TX_BRIDGE_MD_INTR_CLR	 = 24
#0x0: No change0x1: Will be cleared
I2CREG_TX_INTR_LATCH	 = 0x0108 	# Len = 4
BIT_TX_OVTP_INTR_LATCH	 = 0
#0x0: Did not occur0x1: Occurred
BIT_TX_OCP_INTR_LATCH	 = 1
#0x0: Did not occur0x1: Occurred
BIT_TX_OVP_INTR_LATCH	 = 2
#0x0: Did not occur0x1: Occurred
BIT_TX_SYS_ERR_INTR_LATCH	 = 3
#0x0: Did not occur0x1: Occurred
BIT_TX_RP_PKT_RVCD_INTR_LATCH	 = 4
#0x0: Did not occur0x1: Occurred
BIT_TX_CE_PKT_RVCD_INTR_LATCH	 = 5
#0x0: Did not occur0x1: Occurred
BIT_TX_SEND_PKT_SUCCESS_INTR_LATCH	 = 6
#0x0: Did not occur0x1: Occurred
BIT_TX_EXT_MON_INTR_LATCH	 = 7
#0x0: Did not occur0x1: Occurred
BIT_TX_CEP_TO_INTR_LATCH	 = 8
#0x0: Did not occur0x1: Occurred
BIT_TX_RPP_TO_INTR_LATCH	 = 9
#0x0: Did not occur0x1: Occurred
BIT_TX_EPT_INTR_LATCH	 = 10
#0x0: Did not occur0x1: Occurred
BIT_TX_START_PING_INTR_LATCH	 = 11
#0x0: Did not occur0x1: Occurred
BIT_TX_SS_PKT_RCVD_INTR_LATCH	 = 12
#0x0: Did not occur0x1: Occurred
BIT_TX_ID_PKT_RVCD_INTR_LATCH	 = 13
#0x0: Did not occur0x1: Occurred
BIT_TX_CFG_PKT_RCVD_INTR_LATCH	 = 14
#0x0: Did not occur0x1: Occurred
BIT_TX_PP_PKT_RCVD_INTR_LATCH	 = 15
#0x0: Did not occur0x1: Occurred
BIT_TX_DTS_SEND_SUCCESS_INTR_LATCH	 = 16
#0x0: Did not occur0x1: Occurred
BIT_TX_DTS_SEND_END_TIMEOUT_INTR_LATCH	 = 17
#0x0: Did not occur0x1: Occurred
BIT_TX_DTS_SEND_END_RESET_INTR_LATCH	 = 18
#0x0: Did not occur0x1: Occurred
BIT_TX_FOD_DET_INTR_LATCH	 = 19
#0x0: Did not occur0x1: Occurred
BIT_TX_DTS_RCVD_SUCCESS_INTR_LATCH	 = 20
#0x0: Did not occur0x1: Occurred
BIT_TX_DTS_RCVD_END_TIMEOUT_INTR_LATCH	 = 21
#0x0: Did not occur0x1: Occurred
BIT_TX_DTS_RCVD_END_RESET_INTR_LATCH	 = 22
#0x0: Did not occur0x1: Occurred
BIT_TX_PTC_UPDATE_INT_LATCH	 = 23
#0x0: Did not occur0x1: Occurred
BIT_TX_BRIDGE_MD_INTR_LATCH	 = 24
#0x0: Did not occur0x1: Occurred
I2CREG_TX_STAT	 = 0x010C 	# Len = 4
BIT_TX_OVTP_STAT	 = 0
#0x0: Is not occuring0x1: Occurring
BIT_TX_OCP_STAT	 = 1
#0x0: Is not occuring0x1: Occurring
BIT_TX_OVP_STAT	 = 2
#0x0: Is not occuring0x1: Occurring
BIT_TX_SYS_ERR_STAT	 = 3
#0x0: Is not occuring0x1: Occurring
BIT_TX_RP_PKT_RVCD_STAT	 = 4
#0x0: Is not occuring0x1: Occurring
BIT_TX_CE_PKT_RVCD_STAT	 = 5
#0x0: Is not occuring0x1: Occurring
BIT_TX_SEND_PKT_SUCCESS_STAT	 = 6
#0x0: Is not occuring0x1: Occurring
BIT_TX_EXT_MON_INTR_STAT	 = 7
#0x0: Is not occuring0x1: Occurring
BIT_TX_CEP_TO_INTR_STAT	 = 8
#0x0: Is not occuring0x1: Occurring
BIT_TX_RPP_TO_INTR_STAT	 = 9
#0x0: Is not occuring0x1: Occurring
BIT_TX_EPT_STAT	 = 10
#0x0: Is not occuring0x1: Occurring
BIT_TX_START_PING_STAT	 = 11
#0x0: Is not occuring0x1: Occurring
BIT_TX_SS_PKT_RCVD_STAT	 = 12
#0x0: Is not occuring0x1: Occurring
BIT_TX_ID_PKT_RVCD_STAT	 = 13
#0x0: Is not occuring0x1: Occurring
BIT_TX_CFG_PKT_RCVD_STAT	 = 14
#0x0: Is not occuring0x1: Occurring
BIT_TX_PP_PKT_RCVD_STAT	 = 15
#0x0: Is not occuring0x1: Occurring
BIT_TX_DTS_SEND_SUCCESS_STAT	 = 16
#0x0: Is not occuring0x1: Occurring
BIT_TX_DTS_SEND_END_TIMEOUT_STAT	 = 17
#0x0: Is not occuring0x1: Occurring
BIT_TX_DTS_SEND_END_RESET_STAT	 = 18
#0x0: Is not occuring0x1: Occurring
BIT_TX_FOD_DET_INTR_STAT	 = 19
#0x0: Is not occuring0x1: Occurring
BIT_TX_DTS_RCVD_SUCCESS_STAT	 = 20
#0x0: Is not occuring0x1: Occurring
BIT_TX_DTS_RCVD_END_TIMEOUT_STAT	 = 21
#0x0: Is not occuring0x1: Occurring
BIT_TX_DTS_RCVD_END_RESET_STAT	 = 22
#0x0: Is not occuring0x1: Occurring
BIT_TX_PTC_UPDATE_INT_STAT	 = 23
#0x0: Is not occuring0x1: Occurring
BIT_TX_BRIDGE_MD_INTR_STAT	 = 24
#0x0: Is not occuring0x1: Occurring
I2CREG_TX_CMD	 = 0x0110 	# Len = 2
BIT_TX_EN	 = 0
#0x0: Do nothing0x1: Perform action
BIT_TX_DIS	 = 1
#0x0: Do nothing0x1: Perform action
BIT_TX_SEND_MSG	 = 2
#0x0: Do nothing0x1: Perform action
BIT_TX_MEAS_Q	 = 3
#0x0: Do nothing0x1: Perform action
BIT_TX_SEND_DTS	 = 4
#0x0: Do nothing0x1: Perform action
I2CREG_TX_EPT_REASON_RCVD	 = 0x0112 	# Len = 3
BIT_TX_EPT_SRC_OVP	 = 0
#0x0: Did not appear0x1: Appeared
BIT_TX_EPT_SRC_OCP	 = 1
#0x0: Did not appear0x1: Appeared
BIT_TX_EPT_SRC_OVTP	 = 2
#0x0: Did not appear0x1: Appeared
BIT_TX_EPT_SRC_FOD	 = 3
#0x0: Did not appear0x1: Appeared
BIT_TX_EPT_SRC_CMD	 = 4
#0x0: Did not appear0x1: Appeared
BIT_TX_EPT_SRC_RX	 = 5
#0x0: Did not appear0x1: Appeared
BIT_TX_EPT_SRC_CEP_TO	 = 6
#0x0: Did not appear0x1: Appeared
BIT_TX_EPT_SRC_RPP_TO	 = 7
#0x0: Did not appear0x1: Appeared
BIT_TX_EPT_SRC_RX_RST	 = 8
#0x0: Did not appear0x1: Appeared
BIT_TX_EPT_SRC_SYS_ERR	 = 9
#0x0: Did not appear0x1: Appeared
BIT_TX_EPT_SRC_SS_TO	 = 10
#0x0: Did not appear0x1: Appeared
BIT_TX_EPT_SRC_SS	 = 11
#0x0: Did not appear0x1: Appeared
BIT_TX_EPT_SRC_ID	 = 12
#0x0: Did not appear0x1: Appeared
BIT_TX_EPT_SRC_CFG	 = 13
#0x0: Did not appear0x1: Appeared
BIT_TX_EPT_SRC_CFG_CNT_ERR	 = 14
#0x0: Did not appear0x1: Appeared
BIT_TX_EPT_SRC_PCH	 = 15
#0x0: Did not appear0x1: Appeared
BIT_TX_EPT_SRC_XID	 = 16
#0x0: Did not appear0x1: Appeared
BIT_TX_EPT_SRC_NEGO	 = 17
#0x0: Did not appear0x1: Appeared
BIT_TX_EPT_SRC_NEGO_TO	 = 18
#0x0: Did not appear0x1: Appeared
I2CREG_TX_RECENT_CEP	 = 0x0115 	# Len = 1
I2CREG_TX_VRECT	 = 0x0116 	# Len = 2
I2CREG_TX_VIN	 = 0x0118 	# Len = 2
I2CREG_TX_IOUT	 = 0x011A 	# Len = 2
I2CREG_TX_CHIP_TEMP	 = 0x011C 	# Len = 2
I2CREG_TX_OP_FREQ	 = 0x011E 	# Len = 2
I2CREG_TX_NTC	 = 0x0120 	# Len = 2
I2CREG_TX_DFT	 = 0x0122 	# Len = 4
BIT_TX_DFT1	 = 0
#ADC DFT1 ADC code
BIT_TX_DFT2	 = 16
#ADC DFT2 ADC code
I2CREG_TX_ADC_IN	 = 0x0126 	# Len = 2
BIT_TX_ADC_IN3	 = 0
#ADC IN3 ADC code
I2CREG_TX_PWR_TFRD_TO_RX	 = 0x0128 	# Len = 2
I2CREG_TX_PWR_RCVD_BY_RX	 = 0x012A 	# Len = 2
I2CREG_TX_OP_DC	 = 0x012C 	# Len = 1
I2CREG_TX_PTC	 = 0x012D 	# Len = 7
BIT_TX_GUA_PWR	 = 0
BIT_TX_FSK_DEPTH	 = 6
#0x0: -282~-249 / 30.25~63.250x1: -157~-124 / 61.5~94.50x2: -94.5~-61.5 / 124~1570x3: -63.25~-30.25 / 249~282
BIT_TX_RPR_HDR	 = 8
#0x31: RP24 format0x04: RP8 format
BIT_TX_PCH	 = 16
BIT_TX_REF_PWR	 = 24
BIT_TX_OB	 = 30
#0x0: not supported0x1: supported
BIT_TX_AI	 = 31
#0x0: not supported0x1: supported
BIT_TX_REPING_DELAY	 = 32
BIT_TX_FSK_POLARITY	 = 38
#0x0: Positive0x1: Negative
BIT_TX_NEG	 = 39
#0x0: BPP0x1: EPP
BIT_TX_WIN_OFFSET	 = 40
BIT_TX_WIN_SZ	 = 43
BIT_TX_DUP	 = 48
#0x0: not supported0x1: supported
BIT_TX_BUFF_SIZE	 = 49
#0x0: 16 bytes0x1: 32 bytes0x2: 64 bytes0x3: 128 bytes0x4: 256 bytes0x5: 512 bytes0x6: 1024 bytes0x7: 2048 bytes
BIT_TX_MINOR_VER	 = 52
I2CREG_TX_CTRL	 = 0x0134 	# Len = 1
BIT_TX_BRIDGE_MD	 = 0
#0x0: No change (same as ping)0x1: Manual half bridge mode0x2: Manual full bridge mode0x3: Auto switch
BIT_TX_PING_HALF_BRIDGE	 = 2
#0x0:Disable (Full bridge)0x1:Enable (Half bridge)
I2CREG_TX_BRIDGE_MODE_CUR_THRES	 = 0x0135 	# Len = 1
I2CREG_TX_BRIDGE_STAT	 = 0x0136 	# Len = 1
BIT_TX_HALF_BRIDGE_STAT	 = 0
#0x0: Full bridge0x1: Half bridge
I2CREG_TX_OVP_THRES	 = 0x0140 	# Len = 1
I2CREG_TX_OCP_THRES	 = 0x0141 	# Len = 1
I2CREG_TX_OVTP_THRES	 = 0x0142 	# Len = 1
I2CREG_TX_PID_MAX_CUR	 = 0x0143 	# Len = 1
I2CREG_TX_MAX_FREQ	 = 0x0144 	# Len = 1
I2CREG_TX_MIN_FREQ	 = 0x0145 	# Len = 1
I2CREG_TX_PING_FREQ	 = 0x0146 	# Len = 1
I2CREG_TX_PING_INTERVAL	 = 0x0147 	# Len = 1
I2CREG_TX_MAX_DC	 = 0x0148 	# Len = 1
I2CREG_TX_MIN_DC	 = 0x0149 	# Len = 1
I2CREG_TX_FOD_PLOSS_THRES	 = 0x014A 	# Len = 1
I2CREG_TX_FOD_DBNC_CNT	 = 0x014B 	# Len = 1
I2CREG_TX_CE_TO_MAX_CNT	 = 0x014C 	# Len = 1
I2CREG_TX_FHOP_STEP	 = 0x014D 	# Len = 1
I2CREG_TX_PING_DC	 = 0x014E 	# Len = 1
I2CREG_TX_DTS_SEND	 = 0x0150 	# Len = 4
BIT_TX_DTS_ADC_SEND_LEN	 = 0
BIT_TX_DTS_ADC_SEND_REQUEST	 = 16
#0x00: ADC/end0x02: ADC/auth0x05: ADC/rst0x10: ADC/prop0x11: ADC/prop0x12: ADC/prop0x13: ADC/prop0x14: ADC/prop0x15: ADC/prop0x16: ADC/prop0x17: ADC/prop0x18: ADC/prop0x19: ADC/prop0x1a: ADC/prop0x1b: ADC/prop0x1c: ADC/prop0x1d: ADC/prop0x1e: ADC/prop0x1f: ADC/prop
I2CREG_TX_DTS_RCVD	 = 0x0154 	# Len = 4
BIT_TX_DTS_ADC_RCVD_LEN	 = 0
BIT_TX_DTS_ADC_RCVD_REQUEST	 = 16
#0x00: ADC/end0x02: ADC/auth0x05: ADC/rst0x10: ADC/prop0x11: ADC/prop0x12: ADC/prop0x13: ADC/prop0x14: ADC/prop0x15: ADC/prop0x16: ADC/prop0x17: ADC/prop0x18: ADC/prop0x19: ADC/prop0x1a: ADC/prop0x1b: ADC/prop0x1c: ADC/prop0x1d: ADC/prop0x1e: ADC/prop0x1f: ADC/prop
I2CREG_Q_EXCITE_FREQ	 = 0x015A 	# Len = 1
I2CREG_Q_MEAS_RESONANT_FREQ	 = 0x015C 	# Len = 2
I2CREG_Q_MEAS_QFACTOR	 = 0x015E 	# Len = 2
I2CREG_Q_MEAS_ADC	 = 0x0160 	# Len = 2
I2CREG_AUX_DATA	 = 0x0180
I2CREG_SEND_MSG	 = 0x0180
I2CREG_RCVD_MSG  = 0x0190
DTS_SEND_MSG_000        = 0X0200
DTS_RCVD_MSG_000        = 0x0280
#HW reg address
HWREG_GPIO_INPUT_VAL_RegAddr = 0x2001A01C
