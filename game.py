import os.path 
import cocos as c
from const import *

class Field(c.layer.Layer):
    ''' Field layer '''
    
    def __init__(self, pic, pos):
        super(Field, self).__init__()

        field = c.sprite.Sprite(os.path.join(SD, pic), position = pos)
        self.add(field)

class Background(c.layer.ColorLayer):
    ''' Background layer  '''

    # the event handlers of this layer will be registered
    is_event_handler = True 

    def __init__(self, BG):
        super(Background, self).__init__(*BG)

        self.posx, self.posy = 0, 0 # inital mouse coordinates

    def on_mouse_press(self, x, y, buttons, modifiers):
        ''' Mouse handler '''
        self.posx, self.posy = c.director.director.get_virtual_coordinates(x, y)
        print(self.posx, self.posy)
    
def main():
    c.director.director.init(*SZ, caption = CP)

    bg = Background(BG)
    mf = Field(FPIC, MFPOS)
    ef = Field(FPIC, EFPOS)

    scn = c.scene.Scene(bg, mf, ef)

    c.director.director.run(scn)
