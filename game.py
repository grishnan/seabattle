import os 
import cocos as c
from const import *

class Field(c.layer.Layer):
    ''' Field layer '''
    def __init__(self, pic, pos):
        super(Field, self).__init__()

        field = c.sprite.Sprite(os.path.join(SD, pic), position = pos)
        self.add(field)

class BgLayer(c.layer.ColorLayer):
    ''' Background layer  '''

    def __init__(self, BG):
        super(BgLayer, self).__init__(*BG)
    
def main():
    c.director.director.init(*SZ, caption = CP)

    bg = BgLayer(BG)
    mf = Field(FPIC, MFPOS)
    ef = Field(FPIC, EFPOS)

    scn = c.scene.Scene(bg, mf, ef)

    c.director.director.run(scn)

