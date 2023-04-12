import os
import time
import psutil
import appdirs
from pymem import Pymem
from pymem.process import module_from_name

print('Ty Collectibles for OBS')
STEAM_PATH = r'C:\Program Files (x86)\Steam\userdata'
GAME_ID = '411960'
APPDATA_PATH = os.path.join(appdirs.user_data_dir(''), 'TyOBS')
FILENAME = 'Game 2'
TE_VALUE = 72
COG_VALUE = 10
BILBY_VALUE = 5
OPAL_VALUE = 300
EXE_NAMES = {'TY.exe', 'Mul-Ty-Player.exe'}
COGS_OFFSET, BILBY_OFFSET, OPALS_OFFSET = 0x265260, 0x2651AC, 0x2888B0


def find_executable():
    while True:
        for proc in psutil.process_iter(['name']):
            if proc.info['name'] == 'TY.exe':
                return 'TY.exe'
            elif proc.info['name'] == 'Mul-Ty-Player.exe':
                return 'Mul-Ty-Player.exe'

        print("Executable not found. Waiting for it to start...")
        time.sleep(10)


def find_game_directory():
    for steam_id in os.listdir(STEAM_PATH):
        directory = os.path.join(STEAM_PATH, steam_id, GAME_ID, 'remote')
        if os.path.exists(directory):
            return directory


class TyReader:
    def __init__(self):
        self.mem = None
        self.module = None
        self.cogs = None
        self.bilby = None
        self.opals = None
        self.appdata_path = APPDATA_PATH

    def open_process(self):
        try:
            exe_name = find_executable()
            if exe_name is None:
                return False
            self.mem = Pymem(exe_name)
            self.module = module_from_name(self.mem.process_handle, exe_name).lpBaseOfDll
            self.cogs, self.bilby, self.opals = map(lambda x: self.module + x,
                                                    (COGS_OFFSET, BILBY_OFFSET, OPALS_OFFSET))
            return True
        except:
            return False

    def update_values(self):
        while True:
            while not self.open_process():
                print("\nExecutable not found. Waiting for it to start...")
                time.sleep(10)

            file_path = os.path.join(find_game_directory(), FILENAME)
            with open(file_path, 'rb') as f:
                hex_str = ' '.join([f'0x{x:02x}' for x in f.read()])
                TE = int(hex_str.split()[13][2:], 16)

            cogs = self.mem.read_int(self.cogs)
            bilby = self.mem.read_int(self.bilby)
            opals = self.mem.read_int(self.opals)

            os.makedirs(self.appdata_path, exist_ok=True)
            with open(os.path.join(self.appdata_path, "Opal.txt"), "w+") as f:
                f.write(f"{opals}/{OPAL_VALUE}\n")
            with open(os.path.join(self.appdata_path, "Cog.txt"), "w+") as f:
                f.write(f"{cogs}/{COG_VALUE}\n")
            with open(os.path.join(self.appdata_path, "Bilby.txt"), "w+") as f:
                f.write(f"{bilby}/{BILBY_VALUE}\n")
            with open(os.path.join(self.appdata_path, "TE.txt"), "w+") as f:
                f.write(f"{TE}/{TE_VALUE}\n")

            time.sleep(0.2)
            if not psutil.pid_exists(self.mem.process_id):
                break

    def start(self):
        self.update_values()


if __name__ == '__main__':
    ty_reader = TyReader()
    ty_reader.start()
    
