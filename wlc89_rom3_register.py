"""
  ******************************************************************************
  * Copyright c 2024, STMicroelectronics - All Rights Reserved
  * Authors: ACD Analog Custom Devices Software Team for STMicroelectronics.
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
  * DAMAGES INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
  * SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION HOWEVER
  * CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
  * OR TORT INCLUDING NEGLIGENCE OR OTHERWISE ARISING IN ANY WAY OUT OF THE USE
  * OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
  *
  ******************************************************************************
"""
#WLC89 ROM3
I2CREG_CHIP_ID	 = 0x0000 	# Len = 2
I2CREG_CHIP_REV	 = 0x0002 	# Len = 1
I2CREG_CUST_ID	 = 0x0003 	# Len = 1
I2CREG_NVM_PATCH_ID	 = 0x0004 	# Len = 2
I2CREG_CFG_ID	 = 0x0006 	# Len = 2
I2CREG_PRMC_ID	 = 0x000A 	# Len = 2
BIT_PRMC_ID_L	 = 0
#Manufacturer ID low byte
BIT_PRMC_ID_H	 = 8
#Manufacturer ID high byte
I2CREG_RX_ID	 = 0x0010 	# Len = 6
I2CREG_INTR_STAT	 = 0x0018 	# Len = 4
BIT_DTS_ERR_STAT	 = 0
#Live status of corresponding interrupt
BIT_TX_EXT_MON_STAT	 = 1
#Live status of corresponding interrupt
BIT_OVTP_STAT	 = 2
#Live status of corresponding interrupt
BIT_OCP_STAT	 = 3
#Live status of corresponding interrupt
BIT_OVP_STAT	 = 4
#Live status of corresponding interrupt
BIT_OP_MODE_STAT	 = 5
#Live status of corresponding interrupt
BIT_VRECT_STAT	 = 6
#Live status of corresponding interrupt
BIT_RX_OUTPUT_STAT	 = 7
#Live status of corresponding interrupt
BIT_DTS_SEND_SUCCESS_STAT	 = 8
#Live status of corresponding interrupt
BIT_DTS_RCVD_SUCCESS_STAT	 = 9
#Live status of corresponding interrupt
BIT_AC_MISG_STAT	 = 10
#Live status of corresponding interrupt
BIT_TX_CONNECTION_STAT	 = 11
#Live status of corresponding interrupt
BIT_TX_FOD_DET_STAT	 = 12
#Live status of corresponding interrupt
BIT_TX_NO_SS_PKT_STAT	 = 13
#Live status of corresponding interrupt
BIT_TX_OCP_STAT	 = 14
#Live status of corresponding interrupt
BIT_RCVD_MSG_STAT	 = 15
#Live status of corresponding interrupt
BIT_RX_MPP_SUPPORTED_BY_TX_STAT	 = 16
#Live status of corresponding interrupt
BIT_RX_EPP_SUPPORTED_BY_TX_STAT	 = 17
#Live status of corresponding interrupt
BIT_RX_MPP_NEGO_360KHZ_PASS_STAT	 = 18
#Live status of corresponding interrupt
BIT_RX_MPP_INCR_PWR_STAT	 = 19
#Live status of corresponding interrupt
BIT_RX_MPP_DECR_PWR_STAT	 = 20
#Live status of corresponding interrupt
BIT_RX_EXIT_CLOAK_DONE_STAT	 = 21
#Live status of corresponding interrupt
BIT_RX_EPP_NEGO_PASS_STAT	 = 22
#Live status of corresponding interrupt
BIT_RX_EPP_NEG_FAIL_STAT	 = 23
#Live status of corresponding interrupt
BIT_SYS_ERR_STAT	 = 31
#Live status of corresponding interrupt
I2CREG_INTR_LATCH	 = 0x001C 	# Len = 4
BIT_DTS_ERR_INTR_LATCH	 = 0
#Interrupt pending latch status0: No pending interrupt1: Pending interruptSee xxx_intr_clr register for details.
BIT_TX_EXT_MON_INTR_LATCH	 = 1
#Interrupt pending latch status0: No pending interrupt1: Pending interruptSee xxx_intr_clr register for details.
BIT_OVTP_INTR_LATCH	 = 2
#Interrupt pending latch status0: No pending interrupt1: Pending interruptSee xxx_intr_clr register for details.
BIT_OCP_INTR_LATCH	 = 3
#Interrupt pending latch status0: No pending interrupt1: Pending interruptSee xxx_intr_clr register for details.
BIT_OVP_INTR_LATCH	 = 4
#Interrupt pending latch status0: No pending interrupt1: Pending interruptSee xxx_intr_clr register for details.
BIT_OP_MODE_INTR_LATCH	 = 5
#Interrupt pending latch status0: No pending interrupt1: Pending interruptSee xxx_intr_clr register for details.
BIT_VRECT_INTR_LATCH	 = 6
#Interrupt pending latch status0: No pending interrupt1: Pending interruptSee xxx_intr_clr register for details.
BIT_RX_OUTPUT_INTR_LATCH	 = 7
#Interrupt pending latch status0: No pending interrupt1: Pending interruptSee xxx_intr_clr register for details.
BIT_DTS_SEND_SUCCESS_INTR_LATCH	 = 8
#Interrupt pending latch status0: No pending interrupt1: Pending interruptSee xxx_intr_clr register for details.
BIT_DTS_RCVD_SUCCESS_INTR_LATCH	 = 9
#Interrupt pending latch status0: No pending interrupt1: Pending interruptSee xxx_intr_clr register for details.
BIT_AC_MISG_INTR_LATCH	 = 10
#Interrupt pending latch status0: No pending interrupt1: Pending interruptSee xxx_intr_clr register for details.
BIT_TX_CONNECTION_INTR_LATCH	 = 11
#Interrupt pending latch status0: No pending interrupt1: Pending interruptSee xxx_intr_clr register for details.
BIT_TX_FOD_DET_INTR_LATCH	 = 12
#Interrupt pending latch status0: No pending interrupt1: Pending interruptSee xxx_intr_clr register for details.
BIT_TX_NO_SS_PKT_INTR_LATCH	 = 13
#Interrupt pending latch status0: No pending interrupt1: Pending interruptSee xxx_intr_clr register for details.
BIT_TX_OCP_INTR_LATCH	 = 14
#Interrupt pending latch status0: No pending interrupt1: Pending interruptSee xxx_intr_clr register for details.
BIT_RCVD_MSG_INTR_LATCH	 = 15
#Interrupt pending latch status0: No pending interrupt1: Pending interruptSee xxx_intr_clr register for details.
BIT_RX_MPP_SUPPORTED_BY_TX_INTR_LATCH	 = 16
#Interrupt pending latch status0: No pending interrupt1: Pending interruptSee xxx_intr_clr register for details.
BIT_RX_EPP_SUPPORTED_BY_TX_INTR_LATCH	 = 17
#Interrupt pending latch status0: No pending interrupt1: Pending interruptSee xxx_intr_clr register for details.
BIT_RX_MPP_NEGO_360KHZ_PASS_INTR_LATCH	 = 18
#Interrupt pending latch status0: No pending interrupt1: Pending interruptSee xxx_intr_clr register for details.
BIT_RX_MPP_INCR_PWR_INTR_LATCH	 = 19
#Interrupt pending latch status0: No pending interrupt1: Pending interruptSee xxx_intr_clr register for details.
BIT_RX_MPP_DECR_PWR_INTR_LATCH	 = 20
#Interrupt pending latch status0: No pending interrupt1: Pending interruptSee xxx_intr_clr register for details.
BIT_RX_EXIT_CLOAK_DONE_INTR_LATCH	 = 21
#Interrupt pending latch status0: No pending interrupt1: Pending interruptSee xxx_intr_clr register for details.
BIT_RX_EPP_NEGO_PASS_INTR_LATCH	 = 22
#Interrupt pending latch status0: No pending interrupt1: Pending interruptSee xxx_intr_clr register for details.
BIT_RX_EPP_NEG_FAIL_INTR_LATCH	 = 23
#Interrupt pending latch status0: No pending interrupt1: Pending interruptSee xxx_intr_clr register for details.
BIT_SYS_ERR_INTR_LATCH	 = 31
#Interrupt pending latch status0: No pending interrupt1: Pending interruptSee xxx_intr_clr register for details.
I2CREG_INTR_EN	 = 0x0020 	# Len = 4
BIT_DTS_ERR_INTR_EN	 = 0
#DTS error interrupt enable0: Disable1: Enable
BIT_TX_EXT_MON_INTR_EN	 = 1
#Ext Tx Detect interrupt enable0: Disable1: Enable
BIT_OVTP_INTR_EN	 = 2
#Over temperature protection interrupt enable0: Disable1: Enable
BIT_OCP_INTR_EN	 = 3
#Over current protection interrupt enable0: Disable1: Enable
BIT_OVP_INTR_EN	 = 4
#Over voltage protection interrupt enable0: Disable1: Enable
BIT_OP_MODE_INTR_EN	 = 5
#Operation mode changed interrupt enable0: Disable1: Enable
BIT_VRECT_INTR_EN	 = 6
#Vrect level is higher than target Vrect level interrupt enable0: Disable1: Enable
BIT_RX_OUTPUT_INTR_EN	 = 7
#Rx Output on interrupt enable0: Disable1: Enable
BIT_DTS_SEND_SUCCESS_INTR_EN	 = 8
#DTS sending data stream successfully interrupt enable0: Disable1: Enable
BIT_DTS_RCVD_SUCCESS_INTR_EN	 = 9
#DTS receiving data stream successfully interrupt enable0: Disable1: Enable
BIT_AC_MISG_INTR_EN	 = 10
#AC missing interrupt enabled0: Disable1: Enable
BIT_TX_CONNECTION_INTR_EN	 = 11
#SS or EPT packet received interrupt enable0: Disable1: Enable
BIT_TX_FOD_DET_INTR_EN	 = 12
#Tx FOD detect interrupt enable0: Disable1: Enable
BIT_TX_NO_SS_PKT_INTR_EN	 = 13
#No SS packet received interrupt enable0: Disable1: Enable
BIT_TX_OCP_INTR_EN	 = 14
#Icurr is higher than Iuno interrupt enabled0: Disable1: Enable
BIT_RCVD_MSG_INTR_EN	 = 15
#Message received interrupt enabled0: Disable1: Enable
BIT_RX_MPP_SUPPORTED_BY_TX_INTR_EN	 = 16
#Rx received MPP-ack from MPP Tx interrupt enable0: Disable1: Enable
BIT_RX_EPP_SUPPORTED_BY_TX_INTR_EN	 = 17
#Rx received ack from EPP Tx interrupt enable0: Disable1: Enable
BIT_RX_MPP_NEGO_360KHZ_PASS_INTR_EN	 = 18
#Rx pass 360kHz nego interrupt enable0: Disable1: Enable
BIT_RX_MPP_INCR_PWR_INTR_EN	 = 19
#Rx MPLA received ack interrupt enable0: Disable1: Enable
BIT_RX_MPP_DECR_PWR_INTR_EN	 = 20
#Rx MPLA received NAK interrupt enable0: Disable1: Enable
BIT_RX_EXIT_CLOAK_DONE_INTR_EN	 = 21
#Rx exit cloak done interrupt enable0: Disable1: Enable
BIT_RX_EPP_NEGO_PASS_INTR_EN	 = 22
#Rx pass EPP nego interrupt enable0: Disable1: Enable
BIT_RX_EPP_NEG_FAIL_INTR_EN	 = 23
#Rx fail EPP nego interrupt enable0: Disable1: Enable
BIT_SYS_ERR_INTR_EN	 = 31
#System error interrupt enable0: Disable1: Enable
I2CREG_INTR_CLR	 = 0x0024 	# Len = 4
BIT_DTS_ERR_INTR_CLR	 = 0
#Write 1 to clear corresponding interrupt latch (xxx_int_latch)
BIT_TX_EXT_MON_INTR_CLR	 = 1
#Write 1 to clear corresponding interrupt latch (xxx_int_latch)
BIT_OVTP_INTR_CLR	 = 2
#Write 1 to clear corresponding interrupt latch (xxx_int_latch)
BIT_OCP_INTR_CLR	 = 3
#Write 1 to clear corresponding interrupt latch (xxx_int_latch)
BIT_OVP_INTR_CLR	 = 4
#Write 1 to clear corresponding interrupt latch (xxx_int_latch)
BIT_OP_MODE_INTR_CLR	 = 5
#Write 1 to clear corresponding interrupt latch (xxx_int_latch)
BIT_VRECT_INTR_CLR	 = 6
#Write 1 to clear corresponding interrupt latch (xxx_int_latch)
BIT_RX_OUTPUT_INTR_CLR	 = 7
#Write 1 to clear corresponding interrupt latch (xxx_int_latch)
BIT_DTS_SEND_SUCCESS_INTR_CLR	 = 8
#Write 1 to clear corresponding interrupt latch (xxx_int_latch)
BIT_DTS_RCVD_SUCCESS_INTR_CLR	 = 9
#Write 1 to clear corresponding interrupt latch (xxx_int_latch)
BIT_AC_MISG_INTR_CLR	 = 10
#Write 1 to clear corresponding interrupt latch (xxx_int_latch)
BIT_TX_CONNECTION_INTR_CLR	 = 11
#Write 1 to clear corresponding interrupt latch (xxx_int_latch)
BIT_TX_FOD_DET_INTR_CLR	 = 12
#Write 1 to clear corresponding interrupt latch (xxx_int_latch)
BIT_TX_NO_SS_PTK_INTR_CLR	 = 13
#Write 1 to clear corresponding interrupt latch (xxx_int_latch)
BIT_TX_OCP_INTR_CLR	 = 14
#Write 1 to clear corresponding interrupt latch (xxx_int_latch)
BIT_RCVD_MSG_INTR_CLR	 = 15
#Write 1 to clear corresponding interrupt latch (xxx_int_latch)
BIT_RX_MPP_SUPPORTED_BY_TX_INTR_CLR	 = 16
#Write 1 to clear corresponding interrupt latch (xxx_int_latch)
BIT_RX_EPP_SUPPORTED_BY_TX_INTR_CLR	 = 17
#Write 1 to clear corresponding interrupt latch (xxx_int_latch)
BIT_RX_MPP_NEGO_360KHZ_PASS_INTR_CLR	 = 18
#Write 1 to clear corresponding interrupt latch (xxx_int_latch)
BIT_RX_MPP_INCR_PWR_INTR_CLR	 = 19
#Write 1 to clear corresponding interrupt latch (xxx_int_latch)
BIT_RX_MPP_DECR_PWR_INTR_CLR	 = 20
#Write 1 to clear corresponding interrupt latch (xxx_int_latch)
BIT_RX_EXIT_CLOAK_DONE_INTR_CLR	 = 21
#Write 1 to clear corresponding interrupt latch (xxx_int_latch)
BIT_RX_EPP_NEGO_PASS_INTR_CLR	 = 22
#Write 1 to clear corresponding interrupt latch (xxx_int_latch)
BIT_RX_EPP_NEG_FAIL_INTR_CLR	 = 23
#Write 1 to clear corresponding interrupt latch (xxx_int_latch)
BIT_SYS_ERR_INTR_CLR	 = 31
#Write 1 to clear corresponding interrupt latch (xxx_intr_latch)
I2CREG_RXOP_MODE	 = 0x002B 	# Len = 1
BIT_TX_OP_MODE	 = 0
#Tx operation mode0-Back power missing4-MST ON(Passive)5-MST ON(Active)8-Tx Mode9-Tx FOD/Conflict10-Tx PHM
BIT_RX_OP_MODE	 = 5
#Rx Operation mode0-AC Missing1-BPP2-EPP3-MPP,  Restricted4-MPP,  Full5-MPP, Cloak6-MPP, Nego (360kHz)7-EPP, Nego

