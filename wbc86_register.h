#define I2CREG_CHIP_ID	 0x0000 	// Len = 2
#define I2CREG_CHIP_REV	 0x0002 	// Len = 1
#define I2CREG_CUST_ID	 0x0003 	// Len = 1
#define I2CREG_ROM_ID	 0x0004 	// Len = 2
#define I2CREG_NVM_PATCH_ID	 0x0006 	// Len = 2
#define I2CREG_RAM_PATCH_ID	 0x0008 	// Len = 2
#define I2CREG_CFG_ID	 0x000A 	// Len = 2
#define I2CREG_PE_ID	 0x000C 	// Len = 1
#define I2CREG_OP_MODE	 0x000E 	// Len = 1
#define I2CREG_OP_SUB_MODE	 0x000F 	// Len = 1
#define I2CREG_DEVICE_ID	 0x0010 	// Len = 16
#define I2CREG_SYS_CMD	 0x0020 	// Len = 1
	#define BIT_SWITCH_2_TX	0
	/*0x0: Do nothing0x1: Perform Switch*/
	#define BIT_SWITCH_2_RX	1
	/*0x0: Do nothing0x1: Perform switch*/
#define I2CREG_SYS_ERR_LATCH	 0x002C 	// Len = 4
	#define BIT_SYS_M0_HARDFAULT_ERR	0
	/*0x00: No error0x01: Error present*/
	#define BIT_HW_WDT_TRIGGER_ERR	1
	/*0x00: Not triggered0x01: Triggered*/
	#define BIT_FTP_ERR	2
	/*0x00: No error0x01: Error present*/
	#define BIT_FTP_BOOT_ERR	4
	/*0x00: No error0x01: Error present*/
	#define BIT_FTP_PE_ERR	8
	/*0x00: No error0x01: Section header error0x02: Section CRC failed0x03: Reserved*/
	#define BIT_FTP_CFG_ERR	10
	/*0x00: No error0x01: Section header error0x02: Section CRC failed0x03: Reserved*/
	#define BIT_FTP_PATCH_ERR	12
	/*0x00: No error0x01: Section header error0x02: Section CRC failed0x03: Reserved*/
	#define BIT_FTP_PI_ERR	14
	/*0x00: No error0x01: Section header error0x02: Section CRC failed0x03: Reserved*/
	#define BIT_FTP_PE_ADC_ERR	16
	/*0x0: No error0x1: Section header error0x2: Section CRC failed0x3: Reserved*/
#define I2CREG_GPIO0_FUNC	 0x0030 	// Len = 1
#define I2CREG_GPIO1_FUNC	 0x0031 	// Len = 1
#define I2CREG_GPIO2_FUNC	 0x0032 	// Len = 1
#define I2CREG_GPIO3_FUNC	 0x0033 	// Len = 1
#define I2CREG_GPIO4_FUNC	 0x0034 	// Len = 1
#define I2CREG_GPIO5_FUNC	 0x0035 	// Len = 1
#define I2CREG_GPIO6_FUNC	 0x0036 	// Len = 1
#define I2CREG_GPIO7_FUNC	 0x0037 	// Len = 1
#define I2CREG_MEAS_VRECT	 0x0040 	// Len = 2
#define I2CREG_MEAS_VOUT	 0x0042 	// Len = 2
#define I2CREG_MEAS_ICUR	 0x0044 	// Len = 2
	#define BIT_MEAS_VISNS	0
