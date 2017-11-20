#!/usr/bin/env python

from const import *
import cocos as c

class MainWindow(c.layer.ColorLayer):
    ''' Main program window  '''

    def __init__(self, BG):
        super(MainWindow, self).__init__(*BG)

c.director.director.init(*SZ, caption = CP)

wdw = MainWindow(BG)
scn = c.scene.Scene(wdw)

c.director.director.run(scn)