I2CREG_RX_VRECT_ADJ	 = 0x0039 	# Len = 1
I2CREG_RX_CHS	 = 0x003A 	# Len = 1
BIT_RX_CHS_MSG	 = 0
#Charge status message
I2CREG_RX_EPT	 = 0x003B 	# Len = 1
BIT_RX_EPT_MSG	 = 0
#EPT status message
I2CREG_VOUT_MEAS	 = 0x003C 	# Len = 2
I2CREG_RX_VOUT_SET	 = 0x003E 	# Len = 2
BIT_VOUT_SET	 = 0
#Program VOUT output voltage3.5V to 21V, in 20mV steps0 - Invalid1 - 3460mV2 - 3480mV3 - 3500mV¡­878 - 21V879 - Invalid¡­65535 - Invalid
I2CREG_VRECT_MEAS	 = 0x0040 	# Len = 2
I2CREG_ICUR_MEAS	 = 0x0044 	# Len = 2
I2CREG_CHIP_TEMP_MEAS	 = 0x0046 	# Len = 2
I2CREG_OP_FREQ	 = 0x0048 	# Len = 2
I2CREG_RX_PING_FREQ	 = 0x004A 	# Len = 2
I2CREG_ILIM_SET	 = 0x004C 	# Len = 1
I2CREG_CMD	 = 0x004E 	# Len = 2
BIT_SEND_MSG	 = 0
#Rx/Tx send msg data
BIT_LDO_TOGGLE	 = 1
#To turn on and turn off main LDO
BIT_SYS_RST	 = 2
#System reset
BIT_RX_SEND_EPT	 = 3
#Send EPT msg
BIT_RX_SEND_CHS	 = 4
#Send CHS msg
BIT_CLR_INTR	 = 5
#Clear all interrupts
BIT_PHM_TOGGLE	 = 7
#1 - PHM mode supported0 - PHM mode not supported
BIT_DTS_SEND	 = 1
#Sent DTS data
BIT_MPP_FULL	 = 2
#Transition from MPP restricted mode to MPP full mode
BIT_MPP_ENTER_CLOAK	 = 3
#Enter MPP cloak
BIT_MPP_EXIT_CLOAK	 = 4
#Exit MPP cloak
I2CREG_SEND_MSG_HDR	 = 0x0050 	# Len = 1
I2CREG_SEND_MSG_CMD	 = 0x0051 	# Len = 1
I2CREG_SEND_MSG	 = 0x0052 	# Len = 7
I2CREG_SEND_MSG_END	 = 0x0059 	# Len = 1

