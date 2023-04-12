import os
import time
from pymem import Pymem
from pymem.process import module_from_name


class TyReader:
    def __init__(self):
        self.mem = Pymem("Mul-Ty-Player.exe")
        self.module = module_from_name(self.mem.process_handle, "Mul-Ty-Player.exe").lpBaseOfDll
        self.CogCounter = self.module + 0x265260
        self.BilbyCounter = self.module + 0x2651AC
        self.OpalCounter = self.module + 0x2888B0

    def update_values(self):
        while True:
            directory = r'C:\Program Files (x86)\Steam\userdata\80222993\411960\remote'
            filename = 'Game 2'
            file_path = os.path.join(directory, filename)
            with open(file_path, 'rb') as f:
                file_contents = f.read()

            hex_str = ' '.join([f'0x{x:02x}' for x in file_contents])
            hex_14th = hex_str.split()[13]
            hex_14th = hex_14th[2:]

            w = int(hex_14th, 16)   # add 50 to int_val

            x = self.mem.read_int(self.CogCounter)
            y = self.mem.read_int(self.BilbyCounter)
            z = self.mem.read_int(self.OpalCounter)

            # Write the values to separate files
            with open("x_value.txt", "w") as f:
                f.write(f"{x}/10\n")
            with open("y_value.txt", "w") as f:
                f.write(f"{y}/5\n")
            with open("z_value.txt", "w") as f:
                f.write(f"{z}/300\n")
            with open("w_value.txt", "w") as f:
                f.write(f"{w}/72\n")

            time.sleep(0.2)

    def start(self):
        self.update_values()


if __name__ == '__main__':
    ty_reader = TyReader()
    ty_reader.start()
