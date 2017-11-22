import os.path 
import cocos as c
from const import *
from random import randint as rnd
from random import shuffle as shf

class Field(c.layer.Layer):
    ''' Field layer '''
    
    def __init__(self, pic, pos):
        super(Field, self).__init__()

        layer = c.sprite.Sprite(os.path.join(SD, pic), position = pos)
        self.add(layer)

        # generate empty field (without ships) 
        field = {(i, j): False for i in range(0, 10) for j in range(0, 10)}
        

class MyField(Field):
    ''' My field layer '''

    def __init__(self, pic, pos):
        super(MyField, self).__init__(pic, pos)
        self._gen_ships()

    def _gen_ships(self):
        ''' Generate ships on my field '''

        for nd in range(MND, 0, -1):
            for ns in range(1, 6-nd):
                self._gen_ship(nd)

    def _gen_ship(self, nd):
        ''' Generate one nd-decked ship '''
        is_gen = False
        while not is_gen:
            fi, fj = rnd(0, 9), rnd(0, 9)
            directlist = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            shf(directlist)
            for direct in directlist:
                li, lj = fi + nd*direct[0], fj + nd*direct[1]
                if 0 <= li <= 9 and 0 <= lj <= 9:
                    for d in range(0, nd):
                        di, dj = fi + d*direct[0], fj + d*direct[1]
                        x = (MFRUC[0]-SF) + (di+1)*SB + di*SC + SC//2
                        y = (MFRUC[1]-SF) + (dj+1)*SB + dj*SC + SC//2
                        deck = c.sprite.Sprite(os.path.join(SD, PPIC), position = (x, y))
                        self.add(deck)
                    is_gen = True
                    break

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

        # if enemy field is clicked
        if EFRUC[0]-SF < self.posx < EFRUC[0] and EFRUC[1]-SF < self.posy < EFRUC[1]:
            # get cell coordinates by mouse coordinates
            cell = self.virtual_crd_to_cell_crd()
            if cell != None:
                print(cell)
                # TODO send cell by network
                
    def virtual_crd_to_cell_crd(self):
        ''' Virtual coordinates map to cell coordinates of the field '''
        dx = self.posx - EFRUC[0] + SF
        dy = self.posy - EFRUC[1] + SF
        cell = None
        if SB < dx % (SC+SB) < SC+SB and SB < dy % (SC+SB) < SC+SB:
            cell = (int(dx // (SC+SB)), int(dy // (SC+SB)))
        return cell

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
