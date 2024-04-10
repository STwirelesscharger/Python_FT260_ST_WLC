import driver_ft260
from wbc86_register import *
import time
wbc86 = driver_ft260.ft260_dongle()
wbc86.chip_info()
print("example code for STWBC86 to control external GPIO/LED")
print("GPIO0 connect LED Red, GPIO1 connect LED Green")

def LED_RED_CTL(isOn = True):
    if(isOn):
        wbc86.write16(I2CREG_GPIO0_FUNC,GPIO_FUNC_PP_LO)
    else:
        wbc86.write16(I2CREG_GPIO0_FUNC,GPIO_FUNC_PP_HI)

def LED_GREEN_CTL(isOn = True):
    if(isOn):
        wbc86.write16(I2CREG_GPIO1_FUNC,GPIO_FUNC_PP_LO)
    else:
        wbc86.write16(I2CREG_GPIO1_FUNC,GPIO_FUNC_PP_HI)

def LED_CTL_Example1():
    print("MCU read tx ept reason")
    ept_reason = wbc86.wread16(I2CREG_TX_EPT_REASON_RCVD,3)
    if(ept_reason[0] != 0) | (ept_reason[1] != 0) | (ept_reason[2] != 0):
        print("tx have some error set LED RED ON")
        LED_RED_CTL(True)
    else:
        LED_RED_CTL(False)


def LED_CTL_Example2():
    print("when connecting the cable (1s or 2s) and then off")
    LED_GREEN_CTL(True)
    time.sleep(1)
    LED_GREEN_CTL(False)
