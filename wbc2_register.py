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
#tx fw version must > 1.3.0.9
STWBC2_SET_PAGE        = 0x70
INDEX_PAGE_REGS        = 0
INDEX_PAGE_PARAM       = 2
INDEX_PAGE_LOG_EN      = 4
INDEX_PAGE_LOG_DISABLE = 5
INDEX_PAGE_TXPWR_EN    = 6
INDEX_PAGE_TXPWR_DIS   = 7

STWBC2_READ_HOST         = 0x72
STWBC2_WRITE_HOST        = 0x77

HOST_IF_CTL1             = 0x00
BIT_CTL1_TX_DIS          = 0
HOST_IF_CTL2             = 0x01
BIT_CTL2_RSP_ASKPP       = 0
BIT_CTL2_IS_GET_ASKPP    = 1
HOST_IF_CTL3             = 0x02
BIT_CTL3_CHECK_MAN_CODE  = 0
BIT_CTL3_CHECK_DEVICE_ID = 1

CHECK_RX_MAN_CODE_MSB    = 0x03
CHECK_RX_MAN_CODE_LSB    = 0x04
CHECK_RX_DEVICE_ID_MSB   = 0x05
CHECK_RX_DEVICE_ID_3     = 0x06
CHECK_RX_DEVICE_ID_2     = 0x07
CHECK_RX_DEVICE_ID_LSB   = 0x08

HOST_IF_STATUS           = 0x09

HOST_IF_EXT_ID_MSB       = 0x0A
HOST_IF_EXT_ID_7         = 0x0B
HOST_IF_EXT_ID_6         = 0x0C
HOST_IF_EXT_ID_5         = 0x0D
HOST_IF_EXT_ID_4         = 0x0E
HOST_IF_EXT_ID_3         = 0x0F
HOST_IF_EXT_ID_2         = 0x10
HOST_IF_EXT_ID_LSB       = 0x11
HOST_IF_MAN_CODE_MSB     = 0x12
HOST_IF_MAN_CODE_LSB     = 0x13
HOST_IF_DEVICE_ID_MSB    = 0x14
HOST_IF_DEVICE_ID_3      = 0x15
HOST_IF_DEVICE_ID_2      = 0x16
HOST_IF_DEVICE_ID_LSB    = 0x17
HOST_IF_WPID_MSB         = 0x18
HOST_IF_WPID_4           = 0x19
HOST_IF_WPID_3           = 0x1A
HOST_IF_WPID_2           = 0x1B
HOST_IF_WPID_1           = 0x1C
HOST_IF_WPID_LSB         = 0x1D
HOST_IF_SIGNAL_STRENGTH  = 0x1E
HOST_IF_RX_VERSION       = 0x1F
HOST_IF_CHARGE_STATUS    = 0x20
HOST_IF_REF_Q_FACTOR     = 0x21
HOST_IF_Q_FACTOR         = 0x22
HOST_IF_CE               = 0x23
HOST_IF_RP8              = 0x24
HOST_IF_EPT              = 0x25
HOST_IF_RP24_B2          = 0x26
HOST_IF_RP24_B1          = 0x27
HOST_IF_RP24_B0          = 0x28
#/* tx adc data */
HOST_IF_ADC_VIN                 = 0x29#SIZE 2
HOST_IF_TX_BRGMODE              = 0x2B
HOST_IF_TX_DUTY                 = 0x2C
HOST_IF_ADC_VBRG                = 0x2D#SIZE 2
HOST_IF_ADC_IBRG                = 0x2F#SIZE 2
HOST_IF_ADC_NTC                 = 0x31#SIZE 2
HOST_IF_ADC_FREQ                = 0x33#SIZE 2
HOST_IF_ALGO_CALIBRATION = 0x35

HOST_IF_TX_SEND_MSG_1E          = 0x40
HOST_IF_TX_SEND_MSG_1F          = 0x41
HOST_IF_TX_SEND_MSG_2E          = 0x42
HOST_IF_TX_SEND_MSG_2F          = 0x44
HOST_IF_TX_SEND_MSG_3F          = 0x46
HOST_IF_TX_SEND_MSG_4F          = 0x49
HOST_IF_TX_SEND_MSG_5F          = 0x4D
HOST_IF_TX_SEND_MSG_6F          = 0x52
HOST_IF_TX_SEND_MSG_7F          = 0x58
HOST_IF_RX_RCVD_MSG             = 0x5F

