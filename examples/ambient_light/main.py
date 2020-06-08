from xCore import xCore
from xSL06 import xSL06

# SL06 instance
SL06 = xSL06()

# configure SL06
SL06.init()

# enable SL06 for light sensing
SL06.enableLightSensor()

while True:
    light = SL06.getAmbientLight()  # read the the ambient light level
    print('Ambient Light Level: ', light)

    xCore.sleep(2000)