I2CREG_CLOAK_REASON	 = 0x005A 	# Len = 1
I2CREG_EXIT_CLOAK_REASON	 = 0x005B 	# Len = 1
I2CREG_DTS_PKT_TO	 = 0x005C 	# Len = 1
I2CREG_DTS_STM_TO	 = 0x005D 	# Len = 1
I2CREG_PRE_OVP_DUMMY_LD	 = 0x005E 	# Len = 1

I2CREG_RX_OVP_CTRL	 = 0x006A 	# Len = 1
BIT_RX_OVPS2_SEL	 = 0
#To select the threshold for OVPS20 - 25V1 - 24V2 - 22V3 - 20V4 - 17V5 - 15V6 - 13V7 - 11V
BIT_RX_PRE_OVP_SEL	 = 3
#pre-OVP threshold level selection = Vout voltage + {(ovps2 voltage - Vout) * __%}000: disabled001: 90%010: 80%011: 70%100: 60%101: 50%110: 40%111: 30%
BIT_RX_OVPH_SEL	 = 6
#To select the threshold for OVPH0 - 26.5V1 - 26V2 - 25.5V3 - 25V

I2CREG_FOD_PARAM_START	 = 0x0070 	# Len = 1
BIT_FOD_CUR_THRES1_10MA	 = 0
#FOD current threshold, in 10mA
I2CREG_FOD_PARAM_U8	 = 0x0071 	# Len = 7
BIT_FOD_CUR_THRES2_10MA	 = 0
BIT_FOD_CUR_THRES3_10MA	 = 8
BIT_FOD_CUR_THRES4_10MA	 = 16
BIT_FOD_CUR_THRES5_10MA	 = 24
BIT_FOD_CUR_THRES6_10MA	 = 32
BIT_FOD_CUR_THRES7_10MA	 = 40
BIT_FOD_CUR_THRES8_10MA	 = 48
I2CREG_FOD_PARAM_S8	 = 0x0078 	# Len = 9
BIT_FOD_OFFSET0	 = 0
#Signed FOD offset in units of 32mW.0 - 0mW1 - 32mW¡­127 - 4064mW-1 - -32mW¡­-128 - 4096mW
BIT_FOD_OFFSET1	 = 8
BIT_FOD_OFFSET2	 = 16
BIT_FOD_OFFSET3	 = 24
BIT_FOD_OFFSET4	 = 32
BIT_FOD_OFFSET5	 = 40
BIT_FOD_OFFSET6	 = 48
BIT_FOD_OFFSET7	 = 56
BIT_FOD_OFFSET8	 = 64
I2CREG_FOD_PARAM2_U8	 = 0x0081 	# Len = 2
BIT_FOD_GAIN_OFFSET	 = 0
#FOD Gain scaler offset for DC power (V * *) base is 512, default scaler is 512. Specify this value as signed (2'complement) offset.0 - 512/5121 - 513/512¡­127 - 639/512-128 - 384/512¡­-1 - 511/512
BIT_RCOIL_4MOHM	 = 8
#Coil series resistance, specified in units of 4mOhm
I2CREG_FOD_PARAM_END	 = 0x0083 	# Len = 1
BIT_FOD_PARAM_RESERVED	 = 0
I2CREG_FOD_PARAM_MODE	 = 0x0084 	# Len = 1
I2CREG_DTS_ERR_CODE	 = 0x008D 	# Len = 1
BIT_DTS_MISC_FLT	 = 0
#DTS misc faults
BIT_DTS_BUSY	 = 1
#DTS is busy
BIT_DTS_PKT_TO	 = 2
#DTS packet timeout
BIT_DTS_STM_TO	 = 3
#DTS stream timeout
BIT_DTS_OF	 = 4
#DTS overflow fault
BIT_DTS_TX_RST_OR_ABORT	 = 5
#DTS Tx reset or abort:0: reset1: abort
I2CREG_TX_MFR_ID_L	 = 0x009C 	# Len = 1
I2CREG_TX_MFR_ID_H	 = 0x009D 	# Len = 1
I2CREG_PR_MAX	 = 0x00A0 	# Len = 1
I2CREG_FOD_QF	 = 0x00A1 	# Len = 1
I2CREG_FOD_RF	 = 0x00A2 	# Len = 1
I2CREG_PTX_XID	 = 0x00A3 	# Len = 3
BIT_PTX_XID_0	 = 0
#MPP Tx reports extended ID in XID(0x8F:0), B4; EPP Tx ID(0x30)
BIT_PTX_XID_1	 = 8
BIT_PTX_XID_2	 = 16
I2CREG_PTX_AUTH_SUPP	 = 0x00A6 	# Len = 1
I2CREG_THERMAL_CTRL	 = 0x00A7 	# Len = 1
I2CREG_POT_LD_PWR	 = 0x00A8 	# Len = 2
I2CREG_NEG_LD_PWR	 = 0x00AA 	# Len = 2
I2CREG_NEGO_DONE_PWR	 = 0x00AC 	# Len = 2
I2CREG_FW_DATE_CODE	 = 0x00B0 	# Len = 11
BIT_FW_DATE_CODE_0	 = 0
#'ASCII code of firmware compile date. For example, compile date value:0x4E 0x6F 0x76 0x20 0x31 0x30 0x20 0x32 0x30 0x32 0x32 means 'Nov 10 2022'
BIT_FW_DATE_CODE_1	 = 8
BIT_FW_DATE_CODE_2	 = 16
BIT_FW_DATE_CODE_3	 = 24
BIT_FW_DATE_CODE_4	 = 32
BIT_FW_DATE_CODE_5	 = 40
BIT_FW_DATE_CODE_6	 = 48
BIT_FW_DATE_CODE_7	 = 56
BIT_FW_DATE_CODE_8	 = 64
BIT_FW_DATE_CODE_9	 = 72
BIT_FW_DATE_CODE_10	 = 80
I2CREG_RX_RCVD_PWR	 = 0x00BC 	# Len = 2

