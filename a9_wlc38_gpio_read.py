import driver_ft260
from wlc38_register import *
import time
wlc38 = driver_ft260.ft260_dongle()
wlc38.chip_info()
print("example code set gpio pin as input floating and read gpio status")
print("connect external 1.8V to GPIO1")
wlc38.write16(I2CREG_GPIO0_FUNC,GPIO_FUNC_NONE_PD)
wlc38.write16(I2CREG_GPIO1_FUNC,GPIO_FUNC_NONE_PD)

value = wlc38.wreadFA(HWREG_GPIO_INPUT_VAL_RegAddr)
print(f"gpio input value 0x{value:X}")
if(value & 0x01):
    print("gpio0 input high")
else:
    print("gpio0 input low")
if(value & 0x02):
    print("gpio1 input high")
else:
    print("gpio1 input low")
