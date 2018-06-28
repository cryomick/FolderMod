# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at

#   http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

import os
import argparse

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
    print "[INFO] deleting file {}".format(item)
    os.remove(item)
