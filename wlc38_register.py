I2CREG_CHIP_ID	 = 0x0000 	# Len = 2
I2CREG_CHIP_REV	 = 0x0002 	# Len = 1
I2CREG_CUST_ID	 = 0x0003 	# Len = 1
I2CREG_ROM_ID	 = 0x0004 	# Len = 2
I2CREG_NVM_PATCH_ID	 = 0x0006 	# Len = 2
I2CREG_RAM_PATCH_ID	 = 0x0008 	# Len = 2
I2CREG_CFG_ID	 = 0x000A 	# Len = 2
I2CREG_PE_ID	 = 0x000C 	# Len = 2
I2CREG_OP_MODE	 = 0x000E 	# Len = 1
I2CREG_OP_SUB_MODE	 = 0x000F 	# Len = 1
I2CREG_DEVICE_ID	 = 0x0010 	# Len = 16
I2CREG_SYS_ERR_LATCH	 = 0x002C 	# Len = 4
BIT_SYS_M0_HARDFAULT_ERR	 = 0
#0x00: No error0x01: Error present
BIT_HW_WDT_TRIGGER_ERR	 = 1
#0x00: Not triggered0x01: Triggered
BIT_NVM_ERR	 = 2
#0x00: No error0x01: Error present
BIT_NVM_BOOT_ERR	 = 4
#0x00: No error0x01: Error present
BIT_NVM_PE_ERR	 = 8
#0x00: No error0x01: Section header error0x02: Section CRC failed0x03: Reserved
BIT_NVM_CFG_ERR	 = 10
#0x00: No error0x01: Section header error0x02: Section CRC failed0x03: Reserved
BIT_NVM_PATCH_ERR	 = 12
#0x00: No error0x01: Section header error0x02: Section CRC failed0x03: Reserved
BIT_NVM_PI_ERR	 = 14
#0x00: No error0x01: Section header error0x02: Section CRC failed0x03: Reserved
I2CREG_GPIO0_FUNC	 = 0x0030 	# Len = 1
I2CREG_GPIO1_FUNC	 = 0x0031 	# Len = 1
I2CREG_GPIO2_FUNC	 = 0x0032 	# Len = 1
I2CREG_GPIO3_FUNC	 = 0x0033 	# Len = 1
I2CREG_RX_INTR_EN	 = 0x0080 	# Len = 4
GPIO_FUNC_NONE   = 0,                 #///< 00 - in_fl:  No function (GPIO will be configured as Input floating)
GPIO_FUNC_NONE_PU= 1,                  #///< 01 - in_pu:  No function (GPIO will be configured as Input pull-up)
GPIO_FUNC_NONE_PD= 2,                  #///< 02 - in_pd:  No function (GPIO will be configured as Input pull-down)
GPIO_FUNC_INTB_OD= 3,                  #///< 03 - out_od: Interrupt (0=active, 1=inactive)
GPIO_FUNC_INTB_PP= 4,                  #///< 04 - out_pp: Interrupt (0=active, 1=inactive, useful with long wires)
GPIO_FUNC_FW_RDY = 5,                   #///< 05 - out_pp: High on FW ready (before main loop)
GPIO_FUNC_LDO_BLOCK= 6,                #///< 06 - in_fl:  LDO block (0=unblock, 1=block)
GPIO_FUNC_RX_DIS_COM= 7,               #///< 07 - in_fl:  Rx stop ASK communication (0=unblock, 1=block)
GPIO_FUNC_RX_PWR_NEGO = 0x0B,              #///< 0B - out_pp: Power negotiated (0=off, 1=on)
GPIO_FUNC_RX_PWR_NEGO_INV = 0x0C,          #///< 0C - out_pp: Power negotiated (0=on, 1=off)
GPIO_FUNC_RX_PWR_NEGO_OD = 0x0D,           #///< 0D - out_od: Power negotiated (0=on, 1=off)
GPIO_FUNC_OD_LO = 0x29,                    #///< 29 - out_od: driven low
GPIO_FUNC_OD_HI = 0x2A,                    #///< 2A - out_od: driven high
GPIO_FUNC_PP_LO = 0x2B,                    #///< 2B - out_pp: driven low
GPIO_FUNC_PP_HI = 0x0C,                    #///< 2C - out_pp: driven high
BIT_RX_OVTP_INTR_EN	 = 0
#0x0: Disabled0x1: Enabled
BIT_RX_OCP_INTR_EN	 = 1
#0x0: Disabled0x1: Enabled
BIT_RX_OVP_INTR_EN	 = 2
#0x0: Disabled0x1: Enabled
BIT_RX_SYS_ERR_INTR_EN	 = 3
#0x0: Disabled0x1: Enabled
BIT_RX_SCP_INTR_EN	 = 4
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
BIT_RX_UVLO_INTR_EN	 = 12
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
I2CREG_RX_INTR_CLR	 = 0x0084 	# Len = 4
BIT_RX_OVTP_INTR_CLR	 = 0
#0x0: No change0x1: Will be cleared
BIT_RX_OCP_INTR_CLR	 = 1
#0x0: No change0x1: Will be cleared
BIT_RX_OVP_INTR_CLR	 = 2
#0x0: No change0x1: Will be cleared
BIT_RX_SYS_ERR_INTR_CLR	 = 3
#0x0: No change0x1: Will be cleared
BIT_RX_SCP_INTR_CLR	 = 4
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
BIT_RX_UVLO_INTR_CLR	 = 12
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
I2CREG_RX_INTR_LATCH	 = 0x0088 	# Len = 4
BIT_RX_OVTP_INTR_LATCH	 = 0
#0x0: Did not occur0x1: Occurred
BIT_RX_OCP_INTR_LATCH	 = 1
#0x0: Did not occur0x1: Occurred
BIT_RX_OVP_INTR_LATCH	 = 2
#0x0: Did not occur0x1: Occurred
BIT_RX_SYS_ERR_INTR_LATCH	 = 3
#0x0: Did not occur0x1: Occurred
BIT_RX_SCP_INTR_LATCH	 = 4
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
BIT_RX_UVLO_INTR_LATCH	 = 12
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
I2CREG_RX_STAT	 = 0x008C 	# Len = 4
BIT_RX_OVTP_STAT	 = 0
#0x0: Is not occuring0x1: Occurring
BIT_RX_OCP_STAT	 = 1
#0x0: Is not occuring0x1: Occurring
BIT_RX_OVP_STAT	 = 2
#0x0: Is not occuring0x1: Occurring
BIT_RX_SYS_ERR_STAT	 = 3
#0x0: Is not occuring0x1: Occurring
BIT_RX_SCP_STAT	 = 4
#0x0: Is not occuring0x1: Occurring
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
BIT_RX_UVLO_STAT	 = 12
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
I2CREG_RX_IOUT	 = 0x0096 	# Len = 2
BIT_MEAS_VISNS	 = 0
I2CREG_RX_CHIP_TEMP	 = 0x0098 	# Len = 2
I2CREG_RX_OP_FREQ	 = 0x009A 	# Len = 2
I2CREG_RX_NTC	 = 0x009C 	# Len = 2
I2CREG_RX_CTRL_ERR	 = 0x00A4 	# Len = 2
I2CREG_RX_RCVD_PWR	 = 0x00A6 	# Len = 2
I2CREG_RX_SIGNAL_STRENGTH	 = 0x00A8 	# Len = 1
I2CREG_RX_PTC_GUA_PWR	 = 0x00AA 	# Len = 1
BIT_RX_GUA_PWR	 = 0
I2CREG_RX_PTC_MAX_PWR	 = 0x00AB 	# Len = 1
BIT_RX_MAX_PWR	 = 0
I2CREG_RX_PTC_RP_HDR	 = 0x00AC 	# Len = 1
BIT_RX_RP_HDR	 = 0
#0x31: RP24 format0x04: RP8 format
I2CREG_RX_PTC_FSK_CFG	 = 0x00AD 	# Len = 1
BIT_RX_FSK_DEPTH	 = 0
#0x0: -282~-249 / 30.25~63.250x1: -157~-124 / 61.5~94.50x2: -94.5~-61.5 / 124~1570x3: -63.25~-30.25 / 249~282
BIT_RX_FSK_POLARITY	 = 2
#0x0: Positive0x1: Negative
BIT_RX_NEG	 = 3
#0x0: BPP0x1: EPP
I2CREG_RX_VOUT_SET	 = 0x00B1 	# Len = 2
BIT_RX_VOUT_SET_LO	 = 6
#MIN:0MAX:320
I2CREG_RX_ILIM_SET	 = 0x00B5 	# Len = 1
I2CREG_FOD_CUR_THRES	 = 0x00B6 	# Len = 5
BIT_FOD_CUR_THRES1	 = 0
BIT_FOD_CUR_THRES2	 = 8
BIT_FOD_CUR_THRES3	 = 16
BIT_FOD_CUR_THRES4	 = 24
BIT_FOD_CUR_THRES5	 = 32
I2CREG_FOD_GAIN	 = 0x00BB 	# Len = 6
BIT_FOD_GAIN_OFFSET0	 = 0
BIT_FOD_GAIN_OFFSET1	 = 8
BIT_FOD_GAIN_OFFSET2	 = 16
BIT_FOD_GAIN_OFFSET3	 = 24
BIT_FOD_GAIN_OFFSET4	 = 32
BIT_FOD_GAIN_OFFSET5	 = 40
I2CREG_FOD_OFFSET	 = 0x00C1 	# Len = 6
BIT_FOD_OFFSET0	 = 0
BIT_FOD_OFFSET1	 = 8
BIT_FOD_OFFSET2	 = 16
BIT_FOD_OFFSET3	 = 24
BIT_FOD_OFFSET4	 = 32
BIT_FOD_OFFSET5	 = 40
I2CREG_RSER	 = 0x00C7 	# Len = 1
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
I2CREG_RX_DTS_SEND	 = 0x00D8 	# Len = 4
BIT_RX_DTS_ADC_SEND_LEN	 = 0
BIT_RX_DTS_ADC_SEND_REQUEST	 = 16
#0x00: ADC/end0x02: ADC/auth0x05: ADC/rst0x10: ADC/prop0x11: ADC/prop0x12: ADC/prop0x13: ADC/prop0x14: ADC/prop0x15: ADC/prop0x16: ADC/prop0x17: ADC/prop0x18: ADC/prop0x19: ADC/prop0x1a: ADC/prop0x1b: ADC/prop0x1c: ADC/prop0x1d: ADC/prop0x1e: ADC/prop0x1f: ADC/prop
I2CREG_RX_DTS_RCVD	 = 0x00DC 	# Len = 4
BIT_RX_DTS_ADC_RCVD_LEN	 = 0
BIT_RX_DTS_ADC_RCVD_REQUEST	 = 16
#0x00: ADC/end0x02: ADC/auth0x05: ADC/rst0x10: ADC/prop0x11: ADC/prop0x12: ADC/prop0x13: ADC/prop0x14: ADC/prop0x15: ADC/prop0x16: ADC/prop0x17: ADC/prop0x18: ADC/prop0x19: ADC/prop0x1a: ADC/prop0x1b: ADC/prop0x1c: ADC/prop0x1d: ADC/prop0x1e: ADC/prop0x1f: ADC/prop
I2CREG_AUX_DATA	 = 0x0180
I2CREG_SEND_MSG	 = 0x0180
I2CREG_RCVD_MSG  = 0x0190
DTS_SEND_MSG_000        = 0X0200
DTS_RCVD_MSG_000        = 0x0280
#HW reg address
HWREG_GPIO_INPUT_VAL_RegAddr = 0x2001A01C