I2CREG_RCVD_MSG_CMD	 = 0x00D4 	# Len = 1
I2CREG_RCVD_MSG	 = 0x00D5 	# Len = 8
I2CREG_RCVD_MSG_END	 = 0x00DD 	# Len = 1

I2CREG_OP_MODE	 = 0x0102 	# Len = 1
I2CREG_OP_SUB_MODE	 = 0x0103 	# Len = 1
I2CREG_SYS_ERR_LATCH	 = 0x0104 	# Len = 4
BIT_SYS_HARDFAULT_ERR	 = 0
#Core hard fault error0: No hard fault error detected1: Hard fault error detected
BIT_HW_WDT_TRIGGER_ERR	 = 1
#HW WDT trigger latch0: HW WDT not triggered 1: HW WDT triggered
BIT_FTP_ERR	 = 2
#FTP IP error0: No FTP IP error detected1: FTP IP error detected
BIT_FTP_BOOT_ERR	 = 3
#FTP boot error0: No FTP boot error detected1: FTP boot error detected
BIT_FTP_PE_ADC_ERR	 = 8
#FTP PE_ADC section error0: No error1: Section header error2: Section CRC failed3: Skipped
BIT_FTP_PE_TRIM_ERR	 = 10
#FTP PE section error0: No error1: Section header error2: Section CRC failed3: Skipped
BIT_FTP_CFG_ERR	 = 12
#FTP Configuration section error0: No error1: Section header error2: Section CRC failed3: Skipped
BIT_FTP_PATCH_ERR	 = 14
#FTP Patch section error0: No error1: Section header error2: Section CRC failed3: Skipped
I2CREG_SYS_CMD	 = 0x0108 	# Len = 2
BIT_SWITCH_2_TX	 = 0
#Switch to Qi TX command.Write 1 to switch to Qi TX mode
BIT_SWITCH_2_RX	 = 1
#Switch to Qi RX command.Write 1 to switch to Qi RX mode
BIT_FTP_WR	 = 2
#FTP single sector write command.Write 1 to program specified FTP sector. The sector should be erased before programming. Command is password protected. Sector number to be programmed shall be specified in aux_addr register. Data to be programmed shall be specified in aux_data_000 ~ aux_data_127. This register is self-cleared when the operation is completed.
BIT_FTP_RD	 = 3
#FTP single sector read command.Write 1 to read the data from specified FTP sector into aux_data_000 ~ aux_data_127 registers. Sector number should be specified in aux_addr. This bit is self-cleared when the operation is completed.
BIT_FTP_ERASE	 = 4
#FTP single sector erase command.Write 1 to erase specified FTP sector. Command is password protected. Sector number should be specified in aux_addr register. This register is self-cleared when the operation is completed.
BIT_FTP_FULL_ERASE	 = 5
#FTP full erase command.Write 1 to full erase FTP. Command is password protected. This register is self-cleared when the operation is completed.
BIT_FTP_ERASE_WR	 = 6
#FTP single sector erase write command.Write 1 to erase and program data to specified sector. Command is password protected. Sector number should be specified in aux_addr register. Data to be programmed should be specified in aux_data_000 ~ aux_data_127. This register is self-cleared when the operation is completed.
BIT_RST_FTP_DIS	 = 7
#Reset with FTP disable command.Write 1 to perform device reset and skip FTP execution, allowing FTP erase / program to be performed safely. This register is self-cleared when the operation is completed.

