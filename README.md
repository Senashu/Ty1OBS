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
4. Paste the code in the cmd and press Enter

## Usage
 
1. Open "Ty" or "Mul-ty-player" and minimize it
2. Run the script. ( If it closes, it means PIP is not installed.)
2. The script will create a Folder called "TyOBS" in %LocalAppData%. (Type in the Explorer Address Bar %LocalAppData% to locate it)
3. There, you will find the "TyOBS" folder.
4. Open OBS and go to Tools -> Scripts-> Now add main.py to "Loaded Scripts" by pressing "+"
5. After that you go to -> Python Settings ->click Browse and search for -> "C:\Users\*****\AppData\Local\Programs\Python\Python310"
7. Now you can add a source called "Text (GDI+)" and name it, for example "TE_Text".
8. Right-click on "TE_Text" and select "Properties".
9. Choose "Read from file".
10. Browse for "TE.txt". The script will create the file where you opened it.
11. Repeat it for the other called Cog.txt, Opal.txt, TE.txt


## Customization

You can customize value by passing a different value after `=`. For example, to set the TE value to 69, use:

```TE_VALUE = 72```
```python
FILENAME can be changed to 'Game 1', 'Game 2', 'Game 3'.
TE_VALUE can be changed to 34 for Any%. #default 72 for 100%
COG_VALUE representing the maximum Cogs of the Level.
BILBY_VALUE representing the maximum Bilby of the Level.
OPAL_VALUE representing the maximum Opals of the Level, which can be turn in to a Opal machine for a TE reward.
```
