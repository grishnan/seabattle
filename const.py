#############################
### independent constants ###
#############################

BG = (244, 180, 180, 255) # background color
SZ = (1280, 480)          # window's size
CP = "Sea battle"         # window's caption

SD = "sprite"             # sprite directory

FPIC = "f.png"            # field picture
PPIC = "p.png"            # part of a ship picture
MPIC = "m.png"            # miss picture
DPIC = "d.png"            # destroy picture

MFPOS = (320, 240)        # my field position
EFPOS = (960, 240)        # enemy field position

SFL = 390                 # field layer size in pixels (don't change this value) 
SF = 355                  # field size in pixels (don't change this value)

###########################
### dependent constants ###
###########################

EFRUC = (EFPOS[0] + SFL // 2, EFPOS[1] + SFL // 2) # right upper corner of the enemy field