BIT_EXEC_ADDR	 = 13
#Execute memory addressWrite 1 to request FW to execute a code located at address specified in aux_addr register. This bit is self-cleared when the operation is completed.
BIT_MEM_RD	 = 14
#Memory read commandWrite 1 to read the data from the device's memory space into the aux_data_xx registers. The aux_addr register specifies the 32bit address. The aux_len register specifies read length (number of bytes - 1)This bit is self-cleared when the operation is completed.
BIT_MEM_WR	 = 15
#Memory write commandWrite 1 to write the data from the aux_data_xx registers into the device's memory space. The mem_access_addr register specifies the absolute memory address. The mem_access_len register specifies the length to be written (eg: 0x0: 1byte; 0x1: 2bytes ¡­). This bit is self-cleared when the operation is completed.

I2CREG_AUX_LEN	 = 0x010B 	# Len = 1
I2CREG_AUX_ADDR	 = 0x010C 	# Len = 4
I2CREG_GPIO0_FUNC	 = 0x0110 	# Len = 1
I2CREG_GPIO1_FUNC	 = 0x0111 	# Len = 1
I2CREG_GPIO2_FUNC	 = 0x0112 	# Len = 1
I2CREG_GPIO3_FUNC	 = 0x0113 	# Len = 1
I2CREG_GPIO4_FUNC	 = 0x0114 	# Len = 1
I2CREG_GPI5_FUNC	 = 0x0115 	# Len = 1
I2CREG_GPI6_FUNC	 = 0x0116 	# Len = 1
#///< 00 - in_fl:  No function (Hi-Z)
GPIO_FUNC_IN_FL = 0,
#///< 01 - out_od: No function (Drive low)
GPIO_FUNC_OD_LO = 1
#///< 04 - out_od: Interrupt bar (0=active, 1=inactive)
GPIO_FUNC_OD_INTB = 4
#///< 05 - out_pp: FW ready (1=ready, 0=not ready)
GPIO_FUNC_PP_FW_RDY = 5
#///< 06 - in_fl:  LDO block (0=unblock, 1=block)
GPIO_FUNC_IN_LDO_BLOCK = 6
#///< 07 - in_fl:  Stop ASK/FSK communication (0=unblock, 1=block)
GPIO_FUNC_IN_DIS_COMM = 7

