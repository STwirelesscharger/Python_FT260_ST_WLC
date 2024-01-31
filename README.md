# Python_FT260_ST_WLC
 use FT260 dongle and operate ST wireless charge chips


## Introduction

DB5077USB to I2C evaluation board for interfacing wireless applications with PC GUI tool
[FT260 Dongle](https://www.st.com/resource/en/data_brief/steval-usbi2cft.pdf)

UM3226 Versatile USB- I2C bridge for communication and programming of ST wireless charging IC
https://www.st.com/resource/en/user_manual/um3226-versatile-usb-i2c-bridge-for-communication-and-programming-of-st-wireless-charging-ic-stmicroelectronics.pdf


## File Introduction
driver_ft260.py is FT260 dongle python driver
wlc38_register.py is WLC38 register python driver
wlc38_register.h is WLC38 register C driver


## How to use WLC38 example code
Use python a1_wlc38_chipinfo.py to get RX chip info
Use python a2_wlc38_getadc.py to get RX ADC data
Use python a3_wlc38_sendept.py to send EPT packet to TX
