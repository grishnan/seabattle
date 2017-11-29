import os.path 
import cocos as c
from const import *
from random import randint as rnd
from random import shuffle as shf
from socket import *
import threading

class Background(c.layer.ColorLayer):
    ''' Background layer  '''

    def __init__(self, BG):
        super(Background, self).__init__(*BG)

class Field(c.layer.Layer):
    ''' Field layer '''

    # For normal process of game it's important
    # to define who will be doing the first move.
    # At the start of the game it's undefined.
    # Therefore moveflag is equal None for every player and
    # both sides must agree about primacy before the game.
    # In other words moveflag must be equal True for one side
    # and must be equal False for another side at the start of the game.
    moveflag = None
    
    def __init__(self, pic, pos):
        super(Field, self).__init__()

        layer = c.sprite.Sprite(os.path.join(SD, pic), position = pos)
        self.add(layer)
        
    def _cell_crd_to_virtual_crd(self, cell):
        ''' Cell coordinates map to virtual coordinates of the field '''
        x = (MFRUC[0]-SF) + (cell[0]+1)*SB + cell[0]*SC + SC//2
        y = (MFRUC[1]-SF) + (cell[1]+1)*SB + cell[1]*SC + SC//2
        return x, y
        
class MyField(Field):
    ''' My field layer '''

    def __init__(self, pic, pos):
        super(MyField, self).__init__(pic, pos)
        
        self.ships = {}  # ships of my field
        self.gen_ships() # generate ships

        # set up server
        self.sock = socket(AF_INET, SOCK_STREAM)
        self.sock.bind((MY_IP, PORT))
        self.sock.listen(1)

    def gen_ships(self):
        ''' Generate ships on my field '''
        names = iter([i for i in range(0, 10)]) # names of ships
        for nd in range(MND, 0, -1):
            for ns in range(1, 6-nd):
                self._gen_ship(nd, next(names))
        self.draw_ships() # drawing ships
        
    def _gen_ship(self, nd, name):
        ''' Generate one nd-decked ship '''
        is_gen = False
        while not is_gen:
            # get random cell of the field
            fi, fj = rnd(0, 9), rnd(0, 9)
            # list of possible directions for ship creating
            directlist = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            shf(directlist)
            # try to build a ship in one of some different directions
            for direct in directlist:
                li, lj = fi + nd*direct[0], fj + nd*direct[1]
                # if last deck of a ship is on the field
                if 0 <= li <= 9 and 0 <= lj <= 9:
                    # try to build a ship
                    ship = {}
                    for d in range(0, nd):
                        di, dj = fi + d*direct[0], fj + d*direct[1]
                        ship[(di, dj)] = False
                    # check collision between a ship and other ships   
                    if self._is_collision(ship):
                        continue # if collision is detected then go to next direction
                    else:
                        self.ships[name] = ship # add ship to the self.ships
                        is_gen = True           # generation is finished
                        break                   # exit from loop 

    def _is_collision(self, ship):
        ''' Is there a collision between a ship and others ships '''
        collision = False
        for name_other_ship in self.ships:
            if self._get_distance_ships(ship, name_other_ship) < 2:
                collision = True
                break
        return collision

    def _get_distance_ships(self, ship, name_other_ship):
        ''' Get distance between two ships '''
        fir_ship = ship
        sec_ship = self.ships[name_other_ship]
        distances = []
        for cfs in fir_ship:
            for css in sec_ship:
                distances.append(self._get_distance_cells(cfs, css))
        return min(distances)

    def _get_distance_cells(self, fir_cell, sec_cell):
        ''' Get distance between two cells '''
        return abs(fir_cell[0] - sec_cell[0]) + abs(fir_cell[1] - sec_cell[1])
    
    def draw_ships(self):
        ''' Drawing ships '''
        for ship in self.ships:
            for cell in self.ships[ship]:
                x, y = self._cell_crd_to_virtual_crd(cell)
                self.add(c.sprite.Sprite(os.path.join(SD, HPIC), position = (x, y)))
                self.add(c.sprite.Sprite(os.path.join(SD, DPIC), position = (x, y)), name = str(cell))
                
    def receive_cell(self):
        ''' Receive cell '''
        while True:
            conn, address = self.sock.accept()
            data = conn.recv(2)
            # define the target of hit
            cell = int(data.decode()[0]), int(data.decode()[1])
            
            # To know: hit or miss
            is_hit = False
            for ns in self.ships:
                if cell in self.ships[ns]:
                    if not self.ships[ns][cell]:     # if the target isn't destroyed yet
                        is_hit = True
                        self.ships[ns][cell] = True  # to fix hit
                    break
            
            if is_hit:
                conn.send(b'1') # if target is hit then send to enemy b'1'
                self.remove(str(cell))
            else:
                Field.moveflag = True # has right of move
                conn.send(b'0') # if miss then send to enemy b'0'
            conn.close()

class EnemyField(Field):
    ''' Enemy field layer '''
    
    # the event handlers of this layer will be registered
    is_event_handler = True

    def __init__(self, pic, pos):
        super(EnemyField, self).__init__(pic, pos)
        
        # history of shots
        self.shots = set()

    def on_mouse_press(self, x, y, buttons, modifiers):
        ''' Mouse handler '''
        posx, posy = c.director.director.get_virtual_coordinates(x, y)

        # if enemy field is clicked
        if EFRUC[0]-SF < posx < EFRUC[0] and EFRUC[1]-SF < posy < EFRUC[1]:
            # get cell coordinates by mouse coordinates
            cell = self._virtual_crd_to_cell_crd(posx, posy)
            if cell != None:
                if Field.moveflag: # if a player has right of move
                    # send the clicked cell to enemy side
                    self.send_cell(cell)
                
    def _virtual_crd_to_cell_crd(self, posx, posy):
        ''' Virtual coordinates map to cell coordinates of the field '''
        dx = posx - EFRUC[0] + SF
        dy = posy - EFRUC[1] + SF
        cell = None
        if SB < dx % (SC+SB) < SC+SB and SB < dy % (SC+SB) < SC+SB:
            cell = (int(dx // (SC+SB)), int(dy // (SC+SB)))
        return cell
    
    def send_cell(self, cell):
        ''' Send cell '''
        sock = socket(AF_INET, SOCK_STREAM)
        sock.connect((EN_IP, PORT))
        target = str(cell[0]) + str(cell[1])
        sock.send(str.encode(target)) # send a target of shot to enemy
        info = sock.recv(1) # get result (1 byte is enough: b'1' or b'0')
        
        x, y = self._cell_crd_to_virtual_crd(cell)
        d = EFRUC[0] - MFRUC[0]
        if info == b'1':
            self.add(c.sprite.Sprite(os.path.join(SD, CPIC), position = (x + d, y)))
        else:
            if cell not in self.shots:
                Field.moveflag = False # to deny to move
                self.add(c.sprite.Sprite(os.path.join(SD, MPIC), position = (x + d, y)))
        
        self.shots.add(cell) # add cell to history of shots
        sock.close()

def main():
    c.director.director.init(*SZ, caption = CP)

    bg = Background(BG)
    mf = MyField(FPIC, MFPOS)
    ef = EnemyField(FPIC, EFPOS)

    # run server
    t = threading.Thread(target = mf.receive_cell)
    t.start()

    # create scene
    scn = c.scene.Scene(bg, mf, ef)

    # run Main Loop
    c.director.director.run(scn)