I2CREG_MEAS_S16	 = 0x0118 	# Len = 10
BIT_MEAS_ICUR	 = 0
#Current measurement.
BIT_MEAS_VRECT	 = 16
#Rectifier voltage measurement.
BIT_MEAS_VOUT	 = 32
#Main LDO voltage measurement.
BIT_MEAS_VTMEAS	 = 48
#Chip temperature measurement.
BIT_MEAS_DFT1	 = 64
#DFT1 measurement.
I2CREG_MEAS_END	 = 0x0122 	# Len = 2
BIT_MEAS_DFT2	 = 0
#DFT2 measurement.
I2CREG_LAST_CE	 = 0x0124 	# Len = 2
I2CREG_SIGNAL_STRENGTH	 = 0x0126 	# Len = 1
I2CREG_OVP_ADC_THRES	 = 0x0127 	# Len = 1
I2CREG_OCP_ADC_THRES	 = 0x0128 	# Len = 1
I2CREG_OVTP_ADC_THRES	 = 0x0129 	# Len = 1
I2CREG_PTC	 = 0x012A 	# Len = 12
BIT_MINOR_VER	 = 0
#Power Transfer Contract Qi spec minor version number.
BIT_MAJOR_VER	 = 4
#Power Transfer Contract Qi spec major version number.
BIT_PCH	 = 8
#Qi Power Transfer Contract. Power Control Hold-off Time (in ms)in the range of 5 ms up to (and including) 205 ms.
BIT_RPR_HDR	 = 16
#Qi Power Transfer Contract. Received Power Reporting Header. Adopt either one of these values:0x31: RP24 format0x04: RP8 format
BIT_REF_PWR	 = 24
#Qi 1.3 Reference Power Field. This value should be 2x of power in watt.
BIT_CFG_CNT	 = 32
#Reserved field. Placeholder for CFG cnt field for ease of FW coding.
BIT_OB	 = 36
#Qi Power transfer contract. Out-of-band communications functionality is supported (ONE) or not supported (ZERO).
BIT_AI	 = 38
#Qi Power transfer contract. Authentication functionality is supported (ONE) or not supported (ZERO).
BIT_PROP	 = 39
#CFG Prop Field. This field should be kept zero for current FW.This is placeholder only, fixed to zero in FW.
BIT_WIN_OFFSET	 = 40
#Received Power window offset. Specified in uinits of 4ms. Keep default value (changing requires system level review).
BIT_WIN_SZ	 = 43
#Received Power window offset. Specified in uinits of 4ms. Keep default value (changing requires system level review).
BIT_DUP	 = 48
#Qi Power transfer contract. Simultaneous incoming and outgoing data streams are supported (ONE) or not supported (ZERO).
BIT_BUF_SZ	 = 49
#Qi Power Transfer Contract. The size of the transport-layer buffer for receiving a data transport stream. The number of bytes in the buffer is equal to 16*2^n, with n the value contained in the Buffer Size field.Range 16 to 2048 bytes
BIT_FSK_DEPTH	 = 52
#Qi Power Transfer contract.FSK modulation depth
BIT_FSK_POL	 = 54
#Qi Power transfer contract. The requested FSK polarity is positive (ZERO) or negative (ONE).
BIT_NEG	 = 55
#Qi Power transfer contract. The Extended Protocol is supported (ONE) or not supported (ZERO). If the Neg bit is set to ZERO, all bits of the AI, OB, Pol, and Depth fields shall be set to ZERO as well
BIT_GUA_PWR	 = 56
#Qi 1.3 Guaranteed Power Field. This value should be 2x of power in watt.
BIT_REPING_DLY	 = 64
#Qi 1.3 Power Transfer Contract re-ping delay. In units of 200ms, Max is 12.6s
BIT_CLOAKL	 = 72
#MPP Cloak lower byte value.
BIT_CLOAKH	 = 80
#MPP Cloak higher byte value.
BIT_FREQ_SEL	 = 82
#MPP Freq select value.0 - Reserved1 - 360KHz2 - Reserved3 - Reserved
BIT_CLOAK_DET	 = 84
#MPP Cloak detect ping delay value. Specified in 100ms. Setting the delay value to 0 disables the cloak detect pings.
BIT_EGPL	 = 88
#MPP Extended Guaranteed Power. Specified in 100mW units. Default 0 and only used in MPP.
I2CREG_PTC_END	 = 0x0136 	# Len = 1
BIT_EGPH	 = 0
BIT_PCP	 = 1
#MPP Power Control Profile.0 - Default power profile1 - Low K profile
BIT_FSK_N_CYCLES	 = 2
#Number of power signals cycles that make up one FSK bit0: 512 cycles/FSK bit1: 256 cycles/FSK bit2: 128 cycles/FSK bit3: 64 cycles/FSK bit

I2CREG_RX_ARC_AUTO_OFF_THRES	 = 0x0140 	# Len = 1
I2CREG_RX_RECT_SETTING	 = 0x0141 	# Len = 1
BIT_RX_RECT_DELAY	 = 0
#Rx rectifier setting. When writing to this register, it overwrites configuration preset.Reading is invalid if not set.
BIT_RX_RECT_MODE	 = 2
#Rx rectifier setting. When writing to this register, it overwrites configuration preset.Reading is invalid if not set.
BIT_RX_RECT_MOT	 = 4
#Rx rectifier setting. When writing to this register, it overwrites configuration preset.Reading is invalid if not set.
BIT_RX_SHORT_MOT	 = 6
#Rx rectifier setting. When writing to this register, it overwrites configuration preset.Reading is invalid if not set.

I2CREG_RX_VRECT_TGT	 = 0x0164 	# Len = 2
I2CREG_AUX_DATA00	 = 0x0180 	# Len = 128
I2CREG_AUX_DATA127	 = 0x01FF

