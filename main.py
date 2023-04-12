import os
import time
from pymem import Pymem
from pymem.process import module_from_name


class TyReader:
    def __init__(self):
        self.mem = Pymem("Mul-Ty-Player.exe")
        self.module = module_from_name(self.mem.process_handle, "Mul-Ty-Player.exe").lpBaseOfDll
        self.Cogs = self.module + 0x265260
        self.bilby = self.module + 0x2651AC
        self.opals = self.module + 0x2888B0

    def update_values(self, te_value=72):
        while True:
            directory = r'C:\Program Files (x86)\Steam\userdata\80222993\411960\remote'
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
                time.sleep(0.01)

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
