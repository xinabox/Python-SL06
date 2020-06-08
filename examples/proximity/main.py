from xCore import xCore
from xSL06 import xSL06

# SL06 instance
SL06 = xSL06()

# configure SL06
SL06.init()

# enable SL06 for proximity sensing
SL06.enableProximitySensor()

while True:
    prox = SL06.getProximity()  # read the proximity level
    print(prox)

    xCore.sleep(2000)
