#############################
### independent constants ###
#############################
BG = (244, 180, 180, 255) # background color
SZ = (1280, 480)          # window's size
CP = "Sea battle"         # window's caption

SD = "sprite"             # sprite directory

FPIC = "f.png"            # field picture
DPIC = "d.png"            # deck of a ship
MPIC = "m.png"            # miss picture
HPIC = "h.png"            # hit picture
CPIC = "c.png"            # cross picture

MFPOS = (320, 240)        # my field position on the background layer
EFPOS = (960, 240)        # enemy field position on the background layer

MND = 4                   # max number of decks (by the game)

EN_IP = "192.168.0.2"     # enemy IP address
MY_IP = "192.168.0.1"     # my IP address
PORT  = 12345             # TCP port

#########################################################################
### these values are depended on the field picture, don't change them ###
#########################################################################
SFL = 390                 # field layer size in pixels
SF  = 355                 # field size in pixels
SC  = 30                  # cell size in pixels
SB  = 5                   # border size in pixels

###########################
### dependent constants ###
###########################

EFRUC = (EFPOS[0] + SFL // 2, EFPOS[1] + SFL // 2) # right upper corner of enemy field
MFRUC = (MFPOS[0] + SFL // 2, MFPOS[1] + SFL // 2) # right upper corner of my field
