import os.path 
import cocos as c
from const import *

class Field(c.layer.Layer):
    ''' Field layer '''
    
    def __init__(self, pic, pos):
        super(Field, self).__init__()

        field = c.sprite.Sprite(os.path.join(SD, pic), position = pos)
        self.add(field)




class MyField(Field):
    ''' My field layer '''

    def __init__(self, pic, pos):
        super(MyField, self).__init__(pic, pos)


class EnemyField(Field):
    ''' Enemy field layer '''
    
    # the event handlers of this layer will be registered
    is_event_handler = True

    def __init__(self, pic, pos):
        super(EnemyField, self).__init__(pic, pos)
        self.posx, self.posy = 0, 0 # initial mouse coordinates

    def on_mouse_press(self, x, y, buttons, modifiers):
        ''' Mouse handler '''
        self.posx, self.posy = c.director.director.get_virtual_coordinates(x, y)

        if EFRUC[0]-SF < self.posx < EFRUC[0] and EFRUC[1]-SF < self.posy < EFRUC[1]:
            cell = self.virtual_crd_to_cell_crd()
                
    def virtual_crd_to_cell_crd(self):
        ''' Virtual coordinates map to cell coordinates '''
        pass

class Background(c.layer.ColorLayer):
    ''' Background layer  '''

    def __init__(self, BG):
        super(Background, self).__init__(*BG)


def main():
    c.director.director.init(*SZ, caption = CP)

    bg = Background(BG)
    mf = MyField(FPIC, MFPOS)
    ef = EnemyField(FPIC, EFPOS)

    scn = c.scene.Scene(bg, mf, ef)

    c.director.director.run(scn)
