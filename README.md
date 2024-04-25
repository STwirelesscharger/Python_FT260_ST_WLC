# Python_FT260_ST_WLC
 use FT260 dongle and operate ST wireless charge chips


## Introduction
PC Need Microsoft Visual C++ 2010 x86 and x64 Redistributable package.

https://docs.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist?view=msvc-170

DB5077USB to I2C evaluation board for interfacing wireless applications with PC GUI tool
[FT260 Dongle](https://www.st.com/resource/en/data_brief/steval-usbi2cft.pdf)

UM3226 Versatile USB- I2C bridge for communication and programming of ST wireless charging IC
https://www.st.com/resource/en/user_manual/um3226-versatile-usb-i2c-bridge-for-communication-and-programming-of-st-wireless-charging-ic-stmicroelectronics.pdf


## File Introduction
driver_ft260.py is FT260 dongle python driver
wlc38_register.py is WLC38 register python driver
wlc38_register.h is WLC38 register C driver
wbc86_register.py is WBC86 register python driver
wbc86_register.h is WBC86 register C driver

## How to use WLC38 example code
Use python ax_wlc38_xx.py and TX use STWBC86
Use python a1_wlc38_chipinfo.py to get RX chip info
Use python a2_wlc38_getadc.py to get RX ADC data
Use python a3_wlc38_sendept.py to send EPT packet to TX
Use python a4_wlc38_send_recv_pp_packet.py to send pp packet to TX and get TX reply
Use python a5_wlc38_send_recv_dts_packet to send DTS packet to TX and get tx reply
Use python a6_wlc38_setvout to control RX VOUT

## How to use WBC86 example code
Use python bx_wbc86_xx.py and RX use STWLC38
Use python b1_wbc86_chipinfo.py to get TX chip info
Use python b2_wbc86_getadc.py to get TX ADC data

## How to use WLC98 example code
Use python cx_wlc98_xx.py and TX use STWBC2

## How to use WLC99 example code
Use python dx_wlc99_xx.py and TX use STWBC2
