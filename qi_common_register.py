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

EPT_UNKNOWN                 = 0x00,             #///< Unknown (No specific/appropriate code)
EPT_CHARGE_COMPLETE         = 0x01,             #///< Charge Complete (Charge full)
EPT_INTERNAL_FAULT          = 0x02,             #///< Internal Fault (Rx software or logic error)
EPT_OVER_TEMP               = 0x03,             #///< Over Temperature (Rx device over temperature)
EPT_OVER_VOLTAGE            = 0x04,             #///< Over Voltage (Rx device over voltage)
EPT_OVER_CURRENT            = 0x05,             #///< Over Current (Rx device over current)
EPT_BAT_FAILURE             = 0x06,             #///< Battery Failure (Rx device battery problem)
EPT_UNDER_VOLTAGE           = 0x07,             #///< Under Voltage (Rx device vout under voltage)
EPT_NO_RESPONSE             = 0x08,             #///< No Response (Tx not adjusting according to CE)
EPT_RESERVED1               = 0x09,             #///< Reserved
EPT_NEGO_FAIL               = 0x0A,             #///< Negotiation Failure (EPP, no suitable GP)
EPT_RESTART_POWER_TRANSFER  = 0x0B,             #///< Restart Power Transfer (EPP, start no power transfer FOD)

#define QI_ASK_HDR_SS                 (0x01)                ///< Signal Strength header value
#define QI_ASK_HDR_EPT                (0x02)                ///< End Power Transfer header value
#define QI_ASK_HDR_CE                 (0x03)                ///< Control Error header value
#define QI_ASK_HDR_RP8                (0x04)                ///< 8-bit Received Power header value
#define QI_ASK_HDR_CHS                (0x05)                ///< Charge Status header value
#define QI_ASK_HDR_PCH                (0x06)                ///< Power Control Hold-off header value
#define QI_ASK_HDR_GRQ                (0x07)                ///< General Request header value
#define QI_ASK_HDR_RN                 (0x09)                ///< Re-negotiate header value
#define QI_ASK_HDR_SRQ                (0x20)                ///< Specific Request header value
#define QI_ASK_HDR_FOD                (0x22)                ///< FOD Status header value
#define QI_ASK_HDR_RP24               (0x31)                ///< 24-bit Received Power header value
#define QI_ASK_HDR_CFG                (0x51)                ///< Configuration header value
#define QI_ASK_HDR_WPID_MSB           (0x54)                ///< WPID MSB header value
#define QI_ASK_HDR_WPID_LSB           (0x55)                ///< WPID LSB header value
#define QI_ASK_HDR_ID                 (0x71)                ///< Identification header value
#define QI_ASK_HDR_XID                (0x81)                ///< Extended Identification header value
#define QI_ASK_HDR_BC_ACK             (0x18)                ///< Proprietary BC ACK header value

#define QI_ASK_HDR_NULL               (0x00)                ///< Data Not Available Response (size = 1)
#define QI_ASK_HDR_ADC                (0x25)                ///< Auxiliary Data Control
#define QI_ASK_HDR_DSR                (0x15)                ///< Auxiliary Data Control
#define QI_ASK_HDR_ADT_EVEN1          (0x16)                ///< Even Auxiliary Data Transport with packet size 1
#define QI_ASK_HDR_ADT_ODD1           (0x17)                ///< Odd Auxiliary Data Transport with packet size 1
#define QI_ASK_HDR_ADT_EVEN2          (0x26)                ///< Even Auxiliary Data Transport with packet size 2
#define QI_ASK_HDR_ADT_ODD2           (0x27)                ///< Odd Auxiliary Data Transport with packet size 2
#define QI_ASK_HDR_ADT_EVEN3          (0x36)                ///< Even Auxiliary Data Transport with packet size 3
#define QI_ASK_HDR_ADT_ODD3           (0x37)                ///< odd Auxiliary Data Transport with packet size 3
#define QI_ASK_HDR_ADT_EVEN4          (0x46)                ///< Even Auxiliary Data Transport with packet size 4
#define QI_ASK_HDR_ADT_ODD4           (0x47)                ///< Odd Auxiliary Data Transport with packet size 4
#define QI_ASK_HDR_ADT_EVEN5          (0x56)                ///< Even Auxiliary Data Transport with packet size 5
#define QI_ASK_HDR_ADT_ODD5           (0x57)                ///< odd Auxiliary Data Transport with packet size 5
#define QI_ASK_HDR_ADT_EVEN6          (0x66)                ///< Even Auxiliary Data Transport with packet size 6
#define QI_ASK_HDR_ADT_ODD6           (0x67)                ///< Odd Auxiliary Data Transport with packet size 6
#define QI_ASK_HDR_ADT_EVEN7          (0x76)                ///< Even Auxiliary Data Transport with packet size 7
#define QI_ASK_HDR_ADT_ODD7           (0x77)                ///< Odd Auxiliary Data Transport with packet size 7

#define QI_ASK_ADT_END_EVEN           (0x6)                 ///< Even ADT header end with '6'
#define QI_ASK_ADT_END_ODD            (0x7)                 ///< Odd ADT header end with '7'

#define QI_MSG_LEN_SS                 (1)                   ///< Signal Strength message length
#define QI_MSG_LEN_EPT                (1)                   ///< End Power Transfer message length
#define QI_MSG_LEN_CE                 (1)                   ///< Control Error message length
#define QI_MSG_LEN_RP8                (1)                   ///< 8-bit Received Power message length
#define QI_MSG_LEN_DSR                (1)                   ///< DSR message length
#define QI_MSG_LEN_CHS                (1)                   ///< Charge Status message length
#define QI_MSG_LEN_PCH                (1)                   ///< Power Control Hold-off message length
#define QI_MSG_LEN_GRQ                (1)                   ///< General Request message length
#define QI_MSG_LEN_RN                 (1)                   ///< Re-negotiate message length
#define QI_MSG_LEN_ADC                (2)                   ///< DSR message length
#define QI_MSG_LEN_SRQ                (2)                   ///< Specific Request message length
#define QI_MSG_LEN_FOD                (2)                   ///< FOD Status message length
#define QI_MSG_LEN_TXID               (3)                   ///< TX Identification packet
#define QI_MSG_LEN_TXCAP              (3)                   ///< TX Capabilities packet
#define QI_MSG_LEN_RP24               (3)                   ///< 24-bit Received Power message length
#define QI_MSG_LEN_CFG                (5)                   ///< Configuration message length
#define QI_MSG_LEN_WPID_MSB           (5)                   ///< WPID MSB message length
#define QI_MSG_LEN_WPID_LSB           (5)                   ///< WPID LSB message length
#define QI_MSG_LEN_ID                 (7)                   ///< Identification message length
#define QI_MSG_LEN_XID                (8)                   ///< Extended Identification message length
#define QI_MSG_LEN_BC_ACK             (1)                   ///< Proprietary BC ACK message length
#define QI_MSG_LEN_ADT_MAX            (0x7)                 ///< Adt packet max len