#define I2CREG_MEAS_VTMEAS	 0x0046 	// Len = 2
#define I2CREG_MEAS_NTC	 0x0048 	// Len = 2
#define I2CREG_OP_FREQ	 0x004C 	// Len = 2
#define I2CREG_TX_INTR_EN	 0x00C0 	// Len = 4
	#define BIT_TX_OVTP_INTR_EN	0
	/*0x0: Disabled0x1: Enabled*/
	#define BIT_TX_OCP_INTR_EN	1
	/*0x0: Disabled0x1: Enabled*/
	#define BIT_TX_OVP_INTR_EN	2
	/*0x0: Disabled0x1: Enabled*/
	#define BIT_TX_SYS_ERR_INTR_EN	3
	/*0x0: Disabled0x1: Enabled*/
	#define BIT_TX_RP_PKT_RVCD_INTR_EN	4
	/*0x0: Disabled0x1: Enabled*/
	#define BIT_TX_CE_PKT_RVCD_INTR_EN	5
	/*0x0: Disabled0x1: Enabled*/
	#define BIT_TX_PKT_SENT_INTR_EN	6
	/*0x0: Disabled0x1: Enabled*/
	#define BIT_TX_EXT_MON_INTR_EN	7
	/*0x0: Disabled0x1: Enabled*/
	#define BIT_TX_CE_TO_INTR_EN	8
	/*0x0: Disabled0x1: Enabled*/
	#define BIT_TX_RP_TO_INTR_EN	9
	/*0x0: Disabled0x1: Enabled*/
	#define BIT_TX_EPT_INTR_EN	10
	/*0x0: Disabled0x1: Enabled*/
	#define BIT_TX_START_PING_INTR_EN	11
	/*0x0: Disabled0x1: Enabled*/
	#define BIT_TX_SS_PKT_RCVD_INTR_EN	12
	/*0x0: Disabled0x1: Enabled*/
	#define BIT_TX_ID_PKT_RVCD_INTR_EN	13
	/*0x0: Disabled0x1: Enabled*/
	#define BIT_TX_CFG_PKT_RCVD_INTR_EN	14
	/*0x0: Disabled0x1: Enabled*/
	#define BIT_TX_PP_PKT_RCVD_INTR_EN	15
	/*0x0: Disabled0x1: Enabled*/
	#define BIT_TX_BRDG_MD_INTR_EN	16
	/*0x0: Disabled0x1: Enabled*/
	#define BIT_TX_FOD_DET_INTR_EN	17
	/*0x0: Disabled0x1: Enabled*/
	#define BIT_TX_PTC_UPDATE_INT_EN	18
	/*0x0: Disabled0x1: Enabled*/
#define I2CREG_TX_INTR_CLR	 0x00C4 	// Len = 4
	#define BIT_TX_OVTP_INTR_CLR	0
	/*0x0: No change0x1: Will be cleared*/
	#define BIT_TX_OCP_INTR_CLR	1
	/*0x0: No change0x1: Will be cleared*/
	#define BIT_TX_OVP_INTR_CLR	2
	/*0x0: No change0x1: Will be cleared*/
	#define BIT_TX_SYS_ERR_INTR_CLR	3
	/*0x0: No change0x1: Will be cleared*/
	#define BIT_TX_RP_PKT_RVCD_INTR_CLR	4
	/*0x0: No change0x1: Will be cleared*/
	#define BIT_TX_CE_PKT_RVCD_INTR_CLR	5
	/*0x0: No change0x1: Will be cleared*/
	#define BIT_TX_PKT_SENT_INTR_CLR	6
	/*0x0: No change0x1: Will be cleared*/
	#define BIT_TX_EXT_MON_INTR_CLR	7
	/*0x0: No change0x1: Will be cleared*/
	#define BIT_TX_CE_TO_INTR_CLR	8
	/*0x0: No change0x1: Will be cleared*/
	#define BIT_TX_RP_TO_INTR_CLR	9
	/*0x0: No change0x1: Will be cleared*/
	#define BIT_TX_EPT_INTR_CLR	10
	/*0x0: No change0x1: Will be cleared*/
	#define BIT_TX_START_PING_INTR_CLR	11
	/*0x0: No change0x1: Will be cleared*/
	#define BIT_TX_SS_PKT_RCVD_INTR_CLR	12
	/*0x0: No change0x1: Will be cleared*/
	#define BIT_TX_ID_PKT_RVCD_INTR_CLR	13
	/*0x0: No change0x1: Will be cleared*/
	#define BIT_TX_CFG_PKT_RCVD_INTR_CLR	14
	/*0x0: No change0x1: Will be cleared*/
	#define BIT_TX_PP_PKT_RCVD_INTR_CLR	15
	/*0x0: No change0x1: Will be cleared*/
	#define BIT_TX_BRDG_MD_INTR_CLR	16
	/*0x0: No change0x1: Will be cleared*/
	#define BIT_TX_FOD_DET_INTR_CLR	17
	/*0x0: No change0x1: Will be cleared*/
	#define BIT_TX_PTC_UPDATE_INT_CLR	18
	/*0x0: No change0x1: Will be cleared*/
