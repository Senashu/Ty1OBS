# Ty1 Collectables for OBS

Ty1 Collectables is a Python script that reads memory values from the Game "TY.exe" or "Mul-Ty-Player.exe" and writes them to text files. The values that are read include the number of Cogs, Bilbies, Opals, and TE that the player has collected in the game. 

## Getting Started

### Prerequisites

To run this script, you will need:
* Python 3.x
* Pymem, Psutil and appdirs library

### Installation


1. Press Windows + r:
2. Type cmd
3. Copy the code below
```sh
pip install psutil appdirs pymem
```
4.Paste the code in the cmd and press Enter

## Usage
 
1. Open "Ty" or "Mul-ty-player" and minimize it
2. Run the script. ( If it closes, it means PIP is not installed.)
2. The script will create a Folder called "TyOBS" in %LocalAppData%. (Type in the Explorer Address Bar %LocalAppData% to locate it)
3. There you'll find the "TyOBS" Folder
4. Open OBS and go to Tools ->python settings ->add "C:\Users\*****\AppData\Local\Programs\Python\Python310"
5. Go back to Scripts and add script main.py
6. Now you can add a source called "Text (GDI+)" and name it, for example "TE_Text".
7. Right-click on "TE_Text" and select "Properties".
8. Choose "Read from file".
9. Browse for "TE.txt". The script will create the file where you opened it.
10. Repeat it for the other called Cog.txt, Opal.txt, TE.txt


## Customization

You can customize the TE value by passing a different value to the `start()` method. For example, to set the TE value to 72, use:
```python
ty_reader.start(te_value=72)
```
