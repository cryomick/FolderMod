# FolderMod
Python script that allows user to modify the contents of a folder. The user can provide file extensions and can choose whether to keep or remove them.

## Prerequisites
* Python 2.x

## Installation
Just download the script. Easy as that!

## Usage
The script recursively goes through the root directory to find all the files and compares it with the file extensions provided by the user. Based on the mode - keep or remove - the script will either keep only those extensions and delete the rest or vice versa.
```
Usage: python folderMod.py [options] arg_name
  options:
    -p, --path required  absolute path to the folder
    -m, --mode           operation mode : keep/remove (defaut is keep)
    -x, --ext  required  list of extensions
    
  sample:
    python folderMod.py --path C:\TEST\FOLDER --mode remove --ext .mp4 .txt .doc
```
