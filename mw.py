import os 
import cocos as c
from const import *

class Field(c.layer.Layer):
    ''' Field layer '''
    def __init__(self, pic, pos):
        super(Field, self).__init__()

        field = c.sprite.Sprite(os.path.join(SD, pic), position = pos)
        self.add(field)

class MainWindow(c.layer.ColorLayer):
    ''' Main program window  '''

    def __init__(self, BG):
        super(MainWindow, self).__init__(*BG)
    
def main():
    c.director.director.init(*SZ, caption = CP)

    wdw = MainWindow(BG)
    mf = Field(FPIC, (SZ[0]//4, SZ[1]//2))
    ef = Field(FPIC, (3*SZ[0]//4, SZ[1]//2))

    scn = c.scene.Scene(wdw, mf, ef)

    c.director.director.run(scn)

