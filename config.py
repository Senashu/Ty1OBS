import os
import appdirs

STEAM_PATH = r'C:\Program Files (x86)\Steam\userdata'
GAME_ID = '411960'
APPDATA_PATH = os.path.join(appdirs.user_data_dir(''), 'TyOBS')
FILENAME = 'Game 2'
TE_VALUE = 72
COG_VALUE = 90
BILBY_VALUE = 45
OPAL_VALUE = 300
EXE_NAMES = {'TY.exe', 'Mul-Ty-Player.exe'}
COGS_OFFSET, BILBY_OFFSET, OPALS_OFFSET = 0x265260, 0x2651AC, 0x2888B0
