from __future__ import print_function
import os
import argparse
import sys

version = sys.version_info[0]

ap = argparse.ArgumentParser()
ap.add_argument("-p", "--path", required=True, help="path to directory to clean up")
ap.add_argument("-x", "--ext", nargs='+', required=True, help="list of extensions separated by a semicolon")
ap.add_argument("-m", "--mode", type=str, default="keep", help="keep or remove the extensions")

args = vars(ap.parse_args())

path = args["path"]
extensions = args["ext"]
mode = args["mode"]

deleteFiles = []

for (folder, directory, fileNames) in os.walk(path):
    if mode == "keep":
        for fileName in fileNames:
            if any(ext in fileName for ext in extensions):
                    continue
            deleteFiles.append(os.path.join(folder, fileName).replace(" ", "\\ "))
    elif mode == "remove":
        for fileName in fileNames:
            if any(ext in fileName for ext in extensions):
                deleteFiles.append(os.path.join(folder, fileName).replace(" ", "\\ "))

for item in deleteFiles:
    print("[INFO] deleting file {}".format(item))
    os.remove(item)
