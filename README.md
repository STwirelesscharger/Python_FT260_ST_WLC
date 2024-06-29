# Wireless charger chip script

## Requirements
This driver requires the STWLC/WBC wireless charger chip and FT260 dongle.
PC Need Microsoft Visual C++ 2010 x86 and x64 Redistributable package.
https://docs.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist?view=msvc-170

Refer to DB5077USB to I2C evaluation board for interfacing wireless applications with PC GUI tool
[FT260 Dongle](https://www.st.com/resource/en/data_brief/steval-usbi2cft.pdf)

Refer to UM3226 Versatile USB- I2C bridge for communication and programming of ST wireless charging IC
https://www.st.com/resource/en/user_manual/um3226-versatile-usb-i2c-bridge-for-communication-and-programming-of-st-wireless-charging-ic-stmicroelectronics.pdf

## Description
driver_ft260.py is FT260 dongle python driver
wlc38_register.py is WLC38 register python driver
wbc86_register.py is WBC86 register python driver
wlc98_register.py is WLC98 register python driver
wlc99_register.py is WLC99 register python driver

## How to use WLC38 example code
Use python ax_wlc38_xx.py and TX use STWBC86

## How to use WBC86 example code
Use python bx_wbc86_xx.py and RX use STWLC38

## How to use WLC98 example code
Use python cx_wlc98_xx.py and TX use STWBC2

## How to use WLC99 example code
Use python dx_wlc99_xx.py and TX use STWBC2
