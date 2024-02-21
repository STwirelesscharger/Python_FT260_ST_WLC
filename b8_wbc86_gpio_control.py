import driver_ft260
from wbc86_register import *
import time
wbc86 = driver_ft260.ft260_dongle()
wbc86.chip_info()
print("example code set gpio6/intb pin high")
wbc86.write16(I2CREG_GPIO6_FUNC,GPIO_FUNC_PP_HI)
time.sleep(1)
print("example code set gpio6/intb pin low")
wbc86.write16(I2CREG_GPIO6_FUNC,GPIO_FUNC_PP_LO)