#define I2CREG_TX_INTR_LATCH	 0x00C8 	// Len = 4
	#define BIT_TX_OVTP_INTR_LATCH	0
	/*0x0: Did not occur0x1: Occurred*/
	#define BIT_TX_OCP_INTR_LATCH	1
	/*0x0: Did not occur0x1: Occurred*/
	#define BIT_TX_OVP_INTR_LATCH	2
	/*0x0: Did not occur0x1: Occurred*/
	#define BIT_TX_SYS_ERR_INTR_LATCH	3
	/*0x0: Did not occur0x1: Occurred*/
	#define BIT_TX_RP_PKT_RVCD_INTR_LATCH	4
	/*0x0: Did not occur0x1: Occurred*/
	#define BIT_TX_CE_PKT_RVCD_INTR_LATCH	5
	/*0x0: Did not occur0x1: Occurred*/
	#define BIT_TX_PKT_SENT_INTR_LATCH	6
	/*0x0: Did not occur0x1: Occurred*/
	#define BIT_TX_EXT_MON_INTR_LATCH	7
	/*0x0: Did not occur0x1: Occurred*/
	#define BIT_TX_CE_TO_INTR_LATCH	8
	/*0x0: Did not occur0x1: Occurred*/
	#define BIT_TX_RP_TO_INTR_LATCH	9
	/*0x0: Did not occur0x1: Occurred*/
	#define BIT_TX_EPT_INTR_LATCH	10
	/*0x0: Did not occur0x1: Occurred*/
	#define BIT_TX_START_PING_INTR_LATCH	11
	/*0x0: Did not occur0x1: Occurred*/
	#define BIT_TX_SS_PKT_RCVD_INTR_LATCH	12
	/*0x0: Did not occur0x1: Occurred*/
	#define BIT_TX_ID_PKT_RVCD_INTR_LATCH	13
	/*0x0: Did not occur0x1: Occurred*/
	#define BIT_TX_CFG_PKT_RCVD_INTR_LATCH	14
	/*0x0: Did not occur0x1: Occurred*/
	#define BIT_TX_PP_PKT_RCVD_INTR_LATCH	15
	/*0x0: Did not occur0x1: Occurred*/
	#define BIT_TX_BRDG_MD_INTR_LATCH	16
	/*0x0: Did not occur0x1: Occurred*/
	#define BIT_TX_FOD_DET_INTR_LATCH	17
	/*0x0: Did not occur0x1: Occurred*/
	#define BIT_TX_PTC_UPDATE_INT_LATCH	18
	/*0x0: Did not occur0x1: Occurred*/
#define I2CREG_TX_STAT	 0x00CC 	// Len = 4
	#define BIT_TX_OVTP_STAT	0
	/*0x0: Is not occuring0x1: Occurring*/
	#define BIT_TX_OCP_STAT	1
	/*0x0: Is not occuring0x1: Occurring*/
	#define BIT_TX_OVP_STAT	2
	/*0x0: Is not occuring0x1: Occurring*/
	#define BIT_TX_SYS_ERR_STAT	3
	/*0x0: Is not occuring0x1: Occurring*/
	#define BIT_TX_RP_PKT_RVCD_STAT	4
	/*0x0: Is not occuring0x1: Occurring*/
	#define BIT_TX_CE_PKT_RVCD_STAT	5
	/*0x0: Is not occuring0x1: Occurring*/
	#define BIT_TX_PKT_SENT_STAT	6
	/*0x0: Is not occuring0x1: Occurring*/
	#define BIT_TX_EXT_MON_INTR_STAT	7
	/*0x0: Is not occuring0x1: Occurring*/
	#define BIT_TX_CE_TO_INTR_STAT	8
	/*0x0: Is not occuring0x1: Occurring*/
	#define BIT_TX_RP_TO_INTR_STAT	9
	/*0x0: Is not occuring0x1: Occurring*/
	#define BIT_TX_EPT_STAT	10
	/*0x0: Is not occuring0x1: Occurring*/
	#define BIT_TX_START_PING_STAT	11
	/*0x0: Is not occuring0x1: Occurring*/
	#define BIT_TX_SS_PKT_RCVD_STAT	12
	/*0x0: Is not occuring0x1: Occurring*/
	#define BIT_TX_ID_PKT_RVCD_STAT	13
	/*0x0: Is not occuring0x1: Occurring*/
	#define BIT_TX_CFG_PKT_RCVD_STAT	14
	/*0x0: Is not occuring0x1: Occurring*/
	#define BIT_TX_PP_PKT_RCVD_STAT	15
	/*0x0: Is not occuring0x1: Occurring*/
	#define BIT_TX_BRDG_MD_INTR_STAT	16
	/*0x0: Is not occuring0x1: Occurring*/
	#define BIT_TX_FOD_DET_INTR_STAT	17
	/*0x0: Is not occuring0x1: Occurring*/
	#define BIT_TX_PTC_UPDATE_INT_STAT	18
	/*0x0: Is not occuring0x1: Occurring*/
#define I2CREG_TX_CMD	 0x00D0 	// Len = 2
	#define BIT_TX_EN	0
	/*0x0: Do nothing0x1: Perform action*/
	#define BIT_TX_DIS	1
	/*0x0: Do nothing0x1: Perform action*/
	#define BIT_TX_SEND_MSG	3
	/*0x0: Do nothing0x1: Perform action*/