#/* Status reg bits (HOST_IF_STATUS register) */
WBC_QI_FSM_NO_STATE  = 0
STATUS_OBJECT_DETECTED          =0x01
STATUS_QI_POWER                 =0x02
STATUS_QI_DETECTED              =0x04
STATUS_MEDIUM_POWER             =0x08
WBC_QI_FSM_SELECTION_AP_STATE = 0x10
WBC_QI_FSM_SELECTION_QF_STATE = 0x20
WBC_QI_FSM_PRE_PING_STATE = 0x30
WBC_QI_FSM_PING_STATE = 0x40
WBC_QI_FSM_CONFIG_CHECK_ID_STATE = 0x50
WBC_QI_FSM_CONFIG_CHECK_EXT_ID_STATE = 0x60
WBC_QI_FSM_CONFIG_CHECK_CONF_STATE = 0x70
WBC_QI_FSM_NEGOTIATION_STATE = 0x80
WBC_QI_FSM_RENEGOTIATION_STATE = 0x90
WBC_QI_FSM_CALIBRATION_STATE = 0xA0
WBC_QI_FSM_POWER_TRANSFER_STATE = 0xB0
WBC_QI_FSM_POWER_PID_STATE = 0xC0

dic_tx_status = {
    0 : "FSM_NO_STATE",
    # 1 : "OBJECT_DETECTED",
    # 2 : "QI_POWER",
    # 4 : "QI_DETECTED",
    # 8 : "MEDIUM_POWER",
    0x10: "SELECTION_AP_STATE",#analog ping
    0x20: "SELECTION_QF_STATE",
    0x30: "PRE_PING_STATE",
    0x40: "PING_STATE",
    0x50: "CONFIG_CHECK_ID_STATE",
    0x60: "CONFIG_CHECK_EXT_ID_STATE",
    0x70: "CONFIG_CHECK_CONF_STATE",
    0x80: "NEGOTIATION_STATE",
    0x90: "RENEGOTIATION_STATE",
    0xA0: "CALIBRATION_STATE",
    0xB0: "POWER_TRANSFER_STATE",
    0xC0: "POWER_PID_STATE",
}

AFE_PWM_BRIDGE_NO_CONFIG = 0
AFE_PWM_BRIDGE_HALF = 1
AFE_PWM_BRIDGE_FULL = 2
AFE_PWM_BRIDGE_FULL_SYMETRIC = 3
AFE_PWM_BRIDGE_FULL_ASYMETRIC = 4


dic_bridge_mode = {
    0 : "NO_CONFIG",
    1 : "HALF",
    2 : "FULL",
    3 : "FULL_SYMETRIC",
    4 : "FULL_ASYMETRIC",
}

#QI RX ASK PP Packet
PROPRIETARY_1 = 0x18
PROPRIETARY_2 = 0x19
#PROPRIETARY_3 = 0x28
PROPRIETARY_4 = 0x29
#PROPRIETARY_5 = 0x38
#PROPRIETARY_6 = 0x48
PROPRIETARY_7 = 0x58
PROPRIETARY_8 = 0x68
PROPRIETARY_9 = 0x78


ASK_PP_HEAD_0x18 = 0x18
ASK_PP_HEAD_0x19 = 0x19
ASK_PP_HEAD_0x29 = 0x29
ASK_PP_HEAD_0x58 = 0x58
ASK_PP_HEAD_0x68 = 0x68
ASK_PP_HEAD_0x78 = 0x78

FSK_PP_HEAD_0x1E = 0x1E
FSK_PP_HEAD_0x1F = 0x1F
FSK_PP_HEAD_0x2E = 0x2E
FSK_PP_HEAD_0x2F = 0x2F
FSK_PP_HEAD_0x3F = 0x3F
FSK_PP_HEAD_0x4F = 0x4F
FSK_PP_HEAD_0x5F = 0x5F
FSK_PP_HEAD_0x6F = 0x6F
FSK_PP_HEAD_0x7F = 0x7F

#QI TX FSK PP Packet
#< Even Proprietary data wit packet size 1
QI_FSK_HDR_PROP_EVEN1         = 0x1E
#< Odd Proprietary data wit packet size 1
QI_FSK_HDR_PROP_ODD1          = 0x1F
#< Even Proprietary data wit packet size 2
QI_FSK_HDR_PROP_EVEN2         = 0x2E
#< Odd Proprietary data wit packet size 2
QI_FSK_HDR_PROP_ODD2          = 0x2F
#< Proprietary data wit packet size 3
QI_FSK_HDR_PROP_3             = 0x3F
#< Proprietary data wit packet size 4
QI_FSK_HDR_PROP_4             = 0x4F
#< Proprietary data wit packet size 5
QI_FSK_HDR_PROP_5             = 0x5F
#< Proprietary data wit packet size 6
QI_FSK_HDR_PROP_6             = 0x6F
#< Proprietary data wit packet size 7
QI_FSK_HDR_PROP_7             = 0x7F
#< Proprietary data wit packet size 9
QI_FSK_HDR_PROP_9             = 0x8F

