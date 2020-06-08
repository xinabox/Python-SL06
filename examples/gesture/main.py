from xCore import xCore
from xSL06 import xSL06

# SL06 instance
SL06 = xSL06()

# configure SL06
SL06.init()

# enable SL06 for gesture sensing
SL06.enableGestureSensor()

while True:
    if SL06.isGestureAvailable():   # check for gesture
        dir = SL06.getGesture()     # read direction
        print(dir)                  # print direction on console

    xCore.sleep(100)