#define I2CREG_TX_MAX_FREQ	 0x00D2 	// Len = 2
#define I2CREG_TX_MIN_FREQ	 0x00D4 	// Len = 2
#define I2CREG_TX_PING_FREQ	 0x00D6 	// Len = 2
#define I2CREG_TX_MAX_DC	 0x00D8 	// Len = 1
#define I2CREG_TX_MIN_DC	 0x00D9 	// Len = 1
#define I2CREG_TX_PING_DC	 0x00DA 	// Len = 1
#define I2CREG_TX_PING_INTERVAL	 0x00DB 	// Len = 1
#define I2CREG_TX_PING_DUR	 0x00DC 	// Len = 1
#define I2CREG_TX_OVP_THRES	 0x00DD 	// Len = 1
#define I2CREG_TX_OCP_THRES	 0x00DE 	// Len = 1
#define I2CREG_TX_OVTP_THRES	 0x00DF 	// Len = 1
#define I2CREG_TX_FOD_PLOSS_THRES	 0x00E0 	// Len = 1
#define I2CREG_TX_FOD_DBNC_CNT	 0x00E1 	// Len = 1
#define I2CREG_TX_CE_TO_MAX_CNT	 0x00E2 	// Len = 1
#define I2CREG_TX_FHOP_STEP	 0x00E3 	// Len = 1
#define I2CREG_TX_PID_MAX_CUR	 0x00E4 	// Len = 1
#define I2CREG_TX_EPT_REASON_RCVD	 0x00E6 	// Len = 3
	#define BIT_TX_EPT_SRC_OVP	0
	/*0x0: Did not appear0x1: appeared*/
	#define BIT_TX_EPT_SRC_OCP	1
	/*0x0: Did not appear0x1: appeared*/
	#define BIT_TX_EPT_SRC_OVTP	2
	/*0x0: Did not appear0x1: appeared*/
	#define BIT_TX_EPT_SRC_FOD	3
	/*0x0: Did not appear0x1: appeared*/
	#define BIT_TX_EPT_SRC_CMD	4
	/*0x0: Did not appear0x1: appeared*/
	#define BIT_TX_EPT_SRC_RX	5
	/*0x0: Did not appear0x1: appeared*/
	#define BIT_TX_EPT_SRC_CE_TO	6
	/*0x0: Did not appear0x1: appeared*/
	#define BIT_TX_EPT_SRC_RP_TO	7
	/*0x0: Did not appear0x1: appeared*/
	#define BIT_TX_EPT_SRC_RX_RST	8
	/*0x0: Did not appear0x1: appeared*/
	#define BIT_TX_EPT_SRC_SYS_ERR	9
	/*0x0: Did not appear0x1: appeared*/
	#define BIT_TX_EPT_SRC_SS_TO	10
	/*0x0: Did not appear0x1: appeared*/
	#define BIT_TX_EPT_SRC_SS	11
	/*0x0: Did not appear0x1: appeared*/
	#define BIT_TX_EPT_SRC_ID	12
	/*0x0: Did not appear0x1: appeared*/
	#define BIT_TX_EPT_SRC_CFG	13
	/*0x0: Did not appear0x1: appeared*/
	#define BIT_TX_EPT_SRC_CFG_CNT_ERR	14
	/*0x0: Did not appear0x1: appeared*/
	#define BIT_TX_EPT_SRC_PCH	15
	/*0x0: Did not appear0x1: appeared*/
	#define BIT_TX_EPT_SRC_XID	16
	/*0x0: Did not appear0x1: appeared*/
	#define BIT_TX_EPT_SRC_NEGO	17
	/*0x0: Did not appear0x1: appeared*/
	#define BIT_TX_EPT_SRC_NEGO_TO	18
	/*0x0: Did not appear0x1: appeared*/
#define I2CREG_TX_OP_DC	 0x00E9 	// Len = 1
#define I2CREG_TX_CTRL	 0x00EA 	// Len = 1
	#define BIT_TX_BRDG_MD	0
	/*0x0: No change (same as ping)0x1: Manual half bridge mode0x2: Manual full bridge mode0x3: Auto switch*/
	#define BIT_TX_PING_HALF_BRDG	2
	/*0x0:Start ping in full bridge mode0x1:Start ping in half bridge mode*/
#define I2CREG_AUX_DATA	 0x0200 	// Len = 44
	#define BIT_AUX_DATA_256_/_SEND_MSG_00	0
	#define BIT_AUX_DATA_267_/_SEND_MSG_11	88
	#define BIT_AUX_DATA_278_/_RCVD_MSG_00	176
	#define BIT_AUX_DATA_289_/_RCVD_MSG_11	264
