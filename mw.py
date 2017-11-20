import os 
import cocos as c
from const import *

class MainWindow(c.layer.ColorLayer):
    ''' Main program window  '''

    def __init__(self, BG):
        super(MainWindow, self).__init__(*BG)
    
        # my field
        mf = c.sprite.Sprite(os.path.join(SD, FPIC), position = (SZ[0]//4, SZ[1]//2))
        # enemy field
        ef = c.sprite.Sprite(os.path.join(SD, FPIC), position = (3*SZ[0]//4, SZ[1]//2))

        self.add(mf)
        self.add(ef)

def main():
    c.director.director.init(*SZ, caption = CP)

    wdw = MainWindow(BG)
    scn = c.scene.Scene(wdw)

    c.director.director.run(scn)

