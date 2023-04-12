# Ty1 Collectables for OBS

Ty1 Collectables is a Python script that reads memory values from the "Mul-Ty-Player.exe" and writes them to text files. The values that are read include the number of Cogs, Bilbies, Opals, and TE that the player has collected in the game. 

## Getting Started

### Prerequisites

To run this script, you will need:
* Python 3.x
* Pymem library

### Installation


1. Install the required packages:
```sh
pip install pymem
```

## Usage

1. Open the game "Mul-Ty-Player.exe".
2. Run the script:
```sh
python main.py
```
3. The script will start reading the memory values and writing them to text files (Cog.txt, Bilby.txt, Opal.txt, and TE.txt).

## Customization

You can customize the TE value by passing a different value to the `start()` method. For example, to set the TE value to 72, use:
```python
ty_reader.start(te_value=72)
```
