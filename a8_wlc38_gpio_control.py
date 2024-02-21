import driver_ft260
from wlc38_register import *
import time
wlc38 = driver_ft260.ft260_dongle()
wlc38.chip_info()
print("example code set gpio0 pin od high")
wlc38.write16(I2CREG_GPIO0_FUNC,GPIO_FUNC_OD_HI)
time.sleep(1)
print("example code set gpio0 pin od low")
wlc38.write16(I2CREG_GPIO0_FUNC,GPIO_FUNC_OD_LO)
time.sleep(1)

print("example code set gpio0 pin pp high")
wlc38.write16(I2CREG_GPIO0_FUNC,GPIO_FUNC_PP_HI)
time.sleep(1)
print("example code set gpio0 pin pp low")
wlc38.write16(I2CREG_GPIO0_FUNC,GPIO_FUNC_PP_LO)

