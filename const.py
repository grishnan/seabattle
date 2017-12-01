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

MFPOS = (320, 200)        # my field position on the background layer
EFPOS = (960, 200)        # enemy field position on the background layer

MND = 4                   # max number of decks (by the game)

FD         = "fonts"            # font directory
FF         = "LDFComicSans.ttf" # font file
MY_LBL     = "My field"         # label text for my field
EN_LBL     = "Enemy field"      # label text for enemy field
FONT_NAME  = "LDFComicSans"     # font name
FONT_SIZE  = 32                 # font size
MY_LBL_POS = 260, 415           # label position of my field
EN_LBL_POS = 870, 415           # label position of enemy field
FONT_COLOR = 181, 42, 163, 255  # font color

PORT  = 12345             # TCP port

##################################################
### usually, these values are changed manually ###
##################################################
EN_IP = "192.168.0.2"     # enemy IP address
MY_IP = "192.168.1.2"     # my IP address
MF = True                 # this value must be equal True for one side and False for other side

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
