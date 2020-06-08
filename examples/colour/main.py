from xCore import xCore
from xSL06 import xSL06

# SL06 instance
SL06 = xSL06()

# configure SL06
SL06.init()

# enable SL06 for light sensing
SL06.enableLightSensor()

while True:
    red = SL06.getRedLight()        # read red light level
    green = SL06.getGreenLight()    # read green light level
    blue = SL06.getBlueLight()      # read blue light level

    print('RED   :', red)
    print('GREEN :', green)
    print('BLUE  :', blue)

    xCore.sleep(2000)