# -*- coding: utf-8 -*-
"""
# Usage:
## Install patchutils:
brew install patchutils
## Run this code
python3 DifftoFilename.py patchid_start patchid_end DIFF_DIR > outputfile.csv

Diff file format: Patchid_patchno.diff(e.g. 190_3.diff)
"""

import sys
import os
import subprocess

ARGS = sys.argv

PATCH_START_ID = int(ARGS[1])
PATCH_END_ID = int(ARGS[2])
DIFF_DIR_PATH = ARGS[3]

# collection diff file list
FILE_LIST = [(patch_no, DIFF_DIR_PATH + str(patch_no) + "_1.txt")
             for patch_no in range(PATCH_START_ID, PATCH_END_ID)
             if os.path.isfile(DIFF_DIR_PATH + str(patch_no) + "_1.txt")]

FILE_NUM = len(FILE_LIST)

for (patch_no, FILE_NAME) in FILE_LIST:
    filenames = subprocess.Popen(["lsdiff", FILE_NAME], stdout=subprocess.PIPE).stdout.readlines()
    for filename in filenames:
        print(patch_no, ",", filename.decode("utf-8")[:-1])
