import os
import time
import psutil
from pymem import Pymem
from pymem.process import module_from_name

for proc in psutil.process_iter(['name']):
    if proc.info['name'] == 'TY.exe':
        exe_name = 'TY.exe'
        break
    elif proc.info['name'] == 'Mul-Ty-Player.exe':
        exe_name = 'Mul-Ty-Player.exe'
        break


steampath = r'C:\Program Files (x86)\Steam\userdata'
game_id = '411960'

for steam_id in os.listdir(steampath):
    directory = os.path.join(steampath, steam_id, game_id, 'remote')
    if os.path.exists(directory):
        print(f"Path to Game2 through SteamID:{steam_id}")
        break
else:
    print(f"Error: no Steam accounts found with game ID {game_id}")


class TyReader:
    def __init__(self):
        self.mem = None
        self.module = None
        self.Cogs = None
        self.bilby = None
        self.opals = None

    def open_process(self):
        try:
            self.mem = Pymem(exe_name)
            self.module = module_from_name(self.mem.process_handle, exe_name).lpBaseOfDll
            self.Cogs = self.module + 0x265260
            self.bilby = self.module + 0x2651AC
            self.opals = self.module + 0x2888B0
            return True
        except:
            return False

    def update_values(self, te_value=72):
        while True:
            while not self.open_process():
                print("\nTY.exe or Mul-ty-player.exe not found.")
                print("Waiting for it to start...")
                print("If you swapped between version, please restart this script\n")
                time.sleep(10)

            filename = 'Game 2'
            file_path = os.path.join(directory, filename)
            with open(file_path, 'rb') as f:
                file_contents = f.read()

            hex_str = ' '.join([f'0x{x:02x}' for x in file_contents])
            hex_14th = hex_str.split()[13]
            hex_14th = hex_14th[2:]

            TE = int(hex_14th, 16)
            Cogs = self.mem.read_int(self.Cogs)
            bilby = self.mem.read_int(self.bilby)
            opals = self.mem.read_int(self.opals)

            with open("Opal.txt", "w+") as f:
                f.write(f"{opals}/300\n")
                f.flush()
                time.sleep(0.1)

            with open("Cog.txt", "w+") as f:
                f.write(f"{Cogs}/10\n")
                f.flush()
                time.sleep(0.2)

            with open("Bilby.txt", "w+") as f:
                f.write(f"{bilby}/5\n")
                f.flush()
                time.sleep(0.2)

            with open("TE.txt", "w+") as f:
                f.write(f"{TE}/{te_value}\n")
                f.flush()
                time.sleep(0.2)

    def start(self, te_value=72):
        self.update_values(te_value)


if __name__ == '__main__':
    ty_reader = TyReader()
    ty_reader.start(te_value=72)  # 100% = 72, Any% = 34
