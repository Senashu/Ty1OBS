import time
import psutil
from pymem import Pymem
from pymem.process import module_from_name
from config import *

print('TyOBS Collectables Displayer v1.1.1')
print('by Buzchy')


def find_executable():
    while True:
        for proc in psutil.process_iter(['name']):
            if proc.info['name'] == 'TY.exe':
                return 'TY.exe'
            elif proc.info['name'] == 'Mul-Ty-Player.exe':
                return 'Mul-Ty-Player.exe'

        print("\nWaiting TY/MTP.exe to start")
        time.sleep(30)


def find_game_directory():
    for steam_id in os.listdir(STEAM_PATH):
        directory = os.path.join(STEAM_PATH, steam_id, GAME_ID, 'remote')
        if os.path.exists(directory):
            return directory


class TyOBS:
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

            opals = self.mem.read_int(self.opals)

            file_path = os.path.join(find_game_directory(), FILENAME)
            with open(file_path, 'rb') as f:
                hex_str = ' '.join([f'0x{x:02x}' for x in f.read()])
                TE = int(hex_str.split()[13][2:], 16)

            with open(os.path.join(self.appdata_path, "TE.txt"), "w+") as f:
                f.write(f"{TE}/{TE_VALUE}\n")

            file_path = os.path.join(find_game_directory(), FILENAME)
            with open(file_path, 'rb') as f:
                offsets = ['00000200', '00000270', '000002E0', '000003C0', '00000430', '000004A0', '00000580',
                           '000005F0', '00000660']
                cogs = 0
                for offset in offsets:
                    f.seek(int(offset, 16))
                    count = f.read(10).count(b'\x01')
                    cogs += count
                cogs_str = f"{cogs}/{COG_VALUE}\n"

                file_path = os.path.join(find_game_directory(), FILENAME)
                with open(file_path, 'rb') as f:
                    offsets1 = ['00000200', '00000270', '000002E0', '000003C0', '00000430', '000004A0', '00000580',
                                '000005F0', '00000660']
                    offsets2 = ['000001F0', '00000260', '000002D0', '000003B0', '00000420', '00000490', '00000570',
                                '000005E0', '00000650']

                    bilbies = 0
                    for offset in offsets1:
                        f.seek(int(offset, 16))
                        count1 = f.read(16)[9:16].count(b'\x01')
                        bilbies += count1
                    for offset in offsets2:
                        f.seek(int(offset, 16))
                        count2 = f.read(16)[9:16].count(b'\x01') + f.read(16)[9:16].count(b'\x03')
                        count2 -= 1 if count2 > 0 else 0
                        bilbies += count2
                    bilby_str = f"{bilbies}/{BILBY_VALUE}\n"

            with open(os.path.join(self.appdata_path, "Cog.txt"), "w+") as f:
                f.write(cogs_str)
            with open(os.path.join(self.appdata_path, "Bilby.txt"), "w+") as g:
                g.write(bilby_str)

            with open(os.path.join(self.appdata_path, "Opal.txt"), "w+") as f:
                f.write(f"{opals}/{OPAL_VALUE}\n")
            time.sleep(0.15)

    def start(self):
        self.update_values()
        print("Executable found:", psutil.process_iter(['name']))


if __name__ == '__main__':
    tyobs = TyOBS()
    tyobs.start()
